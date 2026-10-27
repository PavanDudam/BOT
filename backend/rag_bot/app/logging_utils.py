from __future__ import annotations

import logging
import time
from contextlib import contextmanager
from typing import Iterator


def get_logger(name: str = "athlyte.rag") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                datefmt="%H:%M:%S",
            )
        )
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
    return logger


@contextmanager
def timed(logger: logging.Logger, label: str, **fields: object) -> Iterator[dict[str, float]]:
    """Log elapsed ms for a block. Yields a dict that receives `ms` after exit."""
    bag: dict[str, float] = {}
    start = time.perf_counter()
    try:
        yield bag
    finally:
        ms = (time.perf_counter() - start) * 1000
        bag["ms"] = ms
        extra = " ".join(f"{k}={v}" for k, v in fields.items())
        suffix = f" | {extra}" if extra else ""
        logger.info("%s | %.1fms%s", label, ms, suffix)
