from pathlib import Path

from app.rag.chunking import chunk_markdown


def test_stat_rows_from_stat_search_guide():
    docs = Path(__file__).resolve().parents[2] / "docs" / "Stat-Search-Guide.md"
    chunks = chunk_markdown(docs)
    stat_rows = [c for c in chunks if c.chunk_kind == "stat_row"]
    assert len(stat_rows) > 50
    net = [c for c in stat_rows if c.stat_name and "Net Rushing Yards" in c.stat_name]
    assert net
    assert "rushing yards" in net[0].text.lower()


def test_query_types_from_functional_doc():
    docs = Path(__file__).resolve().parents[2] / "docs" / "Search-Functional-Documentation.md"
    chunks = chunk_markdown(docs)
    qt = [c for c in chunks if c.chunk_kind == "query_types"]
    assert len(qt) >= 5
    names = " ".join(c.text for c in qt).lower()
    assert "basic" in names
    assert "streak" in names
