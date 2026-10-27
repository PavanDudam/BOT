from __future__ import annotations

import re

_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC_UNDERSCORE = re.compile(r"__(.+?)__")
_ITALIC_STAR = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")
_CODE = re.compile(r"`([^`]+)`")
_HEADING = re.compile(r"^#{1,6}\s*", re.MULTILINE)
_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def clean_plain_text(text: str) -> str:
    """Strip common Markdown so the UI shows clean human text."""
    if not text:
        return text
    text = _BOLD.sub(r"\1", text)
    text = _ITALIC_UNDERSCORE.sub(r"\1", text)
    text = _ITALIC_STAR.sub(r"\1", text)
    text = _CODE.sub(r"\1", text)
    text = _LINK.sub(r"\1", text)
    text = _HEADING.sub("", text)
    # leftover markers from partial stream chunks
    text = text.replace("**", "").replace("__", "").replace("`", "")
    return text
