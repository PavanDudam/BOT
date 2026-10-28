from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

RAG_BOT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = RAG_BOT_ROOT.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(REPO_ROOT / ".env", RAG_BOT_ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    google_api_key: str = ""
    gemini_model: str = "gemini-3.5-flash-lite"
    gemini_temperature: float = 0.0
    embedding_model: str = "BAAI/bge-base-en-v1.5"
    # Default: Docker Qdrant. Set empty to fall back to local embedded store at qdrant_path.
    qdrant_url: str = "http://localhost:6333"
    qdrant_path: Path = RAG_BOT_ROOT / "data" / "qdrant"
    qdrant_collection: str = "athlyte_docs"
    docs_path: Path = REPO_ROOT / "docs"
    okf_bundle_path: Path = REPO_ROOT / "okf_bundle"
    top_k: int = 8
    score_threshold: float = 0.35
    embedding_dim: int = 768
    okf_expand_hops: int = 1
    rrf_k: int = 60


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    if not settings.docs_path.is_absolute():
        settings.docs_path = (RAG_BOT_ROOT / settings.docs_path).resolve()
    if not settings.qdrant_path.is_absolute():
        settings.qdrant_path = (RAG_BOT_ROOT / settings.qdrant_path).resolve()
    if not settings.okf_bundle_path.is_absolute():
        settings.okf_bundle_path = (RAG_BOT_ROOT / settings.okf_bundle_path).resolve()
    return settings
