from __future__ import annotations

import uuid
from functools import lru_cache
from pathlib import Path

from qdrant_client import QdrantClient
from qdrant_client.http import models as qm

from app.config import Settings, get_settings
from app.rag.chunking import Chunk, chunk_docs_dir
from app.rag.embeddings import embed_texts


@lru_cache
def get_qdrant() -> QdrantClient:
    settings = get_settings()
    if settings.qdrant_url:
        return QdrantClient(url=settings.qdrant_url, check_compatibility=False)
    settings.qdrant_path.mkdir(parents=True, exist_ok=True)
    return QdrantClient(path=str(settings.qdrant_path), check_compatibility=False)


def ensure_collection(client: QdrantClient, settings: Settings) -> None:
    name = settings.qdrant_collection
    if client.collection_exists(name):
        client.delete_collection(name)
    client.create_collection(
        collection_name=name,
        vectors_config=qm.VectorParams(
            size=settings.embedding_dim,
            distance=qm.Distance.COSINE,
        ),
    )


def _payload(chunk: Chunk) -> dict:
    return {
        "text": chunk.text,
        "source_file": chunk.source_file,
        "section_title": chunk.section_title,
        "chunk_kind": chunk.chunk_kind,
        "stat_name": chunk.stat_name or "",
        "chunk_index": chunk.chunk_index,
    }


def ingest_docs(docs_path: Path | None = None, batch_size: int = 64) -> int:
    settings = get_settings()
    docs_path = docs_path or settings.docs_path
    chunks = chunk_docs_dir(docs_path)
    if not chunks:
        raise RuntimeError(f"No markdown chunks found under {docs_path}")

    client = get_qdrant()
    ensure_collection(client, settings)

    total = 0
    for start in range(0, len(chunks), batch_size):
        batch = chunks[start : start + batch_size]
        vectors = embed_texts([c.text for c in batch], is_query=False)
        points = [
            qm.PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload=_payload(chunk),
            )
            for chunk, vector in zip(batch, vectors)
        ]
        client.upsert(collection_name=settings.qdrant_collection, points=points)
        total += len(points)
    return total
