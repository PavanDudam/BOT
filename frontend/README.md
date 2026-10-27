# Athlyte Docs Frontend

React chat UI with a **RAG | OKF | Mixed** retrieval switcher (single backend on `:8000`).

## Run

Build indexes and start the API first (see `backend/rag_bot/README.md`):

```bash
# terminal 1 — API
cd backend/rag_bot
source .venv/bin/activate
python scripts/ingest_docs.py
python scripts/build_okf_bundle.py
uvicorn app.main:app --host 0.0.0.0 --port 8000

# terminal 2 — UI
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — pick a bot in the header, then ask. Each answer is badged with the strategy used.

Vite proxies `/api` → `http://127.0.0.1:8000`.
