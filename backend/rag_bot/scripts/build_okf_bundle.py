#!/usr/bin/env python3
"""Build an Athlyte OKF bundle from backend/docs markdown."""

from __future__ import annotations

import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.config import get_settings  # noqa: E402
from app.rag.chunking import chunk_docs_dir  # noqa: E402

QUERY_TYPE_DEFS: list[tuple[str, str, str]] = [
    (
        "basic",
        "Stat Search (Basic)",
        "Single-stat search with qualifiers and a period. Example: Players with rushing yards greater than 10.",
    ),
    (
        "complex",
        "Stat Search (Complex)",
        "1–3 stats combined with AND/OR. Example: Teams with at least 20 passing attempts and three field goals made in a game.",
    ),
    (
        "records",
        "Records (Maximum / Minimum)",
        "Highest or lowest values for a single stat. Example: Highest number of touchdowns scored.",
    ),
    (
        "last_time",
        "Last Time",
        "Most recent occurrence matching up to 3 stats. Example: Last time any team had at least 3 touchdowns in a game.",
    ),
    (
        "streaks",
        "Streaks",
        "Consecutive-game patterns for 1–2 stats (game period only; no qualifiers). Example: Players with 12 receiving yards over 6 consecutive games.",
    ),
    (
        "count",
        "Count",
        "How many games/events match a condition. Example: In how many games did Bryce Young have greater than 80 rushing yards.",
    ),
    (
        "rank",
        "Rank",
        "Nth-most / ranked results. Example: Players at the 9th-most rushing yards in 1st quarter.",
    ),
    (
        "trend",
        "Trend",
        "Whether a metric is rising or changing over a season. Example: Is Alabama's rushing yards on the rise in a season during the regular season.",
    ),
]

SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(name: str) -> str:
    slug = SLUG_RE.sub("_", name.lower()).strip("_")
    return (slug[:96] or "unnamed")


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def write_doc(path: Path, *, doc_type: str, title: str, description: str, tags: list[str], body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tag_line = "[" + ", ".join(f'"{yaml_escape(t)}"' for t in tags) + "]"
    content = (
        "---\n"
        f'type: "{yaml_escape(doc_type)}"\n'
        f'title: "{yaml_escape(title)}"\n'
        f'description: "{yaml_escape(description[:240])}"\n'
        f"tags: {tag_line}\n"
        "---\n\n"
        f"{body.strip()}\n"
    )
    path.write_text(content, encoding="utf-8")


def build_bundle(docs_path: Path, out_path: Path) -> dict[str, int]:
    if out_path.exists():
        shutil.rmtree(out_path)
    out_path.mkdir(parents=True)

    chunks = chunk_docs_dir(docs_path)
    stats: dict[str, dict] = {}
    guides: list[dict] = []
    query_examples: dict[str, list[str]] = defaultdict(list)

    # Prefer Stat-Search-Guide rows (richer search terms / examples) over Data-Centre.
    preferred_sources = ("Stat-Search-Guide.md", "Data-Centre.md")

    for chunk in chunks:
        if chunk.chunk_kind == "stat_row" and chunk.stat_name:
            key = slugify(chunk.stat_name)
            existing = stats.get(key)
            prefer = chunk.source_file in preferred_sources
            if existing is None:
                stats[key] = {
                    "name": chunk.stat_name,
                    "text": chunk.text,
                    "section": chunk.section_title,
                    "source": chunk.source_file,
                    "preferred": prefer,
                }
            elif prefer and not existing["preferred"]:
                stats[key] = {
                    "name": chunk.stat_name,
                    "text": chunk.text,
                    "section": chunk.section_title,
                    "source": chunk.source_file,
                    "preferred": True,
                }
            elif prefer and existing["preferred"] and chunk.source_file == "Stat-Search-Guide.md":
                # Merge example lines if missing
                if "Example" in chunk.text and "Example" not in existing["text"]:
                    existing["text"] = existing["text"] + "\n" + chunk.text
        elif chunk.chunk_kind == "query_types":
            first = chunk.text.splitlines()[0] if chunk.text else ""
            label = first.replace("Query Type:", "").strip()
            slug = slugify(label)
            for key, title, _ in QUERY_TYPE_DEFS:
                if key in slug or slugify(title) == slug or key.replace("_", " ") in label.lower():
                    query_examples[key].append(chunk.text)
                    break
        elif chunk.chunk_kind == "prose" and chunk.source_file in {
            "Navigation-Guide.md",
            "Search-Functional-Documentation.md",
            "Export-Report-Records.md",
            "R3-Features.md",
            "Athlyte-Search-User-Guide.md",
        }:
            if len(chunk.text) < 80:
                continue
            guides.append(
                {
                    "title": chunk.section_title or chunk.source_file,
                    "text": chunk.text,
                    "source": chunk.source_file,
                    "section": chunk.section_title,
                }
            )

    # Query type docs
    qt_links: list[str] = []
    for key, title, description in QUERY_TYPE_DEFS:
        extras = query_examples.get(key, [])
        body_parts = [
            f"# {title}",
            "",
            description,
            "",
            f"Source notes from Athlyte docs for **{title}**.",
        ]
        if extras:
            body_parts.append("")
            body_parts.append("## Examples from docs")
            for ex in extras[:3]:
                body_parts.append("")
                body_parts.append(ex)
        body_parts.extend(
            [
                "",
                "## Related",
                "",
                "Use this query type with any [Stat](../index.md#stats) concept.",
            ]
        )
        rel = f"query_types/{key}.md"
        write_doc(
            out_path / rel,
            doc_type="QueryType",
            title=title,
            description=description,
            tags=["query_type", key, "athlyte"],
            body="\n".join(body_parts),
        )
        qt_links.append(f"- [{title}]({rel})")

    # Stat docs with links to all query types (graph expansion for framing)
    qt_md_links = "\n".join(f"- [{title}](../query_types/{key}.md)" for key, title, _ in QUERY_TYPE_DEFS)
    stat_links: list[str] = []
    for key, info in sorted(stats.items(), key=lambda kv: kv[1]["name"].lower()):
        body = (
            f"# {info['name']}\n\n"
            f"{info['text']}\n\n"
            f"Section: {info['section']}\n"
            f"Source file: {info['source']}\n\n"
            f"## How to frame queries\n\n"
            f"Related Athlyte query types:\n\n"
            f"{qt_md_links}\n"
        )
        rel = f"stats/{key}.md"
        write_doc(
            out_path / rel,
            doc_type="Stat",
            title=info["name"],
            description=info["text"].splitlines()[0][:200] if info["text"] else info["name"],
            tags=["stat", "athlyte", slugify(info["section"].split(">")[0])[:40]],
            body=body,
        )
        stat_links.append(f"- [{info['name']}]({rel})")

    # Guide docs (cap to keep bundle focused)
    guide_links: list[str] = []
    seen_guide: set[str] = set()
    for i, g in enumerate(guides[:80]):
        slug = slugify(f"{g['source']}_{g['title']}")[:80]
        if slug in seen_guide:
            continue
        seen_guide.add(slug)
        rel = f"guides/{slug}.md"
        write_doc(
            out_path / rel,
            doc_type="Guide",
            title=g["title"][:120],
            description=g["text"][:200].replace("\n", " "),
            tags=["guide", "athlyte", slugify(Path(g["source"]).stem)],
            body=f"# {g['title']}\n\n{g['text']}\n\nSource: {g['source']}\n",
        )
        guide_links.append(f"- [{g['title']}]({rel})")

    index_body = (
        "# Athlyte Search Knowledge Bundle\n\n"
        "OKF concepts generated from Athlyte product documentation.\n\n"
        "## Query types\n\n"
        + "\n".join(qt_links)
        + "\n\n## Stats\n\n"
        + "\n".join(stat_links[:400])
        + "\n\n## Guides\n\n"
        + "\n".join(guide_links)
        + "\n"
    )
    write_doc(
        out_path / "index.md",
        doc_type="Index",
        title="Athlyte Search Knowledge Bundle",
        description="Stats, query types, and product guides for Athlyte Search",
        tags=["index", "athlyte"],
        body=index_body,
    )

    return {
        "stats": len(stats),
        "query_types": len(QUERY_TYPE_DEFS),
        "guides": len(guide_links),
        "total_md": len(list(out_path.rglob("*.md"))),
    }


def main() -> None:
    settings = get_settings()
    counts = build_bundle(settings.docs_path, settings.okf_bundle_path)
    print(f"OKF bundle written to {settings.okf_bundle_path}")
    print(
        f"  stats={counts['stats']} query_types={counts['query_types']} "
        f"guides={counts['guides']} total_md={counts['total_md']}"
    )


if __name__ == "__main__":
    main()
