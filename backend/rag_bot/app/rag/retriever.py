from __future__ import annotations

from dataclasses import dataclass

from qdrant_client.http import models as qm

from app.config import get_settings
from app.rag.embeddings import embed_query
from app.rag.ingest import get_qdrant


@dataclass
class RetrievedChunk:
    text: str
    source_file: str
    section_title: str
    chunk_kind: str
    stat_name: str
    score: float


def _to_chunk(point) -> RetrievedChunk:
    payload = point.payload or {}
    return RetrievedChunk(
        text=payload.get("text", ""),
        source_file=payload.get("source_file", ""),
        section_title=payload.get("section_title", ""),
        chunk_kind=payload.get("chunk_kind", "prose"),
        stat_name=payload.get("stat_name", ""),
        score=float(point.score or 0.0),
    )


def retrieve(
    question: str,
    *,
    intent: str = "general",
    stat_hint: str | None = None,
    top_k: int | None = None,
) -> list[RetrievedChunk]:
    settings = get_settings()
    client = get_qdrant()
    k = top_k or settings.top_k
    vector = embed_query(question)

    # Over-fetch then re-rank / boost by intent
    fetch_k = max(k * 3, 20)
    response = client.query_points(
        collection_name=settings.qdrant_collection,
        query=vector,
        limit=fetch_k,
        with_payload=True,
    )
    hits = [_to_chunk(p) for p in response.points]

    if intent == "definition":
        hits = _boost_definition(hits, stat_hint)
    elif intent == "query_framing":
        hits = _boost_framing(hits, question, stat_hint)

    filtered = [h for h in hits if h.score >= settings.score_threshold]
    if not filtered and hits:
        # Keep top few even if below threshold so generator can refuse gracefully
        filtered = hits[: min(3, len(hits))]
    return filtered[:k]


def _boost_definition(hits: list[RetrievedChunk], stat_hint: str | None) -> list[RetrievedChunk]:
    def key(h: RetrievedChunk) -> tuple:
        name_hit = 0
        if stat_hint and h.stat_name:
            if stat_hint.lower() in h.stat_name.lower() or h.stat_name.lower() in stat_hint.lower():
                name_hit = 2
            elif any(tok and tok in h.text.lower() for tok in stat_hint.lower().split()):
                name_hit = 1
        kind_boost = 2 if h.chunk_kind == "stat_row" else 0
        source_boost = 1 if h.source_file in {"Data-Centre.md", "Stat-Search-Guide.md"} else 0
        return (name_hit + kind_boost + source_boost, h.score)

    return sorted(hits, key=key, reverse=True)


def _boost_framing(
    hits: list[RetrievedChunk],
    question: str,
    stat_hint: str | None,
) -> list[RetrievedChunk]:
    settings = get_settings()
    client = get_qdrant()

    # Always try to include query-type rows
    query_type_hits = client.scroll(
        collection_name=settings.qdrant_collection,
        scroll_filter=qm.Filter(
            must=[qm.FieldCondition(key="chunk_kind", match=qm.MatchValue(value="query_types"))]
        ),
        limit=20,
        with_payload=True,
        with_vectors=False,
    )[0]
    extra = [
        RetrievedChunk(
            text=(p.payload or {}).get("text", ""),
            source_file=(p.payload or {}).get("source_file", ""),
            section_title=(p.payload or {}).get("section_title", ""),
            chunk_kind=(p.payload or {}).get("chunk_kind", "query_types"),
            stat_name=(p.payload or {}).get("stat_name", ""),
            score=0.99,
        )
        for p in query_type_hits
    ]

    # Prefer matching stat rows for examples
    hint = (stat_hint or "").lower().strip()
    # Prefer canonical "Net X" when user asks for X yards-style shorthand
    prefers_net = bool(hint) and "net" not in hint

    def key(h: RetrievedChunk) -> tuple:
        name_hit = 0
        name = (h.stat_name or "").lower()
        text_l = h.text.lower()
        if hint:
            if hint in name or (name and name in hint):
                name_hit = 3
            elif all(tok in name or tok in text_l for tok in hint.split() if len(tok) > 2):
                name_hit = 2
            if prefers_net and name_hit and name.startswith("net "):
                name_hit += 1
        kind_boost = 2 if h.chunk_kind in {"stat_row", "query_types"} else 0
        return (name_hit + kind_boost, h.score)

    merged = { (h.source_file, h.section_title, h.text[:80]): h for h in extra + hits }
    return sorted(merged.values(), key=key, reverse=True)
