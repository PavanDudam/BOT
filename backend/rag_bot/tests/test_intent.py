from app.rag.intent import analyze_question, detect_intent, extract_query_type, extract_stat_hint


def test_definition_intent():
    assert detect_intent("What is rushing yards?") == "definition"


def test_framing_intent():
    assert detect_intent("How to frame query using rushing yards") == "query_framing"
    assert detect_intent("Show example queries for passing yards") == "query_framing"


def test_general_intent():
    assert detect_intent("How do I open the Team Dashboard?") == "general"


def test_stat_hint():
    assert "rushing" in (extract_stat_hint("What is rushing yards?") or "").lower()


def test_streak_query_focus():
    focus = analyze_question("how to frame a streak query")
    assert focus.intent == "query_framing"
    assert focus.query_type == "streaks"
    assert focus.stat_hint is None


def test_framing_with_stat_and_type():
    focus = analyze_question("how to frame a streak query for sacks")
    assert focus.intent == "query_framing"
    assert focus.query_type == "streaks"
    assert focus.stat_hint is not None
    assert "sack" in focus.stat_hint.lower()


def test_extract_query_types():
    assert extract_query_type("how to write a basic query") == "basic"
    assert extract_query_type("example last time queries") == "last_time"
