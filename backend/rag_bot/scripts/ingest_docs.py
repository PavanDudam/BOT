#!/usr/bin/env python3
"""Rebuild the Qdrant collection from ../docs markdown files."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.config import get_settings
from app.rag.ingest import ingest_docs


def main() -> None:
    settings = get_settings()
    print(f"Docs path: {settings.docs_path}")
    store = settings.qdrant_url or f"local:{settings.qdrant_path}"
    print(f"Qdrant: {store} / {settings.qdrant_collection}")
    print(f"Embedding model: {settings.embedding_model}")
    count = ingest_docs()
    print(f"Ingested {count} chunks.")


if __name__ == "__main__":
    main()
