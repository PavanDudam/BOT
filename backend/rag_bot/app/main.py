from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_chat import router as chat_router

app = FastAPI(
    title="Athlyte RAG Bot",
    description="Docs-only RAG API for Athlyte Search platform Q&A",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")


@app.get("/")
def root() -> dict:
    return {
        "service": "athlyte-rag-bot",
        "docs": "/docs",
        "health": "/api/health",
        "chat": "POST /api/chat",
    }
