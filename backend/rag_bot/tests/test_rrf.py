from app.mixed.retriever import rrf_fuse
from app.rag.retriever import RetrievedChunk


def _c(text: str, system: str, score: float = 1.0) -> RetrievedChunk:
    return RetrievedChunk(
        text=text,
        source_file=f"{system}/{text}.md",
        section_title=text,
        chunk_kind="prose",
        stat_name="",
        score=score,
        system=system,
    )


def test_rrf_prefers_shared_high_ranks():
    rag = [_c("a", "rag"), _c("b", "rag"), _c("c", "rag")]
    okf = [_c("b", "okf"), _c("a", "okf"), _c("d", "okf")]
    fused = rrf_fuse([rag, okf], k=60, top_k=3)
    titles = [c.section_title for c in fused]
    assert titles[0] in {"a", "b"}
    assert "a" in titles and "b" in titles
