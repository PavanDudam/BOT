from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.api.schemas import ChatRequest, ChatResponse, HealthResponse
from app.config import get_settings
from app.rag.embeddings import get_embedder
from app.rag.generator import answer_question
from app.rag.ingest import get_qdrant

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    settings = get_settings()
    mode = settings.qdrant_url or f"local:{settings.qdrant_path}"

    try:
        get_embedder()
        embeddings_status = f"ready ({settings.embedding_model})"
    except Exception as exc:  # noqa: BLE001
        embeddings_status = f"error: {exc}"

    try:
        client = get_qdrant()
        exists = client.collection_exists(settings.qdrant_collection)
        qdrant_status = f"ok ({mode})" if exists else f"missing_collection ({mode})"
    except Exception as exc:  # noqa: BLE001
        return HealthResponse(
            status="degraded",
            qdrant=f"error: {exc}",
            collection=settings.qdrant_collection,
            embeddings=embeddings_status,
        )

    ready = exists and embeddings_status.startswith("ready")
    return HealthResponse(
        status="ok" if ready else "degraded",
        qdrant=qdrant_status,
        collection=settings.qdrant_collection,
        embeddings=embeddings_status,
    )


@router.post("/chat", response_model=ChatResponse)
def chat(body: ChatRequest) -> ChatResponse:
    question = body.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="question is required")
    try:
        return answer_question(question)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"chat failed: {exc}") from exc
