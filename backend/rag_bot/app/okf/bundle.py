from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from okf import Bundle

from app.config import get_settings
from app.logging_utils import get_logger

logger = get_logger("athlyte.okf")


@lru_cache
def get_bundle() -> Bundle:
    settings = get_settings()
    path = Path(settings.okf_bundle_path)
    if not path.is_dir():
        raise FileNotFoundError(
            f"OKF bundle not found at {path}. Run: python scripts/build_okf_bundle.py"
        )
    bundle = Bundle.load(path)
    logger.info("okf.bundle_loaded | path=%s docs=%s", path, len(bundle.docs))
    return bundle


def bundle_status() -> tuple[bool, str]:
    settings = get_settings()
    path = Path(settings.okf_bundle_path)
    if not path.is_dir():
        return False, f"missing ({path})"
    try:
        bundle = get_bundle()
        return True, f"ok ({len(bundle.docs)} docs)"
    except Exception as exc:  # noqa: BLE001
        return False, f"error: {exc}"
