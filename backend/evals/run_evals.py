#!/usr/bin/env python3
"""Run golden questions against rag / okf / mixed on a single API."""

from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path

import httpx

BOTS = ("rag", "okf", "mixed")
ROOT = Path(__file__).resolve().parent


def load_golden(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare retrieval bots on golden questions")
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--golden", type=Path, default=ROOT / "golden.jsonl")
    parser.add_argument("--out", type=Path, default=ROOT / "results.csv")
    parser.add_argument("--bots", nargs="+", default=list(BOTS))
    parser.add_argument("--timeout", type=float, default=90.0)
    args = parser.parse_args()

    questions = load_golden(args.golden)
    rows: list[dict] = []

    with httpx.Client(base_url=args.base_url, timeout=args.timeout) as client:
        health = client.get("/api/health")
        print("health:", health.status_code, health.text[:200])

        for item in questions:
            qid = item["id"]
            question = item["question"]
            for bot in args.bots:
                t0 = time.perf_counter()
                try:
                    res = client.post("/api/chat", json={"question": question, "bot": bot})
                    elapsed = (time.perf_counter() - t0) * 1000
                    if res.status_code != 200:
                        rows.append(
                            {
                                "id": qid,
                                "bot": bot,
                                "question": question,
                                "status": res.status_code,
                                "grounded": "",
                                "intent": "",
                                "latency_ms": round(elapsed, 1),
                                "answer_chars": 0,
                                "citations": 0,
                                "answer_preview": res.text[:180],
                            }
                        )
                        print(f"FAIL {qid} {bot} {res.status_code}")
                        continue
                    data = res.json()
                    answer = data.get("answer") or ""
                    rows.append(
                        {
                            "id": qid,
                            "bot": bot,
                            "question": question,
                            "status": 200,
                            "grounded": data.get("grounded"),
                            "intent": data.get("intent"),
                            "latency_ms": round(elapsed, 1),
                            "answer_chars": len(answer),
                            "citations": len(data.get("citations") or []),
                            "answer_preview": answer.replace("\n", " ")[:180],
                        }
                    )
                    print(
                        f"ok {qid} {bot} grounded={data.get('grounded')} "
                        f"{elapsed:.0f}ms citations={len(data.get('citations') or [])}"
                    )
                except Exception as exc:  # noqa: BLE001
                    elapsed = (time.perf_counter() - t0) * 1000
                    rows.append(
                        {
                            "id": qid,
                            "bot": bot,
                            "question": question,
                            "status": "error",
                            "grounded": "",
                            "intent": "",
                            "latency_ms": round(elapsed, 1),
                            "answer_chars": 0,
                            "citations": 0,
                            "answer_preview": str(exc)[:180],
                        }
                    )
                    print(f"ERR {qid} {bot} {exc}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "bot",
                "question",
                "status",
                "grounded",
                "intent",
                "latency_ms",
                "answer_chars",
                "citations",
                "answer_preview",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {args.out} ({len(rows)} rows)")
    for bot in args.bots:
        subset = [r for r in rows if r["bot"] == bot and r["status"] == 200]
        if not subset:
            print(f"{bot}: no successful rows")
            continue
        grounded = sum(1 for r in subset if r["grounded"] is True)
        avg_ms = sum(float(r["latency_ms"]) for r in subset) / len(subset)
        print(f"{bot}: {grounded}/{len(subset)} grounded, avg {avg_ms:.0f}ms")


if __name__ == "__main__":
    main()
