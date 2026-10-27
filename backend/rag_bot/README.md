# Athlyte RAG Bot (backend)

Docs-only RAG API for Athlyte Search platform Q&A.

**Layout:** `BOT/backend/` holds `docs/`, `.env`, and `rag_bot/`.

**Stack:** FastAPI · Gemini (`GOOGLE_API_KEY`) · local `BAAI/bge-base-en-v1.5` via `fastembed` (ONNX) · Qdrant (Docker)

## Setup

```bash
cd backend/rag_bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Put `GOOGLE_API_KEY` in `backend/.env` (or `rag_bot/.env`). See `.env.example`.

## Start Qdrant (Docker)

Container name: **`rag_bot_qdrant`**

```bash
cd backend/rag_bot
docker compose up -d
curl http://localhost:6333/readyz
```

Default app config uses `QDRANT_URL=http://localhost:6333`.

To use local on-disk Qdrant instead (no Docker), set `QDRANT_URL=` empty in `.env`.

## Ingest docs

Uses Gemini model `gemini-3.5-flash` by default (override with `GEMINI_MODEL`).

First run downloads the BGE ONNX model via fastembed.

```bash
cd backend/rag_bot
source .venv/bin/activate
python scripts/ingest_docs.py
```

## Run API

```bash
cd backend/rag_bot
source .venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Swagger: http://localhost:8000/docs
- Health: `GET /api/health`
- Chat: `POST /api/chat`

### Example

```bash
curl -s http://localhost:8000/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"question":"What is rushing yards?"}'

curl -s http://localhost:8000/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"question":"How to frame query using rushing yards"}'
```

## Intents

| Question shape | Intent | Behavior |
|---|---|---|
| What is X? | `definition` | Definition from Data Centre / Stat Search Guide |
| How to frame query using X | `query_framing` | One example per Athlyte query type |
| Other platform questions | `general` | Grounded answer from retrieved docs |

UI is deferred; use Swagger or curl for now.
