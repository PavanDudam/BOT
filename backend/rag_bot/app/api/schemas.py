from typing import Literal

from pydantic import BaseModel, Field

BotName = Literal["rag", "okf", "mixed"]


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)
    bot: BotName = "rag"


class Citation(BaseModel):
    source: str
    section: str
    snippet: str
    system: str | None = None


class ChatResponse(BaseModel):
    answer: str
    intent: str
    citations: list[Citation]
    grounded: bool
    bot: BotName = "rag"
    latency_ms: float | None = None
    prompt_tokens: int | None = None
    output_tokens: int | None = None
    total_tokens: int | None = None


class HealthResponse(BaseModel):
    status: str
    qdrant: str
    collection: str
    embeddings: str = "unknown"
    okf_bundle: str = "unknown"
