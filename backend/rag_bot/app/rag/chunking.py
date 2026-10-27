from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TABLE_SEP_RE = re.compile(r"^\|?\s*:?-{3,}")


@dataclass
class Chunk:
    text: str
    source_file: str
    section_title: str
    chunk_kind: str  # prose | stat_row | query_types
    stat_name: str | None = None
    chunk_index: int = 0


def _is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    cells = [c.strip() for c in stripped.strip("|").split("|")]
    return bool(cells) and all(TABLE_SEP_RE.match(c or "---") or set(c) <= set("-: ") for c in cells)


def _split_table_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _looks_like_stat_header(headers: list[str]) -> bool:
    joined = " ".join(h.lower() for h in headers)
    return (
        "statistic" in joined
        or "what it measures" in joined
        or "definition" in joined
        or "search terms" in joined
        or ("alias" in joined and len(headers) >= 2)
    )


def _looks_like_query_types_header(headers: list[str]) -> bool:
    joined = " ".join(h.lower() for h in headers)
    return "query type" in joined and "example" in joined


def _chunk_stat_row(
    headers: list[str],
    cells: list[str],
    source_file: str,
    section_title: str,
) -> Chunk | None:
    if len(cells) < 2:
        return None
    # Pad / trim to header length
    while len(cells) < len(headers):
        cells.append("")
    cells = cells[: len(headers)]
    pairs = list(zip(headers, cells))
    stat_name = cells[0].strip()
    if not stat_name or stat_name.lower() in {"statistic name", "stat", "name"}:
        return None

    lines = [f"Statistic: {stat_name}"]
    for header, value in pairs[1:]:
        if value:
            lines.append(f"{header}: {value}")
    text = "\n".join(lines)
    return Chunk(
        text=text,
        source_file=source_file,
        section_title=section_title,
        chunk_kind="stat_row",
        stat_name=stat_name,
    )


def _chunk_query_type_row(
    headers: list[str],
    cells: list[str],
    source_file: str,
    section_title: str,
) -> Chunk | None:
    if len(cells) < 2:
        return None
    while len(cells) < len(headers):
        cells.append("")
    cells = cells[: len(headers)]
    query_type = cells[0].strip()
    if not query_type or query_type.lower() == "query type":
        return None
    lines = [f"Query Type: {query_type}"]
    for header, value in zip(headers[1:], cells[1:]):
        if value:
            lines.append(f"{header}: {value}")
    return Chunk(
        text="\n".join(lines),
        source_file=source_file,
        section_title=section_title,
        chunk_kind="query_types",
        stat_name=None,
    )


def _flush_prose(
    buffer: list[str],
    source_file: str,
    section_title: str,
    chunks: list[Chunk],
) -> None:
    text = "\n".join(buffer).strip()
    buffer.clear()
    if not text:
        return
    # Split long prose into ~1200 char windows with overlap
    max_len = 1200
    overlap = 150
    if len(text) <= max_len:
        chunks.append(
            Chunk(
                text=text,
                source_file=source_file,
                section_title=section_title,
                chunk_kind="prose",
            )
        )
        return
    start = 0
    while start < len(text):
        end = min(len(text), start + max_len)
        piece = text[start:end].strip()
        if piece:
            chunks.append(
                Chunk(
                    text=piece,
                    source_file=source_file,
                    section_title=section_title,
                    chunk_kind="prose",
                )
            )
        if end >= len(text):
            break
        start = max(0, end - overlap)


def chunk_markdown(path: Path) -> list[Chunk]:
    source_file = path.name
    lines = path.read_text(encoding="utf-8").splitlines()
    chunks: list[Chunk] = []
    section_parts: list[str] = []
    prose_buf: list[str] = []
    i = 0

    def section_title() -> str:
        return " > ".join(section_parts) if section_parts else source_file

    while i < len(lines):
        line = lines[i]
        heading = HEADING_RE.match(line)
        if heading:
            _flush_prose(prose_buf, source_file, section_title(), chunks)
            level = len(heading.group(1))
            title = heading.group(2).strip()
            section_parts = section_parts[: level - 1]
            section_parts.append(title)
            prose_buf.append(line)
            i += 1
            continue

        # Detect markdown table
        if line.strip().startswith("|") and i + 1 < len(lines) and _is_table_separator(lines[i + 1]):
            _flush_prose(prose_buf, source_file, section_title(), chunks)
            headers = _split_table_row(line)
            i += 2  # skip header + separator
            is_stat = _looks_like_stat_header(headers)
            is_query = _looks_like_query_types_header(headers)
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = _split_table_row(lines[i])
                if is_stat:
                    row = _chunk_stat_row(headers, cells, source_file, section_title())
                    if row:
                        chunks.append(row)
                elif is_query:
                    row = _chunk_query_type_row(headers, cells, source_file, section_title())
                    if row:
                        chunks.append(row)
                else:
                    # Generic table row as prose-like chunk
                    paired = "; ".join(
                        f"{h}: {c}" for h, c in zip(headers, cells) if c.strip()
                    )
                    if paired:
                        chunks.append(
                            Chunk(
                                text=paired,
                                source_file=source_file,
                                section_title=section_title(),
                                chunk_kind="prose",
                            )
                        )
                i += 1
            continue

        prose_buf.append(line)
        i += 1

    _flush_prose(prose_buf, source_file, section_title(), chunks)
    for idx, chunk in enumerate(chunks):
        chunk.chunk_index = idx
    return chunks


def chunk_docs_dir(docs_path: Path) -> list[Chunk]:
    files = sorted(docs_path.glob("*.md"))
    all_chunks: list[Chunk] = []
    for path in files:
        all_chunks.extend(chunk_markdown(path))
    return all_chunks
