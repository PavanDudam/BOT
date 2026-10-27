from contextlib import asynccontextmanager
import logging
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_chat import router as chat_router
from app.config import get_settings
from app.logging_utils import get_logger
from app.rag.embeddings import get_embedder

# Keep uvicorn's logger for lifespan banners; use app logger for timings.
uvicorn_logger = logging.getLogger("uvicorn.error")
logger = get_logger("athlyte.startup")


@asynccontextmanager
async def lifespan(_app: FastAPI):
    settings = get_settings()
    logger.info("startup.begin | embedding_model=%s gemini_model=%s", settings.embedding_model, settings.gemini_model)
    t0 = time.perf_counter()
    uvicorn_logger.info("Loading embedding model %s …", settings.embedding_model)
    get_embedder()
    load_ms = (time.perf_counter() - t0) * 1000
    uvicorn_logger.info("Embedding model ready.")
    logger.info("startup.embedder_ready | %.1fms", load_ms)
    yield
    logger.info("shutdown")


app = FastAPI(
    title="Athlyte RAG Bot",
    description="Docs-only RAG API for Athlyte Search platform Q&A",
    version="0.1.0",
    lifespan=lifespan,
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
