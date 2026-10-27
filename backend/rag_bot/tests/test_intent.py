from app.rag.intent import detect_intent, extract_stat_hint


def test_definition_intent():
    assert detect_intent("What is rushing yards?") == "definition"


def test_framing_intent():
    assert detect_intent("How to frame query using rushing yards") == "query_framing"
    assert detect_intent("Show example queries for passing yards") == "query_framing"


def test_general_intent():
    assert detect_intent("How do I open the Team Dashboard?") == "general"


def test_stat_hint():
    assert "rushing" in (extract_stat_hint("What is rushing yards?") or "").lower()
