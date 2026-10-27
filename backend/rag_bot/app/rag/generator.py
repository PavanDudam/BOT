from __future__ import annotations

import json
import time
from collections.abc import Iterator
from typing import Any, Literal

from google import genai
from google.genai import types

from app.api.schemas import ChatResponse, Citation
from app.config import get_settings
from app.logging_utils import get_logger, timed
from app.mixed import retriever as mixed_retriever
from app.okf import retriever as okf_retriever
from app.rag.intent import QUERY_TYPE_LABELS, analyze_question
from app.rag.prompts import REFUSAL_MESSAGE, SYSTEM_BASE, build_user_prompt
from app.rag.retriever import RetrievedChunk, retrieve as rag_retrieve
from app.rag.text_clean import clean_plain_text

logger = get_logger("athlyte.chat")

BotName = Literal["rag", "okf", "mixed"]


def _format_context(chunks: list[RetrievedChunk]) -> str:
    parts: list[str] = []
    for i, chunk in enumerate(chunks, start=1):
        header = f"[{i}] {chunk.source_file} | {chunk.section_title} | kind={chunk.chunk_kind}"
        if chunk.stat_name:
            header += f" | stat={chunk.stat_name}"
        if chunk.system:
            header += f" | system={chunk.system}"
        parts.append(f"{header}\n{chunk.text}")
    return "\n\n".join(parts)


def _citations(chunks: list[RetrievedChunk]) -> list[Citation]:
    seen: set[tuple[str, str, str | None]] = set()
    out: list[Citation] = []
    for chunk in chunks:
        key = (chunk.source_file, chunk.section_title, chunk.system)
        if key in seen:
            continue
        seen.add(key)
        snippet = chunk.text.replace("\n", " ")
        if len(snippet) > 220:
            snippet = snippet[:217] + "..."
        out.append(
            Citation(
                source=chunk.source_file,
                section=chunk.section_title,
                snippet=snippet,
                system=chunk.system,
            )
        )
    return out[:8]


def _gemini_client() -> genai.Client:
    settings = get_settings()
    if not settings.google_api_key:
        raise RuntimeError("GOOGLE_API_KEY is not set")
    return genai.Client(api_key=settings.google_api_key)


def _usage_dict(response) -> dict[str, int | None]:
    usage = getattr(response, "usage_metadata", None)
    if usage is None:
        return {
            "prompt_tokens": None,
            "output_tokens": None,
            "total_tokens": None,
        }
    return {
        "prompt_tokens": getattr(usage, "prompt_token_count", None),
        "output_tokens": getattr(usage, "candidates_token_count", None),
        "total_tokens": getattr(usage, "total_token_count", None),
    }


def _dispatch_retrieve(
    bot: BotName,
    question: str,
    *,
    intent: str,
    stat_hint: str | None,
    query_type: str | None,
) -> list[RetrievedChunk]:
    kwargs = {
        "intent": intent,
        "stat_hint": stat_hint,
        "query_type": query_type,
    }
    if bot == "okf":
        return okf_retriever.retrieve(question, **kwargs)
    if bot == "mixed":
        return mixed_retriever.retrieve(question, **kwargs)
    return rag_retrieve(question, **kwargs)


def _prepare(
    question: str,
    bot: BotName = "rag",
) -> tuple[str, str | None, list[RetrievedChunk], str, str]:
    """Intent + retrieve + prompt. Empty chunks means refuse path."""
    with timed(logger, "chat.intent"):
        focus = analyze_question(question)
        intent = focus.intent
        stat_hint = focus.stat_hint
        query_type = focus.query_type
    logger.info(
        "chat.intent.done | bot=%s intent=%s stat_hint=%s query_type=%s",
        bot,
        intent,
        stat_hint or "-",
        query_type or "-",
    )

    with timed(logger, "chat.retrieve", intent=intent, bot=bot):
        chunks = _dispatch_retrieve(
            bot,
            question,
            intent=intent,
            stat_hint=stat_hint,
            query_type=query_type,
        )

    settings = get_settings()
    # OKF/mixed scores are not cosine similarities — skip dense threshold.
    if bot in {"okf", "mixed"} or intent == "query_framing":
        useful = chunks
    else:
        strong = [c for c in chunks if c.score >= settings.score_threshold]
        useful = strong or chunks

    if not useful:
        return intent, stat_hint, [], "", ""

    context = _format_context(useful)
    prompt = build_user_prompt(
        intent,
        question,
        context,
        stat_hint=stat_hint,
        query_type=query_type,
        query_type_label=QUERY_TYPE_LABELS.get(query_type or "", query_type),
    )
    logger.info(
        "chat.prompt | bot=%s model=%s temp=%s chunks=%s context_chars=%s prompt_chars=%s",
        bot,
        settings.gemini_model,
        settings.gemini_temperature,
        len(useful),
        len(context),
        len(prompt),
    )
    return intent, stat_hint, useful, context, prompt


def _gen_config() -> types.GenerateContentConfig:
    settings = get_settings()
    return types.GenerateContentConfig(
        system_instruction=SYSTEM_BASE,
        temperature=settings.gemini_temperature,
    )


def answer_question(question: str, bot: BotName = "rag") -> ChatResponse:
    t0 = time.perf_counter()
    preview = question.replace("\n", " ")[:120]
    logger.info("chat.start | question=%r mode=sync bot=%s", preview, bot)

    intent, _stat_hint, useful, _context, prompt = _prepare(question, bot=bot)

    if not useful:
        total_ms = (time.perf_counter() - t0) * 1000
        logger.info("chat.refuse | reason=no_chunks bot=%s total=%.1fms", bot, total_ms)
        return ChatResponse(
            answer=REFUSAL_MESSAGE,
            intent=intent,
            citations=[],
            grounded=False,
            bot=bot,
        )

    settings = get_settings()
    client = _gemini_client()
    last_error: Exception | None = None
    response = None
    attempts = 0
    with timed(logger, "chat.gemini", model=settings.gemini_model) as gemini_timing:
        for attempt in range(4):
            attempts = attempt + 1
            try:
                response = client.models.generate_content(
                    model=settings.gemini_model,
                    contents=prompt,
                    config=_gen_config(),
                )
                break
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                msg = str(exc)
                logger.warning("chat.gemini.retry | attempt=%s error=%s", attempts, msg[:200])
                if "503" in msg or "UNAVAILABLE" in msg or "high demand" in msg.lower():
                    time.sleep(1.5 * attempts)
                    continue
                raise

    if response is None:
        raise RuntimeError(f"Gemini unavailable after retries: {last_error}") from last_error

    usage = _usage_dict(response)
    logger.info(
        "chat.tokens | model=%s attempts=%s prompt_tokens=%s output_tokens=%s total_tokens=%s gemini_ms=%.1f",
        settings.gemini_model,
        attempts,
        usage["prompt_tokens"],
        usage["output_tokens"],
        usage["total_tokens"],
        gemini_timing.get("ms", 0.0),
    )

    text = clean_plain_text((response.text or "").strip())
    citations = _citations(useful)
    total_ms = (time.perf_counter() - t0) * 1000
    if not text:
        logger.info("chat.refuse | reason=empty_model_text bot=%s total=%.1fms", bot, total_ms)
        return ChatResponse(
            answer=REFUSAL_MESSAGE,
            intent=intent,
            citations=citations,
            grounded=False,
            bot=bot,
        )

    logger.info(
        "chat.done | grounded=true bot=%s intent=%s answer_chars=%s citations=%s total=%.1fms",
        bot,
        intent,
        len(text),
        len(citations),
        total_ms,
    )
    return ChatResponse(
        answer=text,
        intent=intent,
        citations=citations,
        grounded=True,
        bot=bot,
    )


def _sse(payload: dict[str, Any]) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


def stream_answer(question: str, bot: BotName = "rag") -> Iterator[str]:
    """Yield SSE events: meta → token* → done | error | refuse."""
    t0 = time.perf_counter()
    preview = question.replace("\n", " ")[:120]
    logger.info("chat.start | question=%r mode=stream bot=%s", preview, bot)

    try:
        intent, _stat_hint, useful, _context, prompt = _prepare(question, bot=bot)

        if not useful:
            total_ms = (time.perf_counter() - t0) * 1000
            logger.info("chat.refuse | reason=no_chunks bot=%s total=%.1fms", bot, total_ms)
            yield _sse(
                {
                    "type": "meta",
                    "bot": bot,
                    "intent": intent,
                    "citations": [],
                    "grounded": False,
                }
            )
            yield _sse({"type": "token", "text": REFUSAL_MESSAGE})
            yield _sse({"type": "done", "grounded": False, "bot": bot, "total_ms": round(total_ms, 1)})
            return

        citations = [c.model_dump() for c in _citations(useful)]
        yield _sse(
            {
                "type": "meta",
                "bot": bot,
                "intent": intent,
                "citations": citations,
                "grounded": True,
            }
        )

        settings = get_settings()
        client = _gemini_client()
        answer_parts: list[str] = []
        last_usage = None

        with timed(logger, "chat.gemini_stream", model=settings.gemini_model) as gemini_timing:
            stream = client.models.generate_content_stream(
                model=settings.gemini_model,
                contents=prompt,
                config=_gen_config(),
            )
            for chunk in stream:
                piece = getattr(chunk, "text", None) or ""
                if piece:
                    cleaned = clean_plain_text(piece)
                    if cleaned:
                        answer_parts.append(cleaned)
                        yield _sse({"type": "token", "text": cleaned})
                if getattr(chunk, "usage_metadata", None) is not None:
                    last_usage = chunk

        usage = _usage_dict(last_usage) if last_usage else _usage_dict(None)
        total_ms = (time.perf_counter() - t0) * 1000
        full = "".join(answer_parts).strip()
        grounded = bool(full)
        if not full:
            yield _sse({"type": "token", "text": REFUSAL_MESSAGE})
            grounded = False

        logger.info(
            "chat.tokens | model=%s prompt_tokens=%s output_tokens=%s total_tokens=%s gemini_ms=%.1f",
            settings.gemini_model,
            usage["prompt_tokens"],
            usage["output_tokens"],
            usage["total_tokens"],
            gemini_timing.get("ms", 0.0),
        )
        logger.info(
            "chat.done | grounded=%s bot=%s intent=%s answer_chars=%s citations=%s total=%.1fms mode=stream",
            grounded,
            bot,
            intent,
            len(full),
            len(citations),
            total_ms,
        )
        yield _sse({"type": "done", "grounded": grounded, "bot": bot, "total_ms": round(total_ms, 1)})
    except Exception as exc:  # noqa: BLE001
        logger.exception("chat.stream_error | bot=%s", bot)
        yield _sse({"type": "error", "message": str(exc)})
