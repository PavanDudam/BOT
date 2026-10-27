from __future__ import annotations

from functools import lru_cache

from fastembed import TextEmbedding

from app.config import get_settings


@lru_cache
def get_embedder() -> TextEmbedding:
    settings = get_settings()
    return TextEmbedding(model_name=settings.embedding_model)


def embed_texts(texts: list[str], *, is_query: bool = False) -> list[list[float]]:
    """Embed documents or queries with BGE via fastembed (ONNX, no full torch)."""
    model = get_embedder()
    if is_query:
        vectors = list(model.query_embed(texts))
    else:
        vectors = list(model.passage_embed(texts))
    return [v.tolist() for v in vectors]


def embed_query(text: str) -> list[float]:
    return embed_texts([text], is_query=True)[0]
