import logging
from pathlib import Path


def get_logger(name="autodevops"):
    """Create and return the application logger."""

    log_directory = Path("logs")
    log_directory.mkdir(parents=True, exist_ok=True)

    log_file = log_directory / "autodevops.log"

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
