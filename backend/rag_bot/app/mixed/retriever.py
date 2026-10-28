from __future__ import annotations

from app.config import get_settings
from app.logging_utils import get_logger, timed
from app.okf import retriever as okf_retriever
from app.rag import retriever as rag_retriever
from app.rag.retriever import RetrievedChunk

logger = get_logger("athlyte.mixed.retrieve")


def _chunk_key(chunk: RetrievedChunk) -> str:
    return f"{chunk.system}|{chunk.source_file}|{chunk.section_title}|{chunk.text[:100]}"


def rrf_fuse(
    ranked_lists: list[list[RetrievedChunk]],
    *,
    k: int,
    top_k: int,
) -> list[RetrievedChunk]:
    scores: dict[str, float] = {}
    best: dict[str, RetrievedChunk] = {}
    for hits in ranked_lists:
        for rank, chunk in enumerate(hits, start=1):
            key = _chunk_key(chunk)
            scores[key] = scores.get(key, 0.0) + 1.0 / (k + rank)
            prev = best.get(key)
            if prev is None or chunk.score > prev.score:
                best[key] = chunk

    ordered = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    out: list[RetrievedChunk] = []
    for key, rrf_score in ordered[:top_k]:
        base = best[key]
        out.append(
            RetrievedChunk(
                text=base.text,
                source_file=base.source_file,
                section_title=base.section_title,
                chunk_kind=base.chunk_kind,
                stat_name=base.stat_name,
                score=rrf_score,
                system=base.system,
            )
        )
    return out


def retrieve(
    question: str,
    *,
    intent: str = "general",
    stat_hint: str | None = None,
    query_type: str | None = None,
    top_k: int | None = None,
) -> list[RetrievedChunk]:
    settings = get_settings()
    k = top_k or settings.top_k
    fetch = max(k * 2, 12)

    with timed(logger, "mixed.rag_leg"):
        rag_hits = rag_retriever.retrieve(
            question,
            intent=intent,
            stat_hint=stat_hint,
            query_type=query_type,
            top_k=fetch,
        )

    with timed(logger, "mixed.okf_leg"):
        try:
            okf_hits = okf_retriever.retrieve(
                question,
                intent=intent,
                stat_hint=stat_hint,
                query_type=query_type,
                top_k=fetch,
            )
        except FileNotFoundError:
            logger.warning("mixed.okf_missing | falling back to rag-only")
            okf_hits = []

    with timed(logger, "mixed.rrf", rag=len(rag_hits), okf=len(okf_hits)):
        fused = rrf_fuse([rag_hits, okf_hits], k=settings.rrf_k, top_k=k)

    systems = ",".join(sorted({c.system or "?" for c in fused})) or "-"
    logger.info(
        "mixed.retrieve.done | returned=%s systems=[%s] rag=%s okf=%s",
        len(fused),
        systems,
        len(rag_hits),
        len(okf_hits),
    )
    return fused
