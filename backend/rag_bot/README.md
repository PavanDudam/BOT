# Athlyte Docs Bot (backend)

Docs-only Q&A for Athlyte Search with **three retrieval strategies** in one API:

| `bot` | Retrieval |
|---|---|
| `rag` (default) | Dense vectors in Qdrant (BGE + heuristic boosts) |
| `okf` | OKF bundle BM25 + 1-hop link graph (`okf-retrieve`) |
| `mixed` | RRF fusion of RAG + OKF |

**Layout:** `BOT/backend/` holds `docs/`, generated `okf_bundle/`, `.env`, `rag_bot/`, and `evals/`.

**Stack:** FastAPI · Gemini · local `BAAI/bge-base-en-v1.5` (fastembed) · Qdrant · OKF

## Setup

```bash
cd backend/rag_bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Put `GOOGLE_API_KEY` in `backend/.env` (or `rag_bot/.env`). See `.env.example`.

## Start Qdrant (Docker)

```bash
cd backend/rag_bot
docker compose up -d
curl http://localhost:6333/readyz
```

## Build indexes

```bash
cd backend/rag_bot
source .venv/bin/activate
python scripts/ingest_docs.py      # Qdrant for rag/mixed
python scripts/build_okf_bundle.py # OKF markdown concepts for okf/mixed
```

## Run API (single port)

```bash
cd backend/rag_bot
source .venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Swagger: http://localhost:8000/docs
- Health: `GET /api/health` (qdrant + embeddings + okf_bundle)
- Chat: `POST /api/chat` with `{"question":"...","bot":"rag|okf|mixed"}`
- Stream: `POST /api/chat/stream` (SSE)

### Examples

```bash
curl -s http://localhost:8000/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"question":"What is rushing yards?","bot":"rag"}'

curl -s http://localhost:8000/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"question":"What is rushing yards?","bot":"okf"}'

curl -s http://localhost:8000/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"question":"How to frame query using rushing yards","bot":"mixed"}'
```

## Frontend

From `frontend/`: `npm install && npm run dev` → http://localhost:5173  
Use the **RAG | OKF | Mixed** switcher; Vite proxies `/api` → `:8000`.

## Evals

With the API running:

```bash
cd backend/rag_bot && source .venv/bin/activate
python ../evals/run_evals.py --base-url http://localhost:8000
```

Writes `backend/evals/results.csv` and prints grounded rate / latency per bot.

## Intents

| Question shape | Intent | Behavior |
|---|---|---|
| What is X? | `definition` | Prefer stat definitions |
| How to frame query using X | `query_framing` | Query-type examples |
| Other platform questions | `general` | Grounded answer from retrieved docs |
