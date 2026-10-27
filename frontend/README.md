# Athlyte RAG Frontend

Simple React chat UI for testing the Athlyte docs RAG backend.

## Run

Backend must be up on port 8000 first.

```bash
# terminal 1 — API
cd backend/rag_bot
source .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000

# terminal 2 — UI
cd frontend
npm install
npm run dev
```

Open http://localhost:5173

Vite proxies `/api` → `http://127.0.0.1:8000`.
