from __future__ import annotations

import re
from dataclasses import dataclass

DEFINITION_RE = re.compile(
    r"\b(what\s+is|what'?s|define|definition\s+of|meaning\s+of|explain\s+what)\b",
    re.I,
)
FRAMING_RE = re.compile(
    r"\b("
    r"how\s+to\s+(frame|write|build|make|search|query)|"
    r"frame\s+(a\s+)?query|"
    r"example\s+quer(y|ies)|"
    r"query\s+types?|"
    r"sample\s+quer(y|ies)|"
    r"how\s+(do|can)\s+i\s+(search|query|ask|frame)|"
    r"write\s+quer(y|ies)"
    r")\b",
    re.I,
)

# Order matters: more specific patterns first.
QUERY_TYPE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("streaks", re.compile(r"\bstreaks?\b|\bconsecutive(?:\s+games?)?\b|\bstraight\s+games?\b", re.I)),
    ("last_time", re.compile(r"\blast\s+time\b|\bltw\b|\blast\s+time\s+when\b|\blast\s+time\s+was\b", re.I)),
    ("records", re.compile(r"\brecords?\b|\bmaximum\b|\bminimum\b|\bhighest\b|\blowest\b|\bmost\b|\bfewest\b", re.I)),
    ("complex", re.compile(r"\bcomplex\b", re.I)),
    ("basic", re.compile(r"\bbasic\b", re.I)),
    ("count", re.compile(r"\bcount\b|\bin\s+how\s+many\b", re.I)),
    ("rank", re.compile(r"\brank\b|\bnth[- ]?most\b|\b9th[- ]?most\b", re.I)),
    ("trend", re.compile(r"\btrend\b|\bon\s+the\s+rise\b", re.I)),
]

QUERY_TYPE_LABELS = {
    "basic": "Stat Search (Basic)",
    "complex": "Stat Search (Complex)",
    "records": "Records (Maximum / Minimum)",
    "last_time": "Last Time",
    "streaks": "Streaks",
    "count": "Count",
    "rank": "Rank",
    "trend": "Trend",
}

NOISE_WORDS_RE = re.compile(
    r"\b("
    r"a|an|the|query|queries|quer(?:y|ies)|stat|statistic|stats|"
    r"in\s+athlyte|athlyte|search|searches|type|types|"
    r"frame|framing|write|writing|build|make|example|examples|sample|samples|"
    r"streak|streaks|basic|complex|record|records|ltw|count|rank|trend|"
    r"last\s+time|consecutive|straight|maximum|minimum|highest|lowest|"
    r"how\s+to|for|using|with|about"
    r")\b",
    re.I,
)


@dataclass
class QuestionFocus:
    intent: str
    stat_hint: str | None = None
    query_type: str | None = None


def detect_intent(question: str) -> str:
    q = question.strip()
    if FRAMING_RE.search(q):
        return "query_framing"
    if DEFINITION_RE.search(q):
        return "definition"
    return "general"


def extract_query_type(question: str) -> str | None:
    q = question.strip()
    # Prefer explicit "streak query" / "basic query" shapes
    for key, pattern in QUERY_TYPE_PATTERNS:
        if pattern.search(q):
            # Avoid treating "highest" in random questions as records unless framing-ish
            if key == "records" and not FRAMING_RE.search(q) and not re.search(
                r"\brecord\b", q, re.I
            ):
                # still allow "how to frame a record query"
                if not re.search(r"\b(record|records|maximum|minimum)\s+quer", q, re.I):
                    if not re.search(r"\bquer(?:y|ies)\b.*\b(record|max|min|highest|lowest)", q, re.I):
                        if not re.search(r"\b(record|max|min|highest|lowest).*\bquer", q, re.I):
                            continue
            return key
    return None


def extract_stat_hint(question: str) -> str | None:
    """Best-effort pull of the stat phrase from common question shapes."""
    patterns = [
        r"what\s+is\s+(.+?)[\?\.]?\s*$",
        r"definition\s+of\s+(.+?)[\?\.]?\s*$",
        r"meaning\s+of\s+(.+?)[\?\.]?\s*$",
        r"(?:using|for|with|about)\s+(?:the\s+)?(?:stat(?:istic)?\s+)?(.+?)[\?\.]?\s*$",
        r"frame\s+(?:a\s+)?query\s+(?:using|for|with)\s+(.+?)[\?\.]?\s*$",
        r"(?:quer(?:y|ies)|search(?:es)?)\s+(?:using|for|with|about)\s+(.+?)[\?\.]?\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, question.strip(), re.I)
        if match:
            hint = match.group(1).strip(" ?.")
            hint = NOISE_WORDS_RE.sub(" ", hint)
            hint = re.sub(r"\s+", " ", hint).strip(" ?.-")
            # Reject hints that are only query-type words or empty
            if not hint or extract_query_type(hint):
                continue
            if len(hint) < 2:
                continue
            return hint
    return None


def analyze_question(question: str) -> QuestionFocus:
    intent = detect_intent(question)
    query_type = extract_query_type(question) if intent == "query_framing" else None
    # For framing questions like "streak query", don't treat type name as a stat
    stat_hint = extract_stat_hint(question)
    if stat_hint and query_type and extract_query_type(stat_hint) == query_type:
        stat_hint = None
    if stat_hint:
        # strip residual type words from mixed phrases like "streak sacks"
        cleaned = NOISE_WORDS_RE.sub(" ", stat_hint)
        cleaned = re.sub(r"\s+", " ", cleaned).strip(" ?.-")
        stat_hint = cleaned or None
    return QuestionFocus(intent=intent, stat_hint=stat_hint, query_type=query_type)
