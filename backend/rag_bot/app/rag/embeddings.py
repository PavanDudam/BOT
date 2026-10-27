from __future__ import annotations

from functools import lru_cache

from fastembed import TextEmbedding

from app.config import get_settings
from app.logging_utils import get_logger, timed

logger = get_logger("athlyte.embeddings")


@lru_cache
def get_embedder() -> TextEmbedding:
    settings = get_settings()
    with timed(logger, "embedder.load", model=settings.embedding_model):
        return TextEmbedding(model_name=settings.embedding_model)


def embed_texts(texts: list[str], *, is_query: bool = False) -> list[list[float]]:
    """Embed documents or queries with BGE via fastembed (ONNX, no full torch)."""
    model = get_embedder()
    kind = "query" if is_query else "passage"
    with timed(logger, "embed.encode", kind=kind, count=len(texts)):
        if is_query:
            vectors = list(model.query_embed(texts))
        else:
            vectors = list(model.passage_embed(texts))
    return [v.tolist() for v in vectors]


def embed_query(text: str) -> list[float]:
    return embed_texts([text], is_query=True)[0]
