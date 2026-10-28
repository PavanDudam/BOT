from contextlib import asynccontextmanager
import logging
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_chat import router as chat_router
from app.config import get_settings
from app.logging_utils import get_logger
from app.okf.bundle import bundle_status, get_bundle
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

    ok, status = bundle_status()
    if ok:
        t1 = time.perf_counter()
        get_bundle()
        logger.info("startup.okf_ready | %.1fms | %s", (time.perf_counter() - t1) * 1000, status)
        uvicorn_logger.info("OKF bundle ready: %s", status)
    else:
        logger.warning("startup.okf_missing | %s", status)
        uvicorn_logger.warning("OKF bundle not loaded: %s (okf/mixed bots degraded)", status)
    yield
    logger.info("shutdown")


app = FastAPI(
    title="Athlyte Docs Bot",
    description="Athlyte Search docs Q&A with rag | okf | mixed retrieval strategies",
    version="0.2.0",
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
        "service": "athlyte-docs-bot",
        "docs": "/docs",
        "health": "/api/health",
        "chat": "POST /api/chat",
        "bots": ["rag", "okf", "mixed"],
    }
