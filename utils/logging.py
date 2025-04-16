# utils/logger.py

import logging
import sys

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
