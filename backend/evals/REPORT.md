# Athlyte Multi-Bot Eval Report

**Date:** 2026-10-27  
**Questions:** 50 (stratified: definition, query framing, platform, navigation, features, export, search, basketball, edge)  
**Pipeline:**
1. Retrieve-only contexts via `rag` / `okf` / `mixed` (local Qdrant + OKF bundle; no Gemini)
2. **Gold answers:** Grok 4.6 (Cursor) grounded on oracle/mixed context + manual repair for 5 false refusals from weak retrieval
3. **Predictions:** Composer 2.5 from each bot's retrieved context only (avoids Google AI Studio 5 RPM limit)
4. **Judge:** Grok 4.7 — correctness / groundedness / completeness / overall (1–5); pass if overall ≥ 4

## Headline results

| Bot | Pass rate | Avg overall | Avg correct | Avg grounded | Avg complete | Avg retrieve ms | p50 retrieve ms |
|---|---:|---:|---:|---:|---:|---:|---:|
| **rag** | **90%** | **4.52** | 4.78 | 4.84 | 4.54 | 102 | 55 |
| okf | 64% | 3.36 | 3.60 | 4.76 | 3.28 | 56 | 47 |
| mixed | 88% | 4.30 | 4.56 | 4.88 | 4.30 | 114 | 108 |

**Solo wins** (strictly highest overall on a question): rag 8 · okf 3 · mixed 4 · ties 35

## Token / cost estimates (chars÷4; Cursor usage, not Google)

These are **estimates** for context fed to Composer + answer length (no Gemini billing used for predictions).

| Bot | Est. total context tokens | Est. total answer tokens | Avg context tok/q | Avg answer tok/q | Wrong refusals |
|---|---:|---:|---:|---:|---:|
| rag | 41,708 | 3,208 | 834 | 64 | 1 |
| okf | 158,820 | 2,428 | 3176 | 49 | 15 |
| mixed | 131,110 | 2,702 | 2622 | 54 | 5 |

Also used Cursor for: gold (Grok 4.6 × 50) + judge (Grok 4.7 × 150).

## Pass rate by category

| Category | rag | okf | mixed |
|---|---:|---:|---:|
| basketball | 50% (n=2) | 50% (n=2) | 100% (n=2) |
| definition | 100% (n=10) | 100% (n=10) | 100% (n=10) |
| edge | 100% (n=3) | 100% (n=3) | 100% (n=3) |
| export | 100% (n=2) | 100% (n=2) | 100% (n=2) |
| features | 80% (n=5) | 40% (n=5) | 60% (n=5) |
| navigation | 80% (n=5) | 80% (n=5) | 80% (n=5) |
| platform | 100% (n=6) | 17% (n=6) | 83% (n=6) |
| query_framing | 90% (n=10) | 50% (n=10) | 80% (n=10) |
| search | 86% (n=7) | 57% (n=7) | 100% (n=7) |

## Findings

1. **RAG wins this eval** on pass rate (90%) and average overall (4.52). Dense retrieval over chunked product docs covers definitions *and* guide/prose questions well.
2. **OKF is fastest to retrieve** (~56 ms avg) and highly grounded when it answers, but **over-refuses** (15 wrong refusals) when BM25+graph misses guide concepts (Ask Athlyte, data ranges, query-type diffs, filters). Bundle authoring/linking needs work for non-stat questions.
3. **Mixed is close to RAG** (88% pass) but slightly worse — RRF sometimes inherits OKF misses / noise and does not always beat dense-only.
4. **Edge questions** (weather, Super Bowl) all bots correctly refuse — good safety.
5. This measures **retrieval + Composer generation**, not production Gemini. Still valid for comparing retrieval strategies under a fixed generator.

## Recommended next steps

- Enrich OKF bundle: more Guide concepts + stronger links from stats → query types → platform guides
- Add hybrid BM25 to RAG path for exact names
- Re-run after OKF improvements; expect mixed to pull ahead if OKF recall rises without hurting precision

## Artifacts

| File | Description |
|---|---|
| `questions_50.jsonl` | 50 eval questions |
| `contexts.jsonl` | Retrieved contexts + retrieve latency per bot |
| `gold.jsonl` | Grok 4.6 gold answers |
| `predictions.jsonl` | Composer predictions (150) |
| `judgments.jsonl` | Grok 4.7 scores (150) |
| `results_full.csv` | Flat joined metrics |
| `summary.json` | Machine-readable summary |

## Sample failures

### rag
- q11 (query_framing): Frames rushing yards as Rushing Yards Gained instead of the net-rushing-yards default, ter
- q29 (navigation): Gets the no-requery behavior and Streaks exception, but lists only Name, Date, Period Type
- q34 (features): Refuses even though Team Streaks is consecutive-game team performance on the Team Dashboar
- q38 (search): Lists some sidebar filters and the streaks exception, but mis-scopes Position and Classes 
- q45 (basketball): Names defensive rebound percentage among other defense stats but omits the definition, sea
### okf
- q12 (query_framing): Wrongly refuses a streak question the docs answer.
- q13 (query_framing): Gives the last-time definition and two examples but omits the sport-specific period lists.
- q14 (query_framing): Gives other single-stat record examples and misses the gold examples and period rules.
- q15 (query_framing): Wrongly refuses a complex passing-yards question the docs answer.
- q19 (query_framing): Wrongly refuses a basic-versus-complex question the docs answer.
### mixed
- q15 (query_framing): Wrongly refuses a complex passing-yards question the docs answer.
- q19 (query_framing): Wrongly refuses a basic-versus-complex question the docs answer.
- q23 (platform): Wrongly refuses the Men's Football standard data range given in the gold answer.
- q30 (navigation): Wrongly refuses the Ask Athlyte definition given in the gold answer.
- q33 (features): Names the feature and query types, but omits each query type's chart rules.
