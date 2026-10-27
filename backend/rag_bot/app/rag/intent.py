from __future__ import annotations

import re

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


def detect_intent(question: str) -> str:
    q = question.strip()
    if FRAMING_RE.search(q):
        return "query_framing"
    if DEFINITION_RE.search(q):
        return "definition"
    return "general"


def extract_stat_hint(question: str) -> str | None:
    """Best-effort pull of the stat phrase from common question shapes."""
    patterns = [
        r"what\s+is\s+(.+?)[\?\.]?\s*$",
        r"definition\s+of\s+(.+?)[\?\.]?\s*$",
        r"meaning\s+of\s+(.+?)[\?\.]?\s*$",
        r"(?:using|for|with|about)\s+(.+?)[\?\.]?\s*$",
        r"frame\s+(?:a\s+)?query\s+(?:using|for|with)\s+(.+?)[\?\.]?\s*$",
    ]
    for pattern in patterns:
        match = re.search(pattern, question.strip(), re.I)
        if match:
            hint = match.group(1).strip(" ?.")
            hint = re.sub(
                r"\b(a|an|the|query|queries|stat|statistic|in\s+athlyte)\b",
                "",
                hint,
                flags=re.I,
            ).strip(" ?.")
            if hint:
                return hint
    return None
