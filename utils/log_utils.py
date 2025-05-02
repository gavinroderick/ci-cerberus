import logging
import sys


def setup_logger(verbosity: str = "INFO") -> None:
    level = logging.getLevelName(verbosity.upper())

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
