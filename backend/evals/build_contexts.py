#!/usr/bin/env python3
"""Retrieve rag/okf/mixed contexts for each eval question (no LLM generation)."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

# Force local Qdrant if Docker is down
os.environ.setdefault("QDRANT_URL", "")

ROOT = Path(__file__).resolve().parents[1] / "rag_bot"
sys.path.insert(0, str(ROOT))

from app.mixed import retriever as mixed_retriever  # noqa: E402
from app.okf import retriever as okf_retriever  # noqa: E402
from app.rag import retriever as rag_retriever  # noqa: E402
from app.rag.intent import analyze_question  # noqa: E402
from app.rag.retriever import RetrievedChunk  # noqa: E402

EVAL_DIR = Path(__file__).resolve().parent
QUESTIONS = EVAL_DIR / "questions_50.jsonl"
OUT = EVAL_DIR / "contexts.jsonl"


def format_chunks(chunks: list[RetrievedChunk]) -> str:
    parts: list[str] = []
    for i, c in enumerate(chunks, start=1):
        header = f"[{i}] {c.source_file} | {c.section_title} | kind={c.chunk_kind}"
        if c.stat_name:
            header += f" | stat={c.stat_name}"
        if c.system:
            header += f" | system={c.system}"
        parts.append(f"{header}\n{c.text}")
    return "\n\n".join(parts)


def chunk_meta(chunks: list[RetrievedChunk]) -> list[dict]:
    return [
        {
            "source_file": c.source_file,
            "section_title": c.section_title,
            "chunk_kind": c.chunk_kind,
            "stat_name": c.stat_name,
            "score": round(c.score, 4),
            "system": c.system,
        }
        for c in chunks
    ]


def retrieve_one(bot: str, question: str, intent: str, stat_hint: str | None, query_type: str | None):
    t0 = time.perf_counter()
    if bot == "okf":
        chunks = okf_retriever.retrieve(
            question, intent=intent, stat_hint=stat_hint, query_type=query_type
        )
    elif bot == "mixed":
        chunks = mixed_retriever.retrieve(
            question, intent=intent, stat_hint=stat_hint, query_type=query_type
        )
    else:
        chunks = rag_retriever.retrieve(
            question, intent=intent, stat_hint=stat_hint, query_type=query_type
        )
    ms = (time.perf_counter() - t0) * 1000
    return chunks, ms


def main() -> None:
    rows = [json.loads(line) for line in QUESTIONS.read_text().splitlines() if line.strip()]
    out_f = OUT.open("w", encoding="utf-8")
    for row in rows:
        qid = row["id"]
        question = row["question"]
        focus = analyze_question(question)
        record = {
            "id": qid,
            "category": row.get("category"),
            "doc_focus": row.get("doc_focus"),
            "question": question,
            "intent": focus.intent,
            "stat_hint": focus.stat_hint,
            "query_type": focus.query_type,
            "bots": {},
        }
        for bot in ("rag", "okf", "mixed"):
            try:
                chunks, ms = retrieve_one(
                    bot, question, focus.intent, focus.stat_hint, focus.query_type
                )
                record["bots"][bot] = {
                    "latency_ms": round(ms, 1),
                    "n_chunks": len(chunks),
                    "context": format_chunks(chunks),
                    "sources": chunk_meta(chunks),
                    "error": None,
                }
                print(f"{qid} {bot}: {len(chunks)} chunks in {ms:.0f}ms")
            except Exception as exc:  # noqa: BLE001
                record["bots"][bot] = {
                    "latency_ms": None,
                    "n_chunks": 0,
                    "context": "",
                    "sources": [],
                    "error": str(exc),
                }
                print(f"{qid} {bot}: ERROR {exc}")
        out_f.write(json.dumps(record, ensure_ascii=False) + "\n")
        out_f.flush()
    out_f.close()
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
