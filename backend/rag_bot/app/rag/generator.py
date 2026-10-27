from __future__ import annotations

import time

from google import genai
from google.genai import types

from app.api.schemas import ChatResponse, Citation
from app.config import get_settings
from app.logging_utils import get_logger, timed
from app.rag.intent import detect_intent, extract_stat_hint
from app.rag.prompts import REFUSAL_MESSAGE, SYSTEM_BASE, build_user_prompt
from app.rag.retriever import RetrievedChunk, retrieve

logger = get_logger("athlyte.chat")


def _format_context(chunks: list[RetrievedChunk]) -> str:
    parts: list[str] = []
    for i, chunk in enumerate(chunks, start=1):
        header = f"[{i}] {chunk.source_file} | {chunk.section_title} | kind={chunk.chunk_kind}"
        if chunk.stat_name:
            header += f" | stat={chunk.stat_name}"
        parts.append(f"{header}\n{chunk.text}")
    return "\n\n".join(parts)


def _citations(chunks: list[RetrievedChunk]) -> list[Citation]:
    seen: set[tuple[str, str]] = set()
    out: list[Citation] = []
    for chunk in chunks:
        key = (chunk.source_file, chunk.section_title)
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


def answer_question(question: str) -> ChatResponse:
    t0 = time.perf_counter()
    preview = question.replace("\n", " ")[:120]
    logger.info("chat.start | question=%r", preview)

    with timed(logger, "chat.intent"):
        intent = detect_intent(question)
        stat_hint = extract_stat_hint(question)
    logger.info("chat.intent.done | intent=%s stat_hint=%s", intent, stat_hint or "-")

    with timed(logger, "chat.retrieve", intent=intent):
        chunks = retrieve(question, intent=intent, stat_hint=stat_hint)

    settings = get_settings()
    strong = [c for c in chunks if c.score >= settings.score_threshold]
    if intent == "query_framing":
        useful = chunks
    else:
        useful = strong or chunks

    if not useful:
        total_ms = (time.perf_counter() - t0) * 1000
        logger.info("chat.refuse | reason=no_chunks total=%.1fms", total_ms)
        return ChatResponse(
            answer=REFUSAL_MESSAGE,
            intent=intent,
            citations=[],
            grounded=False,
        )

    context = _format_context(useful)
    prompt = build_user_prompt(intent, question, context)
    logger.info(
        "chat.prompt | model=%s chunks=%s context_chars=%s prompt_chars=%s system_chars=%s",
        settings.gemini_model,
        len(useful),
        len(context),
        len(prompt),
        len(SYSTEM_BASE),
    )

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
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_BASE,
                        temperature=0.2,
                    ),
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

    text = (response.text or "").strip()
    citations = _citations(useful)
    total_ms = (time.perf_counter() - t0) * 1000
    if not text:
        logger.info("chat.refuse | reason=empty_model_text total=%.1fms", total_ms)
        return ChatResponse(
            answer=REFUSAL_MESSAGE,
            intent=intent,
            citations=citations,
            grounded=False,
        )

    logger.info(
        "chat.done | grounded=true intent=%s answer_chars=%s citations=%s total=%.1fms",
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
    )
