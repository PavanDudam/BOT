from __future__ import annotations

import time

from google import genai
from google.genai import types

from app.api.schemas import ChatResponse, Citation
from app.config import get_settings
from app.rag.intent import detect_intent, extract_stat_hint
from app.rag.prompts import REFUSAL_MESSAGE, SYSTEM_BASE, build_user_prompt
from app.rag.retriever import RetrievedChunk, retrieve


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


def answer_question(question: str) -> ChatResponse:
    intent = detect_intent(question)
    stat_hint = extract_stat_hint(question)
    chunks = retrieve(question, intent=intent, stat_hint=stat_hint)

    settings = get_settings()
    strong = [c for c in chunks if c.score >= settings.score_threshold]
    if intent == "query_framing":
        # query_types injected with high score; require at least one real hit
        useful = chunks
    else:
        useful = strong or chunks

    if not useful:
        return ChatResponse(
            answer=REFUSAL_MESSAGE,
            intent=intent,
            citations=[],
            grounded=False,
        )

    context = _format_context(useful)
    prompt = build_user_prompt(intent, question, context)
    client = _gemini_client()
    last_error: Exception | None = None
    response = None
    for attempt in range(4):
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
            if "503" in msg or "UNAVAILABLE" in msg or "high demand" in msg.lower():
                time.sleep(1.5 * (attempt + 1))
                continue
            raise
    if response is None:
        raise RuntimeError(f"Gemini unavailable after retries: {last_error}") from last_error
    text = (response.text or "").strip()
    if not text:
        return ChatResponse(
            answer=REFUSAL_MESSAGE,
            intent=intent,
            citations=_citations(useful),
            grounded=False,
        )

    return ChatResponse(
        answer=text,
        intent=intent,
        citations=_citations(useful),
        grounded=True,
    )
