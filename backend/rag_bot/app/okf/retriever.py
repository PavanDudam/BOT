from __future__ import annotations

from okf import GraphExpandedRetriever, StructuredRetriever

from app.config import get_settings
from app.logging_utils import get_logger, timed
from app.okf.bundle import get_bundle
from app.rag.retriever import RetrievedChunk

logger = get_logger("athlyte.okf.retrieve")


def _hit_to_chunk(hit) -> RetrievedChunk:
    doc = hit.doc
    title = doc.title or doc.path
    body = (doc.body or "").strip()
    description = doc.description or ""
    text = body if body else description
    fm_type = doc.type or "Concept"
    stat_name = title if fm_type == "Stat" else ""
    return RetrievedChunk(
        text=text,
        source_file=doc.path,
        section_title=title,
        chunk_kind=f"okf_{fm_type.lower()}",
        stat_name=stat_name,
        score=float(hit.score or 0.0),
        system="okf",
    )


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
    bundle = get_bundle()

    type_filter: str | None = None
    if intent == "definition":
        type_filter = "Stat"
    elif intent == "query_framing" and not (stat_hint or "").strip():
        type_filter = "QueryType"

    query = question
    if stat_hint and stat_hint.lower() not in question.lower():
        query = f"{question} {stat_hint}"

    with timed(logger, "okf.search", intent=intent, type=type_filter or "-"):
        base = StructuredRetriever(bundle)
        if intent == "definition":
            # Keep definition answers on Stat concepts (graph hops pull query types).
            hits = base.search(query, limit=max(k * 2, 12), type="Stat")
        elif type_filter:
            typed = base.search(query, limit=max(k, 8), type=type_filter)
            graph = GraphExpandedRetriever(base, bundle, hops=settings.okf_expand_hops)
            expanded = graph.search(query, limit=max(k * 2, 12))
            seen = {h.doc.path for h in typed}
            hits = list(typed) + [h for h in expanded if h.doc.path not in seen]
        else:
            graph = GraphExpandedRetriever(base, bundle, hops=settings.okf_expand_hops)
            hits = graph.search(query, limit=max(k * 2, 12))

    chunks = [_hit_to_chunk(h) for h in hits]

    # Prefer exact / partial title matches (BM25 alone can favor longer compound names).
    hint = (stat_hint or "").lower().strip()
    q_l = question.lower()

    def _boost(c: RetrievedChunk) -> float:
        bonus = 0.0
        title = (c.section_title or "").lower()
        if hint:
            if title == hint:
                bonus += 20.0
            elif hint in title or title in hint:
                bonus += 12.0
        if title and title in q_l:
            bonus += 8.0
        return c.score + bonus

    chunks.sort(key=_boost, reverse=True)
    chunks = chunks[:k]

    # Framing with a known stat: ensure QueryType docs are present
    if intent == "query_framing":
        qt_docs = [d for d in bundle.docs.values() if d.type == "QueryType"]
        if query_type:
            preferred = [d for d in qt_docs if query_type.replace("_", "") in (d.path + (d.title or "")).lower().replace("_", "").replace("-", "").replace(" ", "")]
            # Fallback: match path slug
            if not preferred:
                preferred = [d for d in qt_docs if query_type in d.path]
            qt_docs = preferred or qt_docs
        existing = {c.source_file for c in chunks}
        for doc in qt_docs:
            if doc.path in existing:
                continue
            chunks.append(
                RetrievedChunk(
                    text=(doc.body or doc.description or "").strip(),
                    source_file=doc.path,
                    section_title=doc.title or doc.path,
                    chunk_kind="okf_querytype",
                    stat_name="",
                    score=0.99,
                    system="okf",
                )
            )
            existing.add(doc.path)
            if len(chunks) >= k + 4:
                break
        chunks = chunks[: max(k, 8)]

    sources = ",".join(sorted({c.source_file for c in chunks})) or "-"
    logger.info(
        "okf.retrieve.done | returned=%s intent=%s sources=[%s] stat_hint=%s",
        len(chunks),
        intent,
        sources,
        stat_hint or "-",
    )
    return chunks
