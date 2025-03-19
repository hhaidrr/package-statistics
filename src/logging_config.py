import logging
import sys
from typing import Final
import os

__all__ = ["initialize_logger"]


_ENV_LOG_LEVEL = os.getenv("LOG_LEVEL")
_ENV_LOG_LEVEL = (
    logging.getLevelNamesMapping()[_ENV_LOG_LEVEL.upper()] if _ENV_LOG_LEVEL else None
)

_DEFAULT_LOG_LEVEL: Final[int] = logging.INFO
_DEFAULT_LOG_FORMAT: Final[str] = "%(levelname)-5s [%(name)s] %(message)s"

_LOG_LEVEL: Final[int] = _ENV_LOG_LEVEL or _DEFAULT_LOG_LEVEL


class _CustomFormatter(logging.Formatter):
    def format(self, record):
        is_a_submodule: bool = "." in record.name
        if type(record.name) is str and is_a_submodule:
            record.name = ".".join(record.name.split(".")[-2:])
        return super().format(record)


def _clear_root_logger_handlers() -> None:
    root_logger = logging.getLogger()
    root_logger.handlers = []


def initialize_logger(root_module: str) -> None:
    """Initialize the application logger

    This should be called from the module you consider to be the root of your application for all other modules.

    e.g. src/project_name/__init__.py

    :param root_module: The name of your project root module.

    Invoke from the root module e.g.
    >>> initialize_logger(__name__)
    """

    _clear_root_logger_handlers()

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(_CustomFormatter(_DEFAULT_LOG_FORMAT))

    logger = logging.getLogger(root_module)
    logger.propagate = False
    logger.addHandler(handler)
    logger.setLevel(_LOG_LEVEL)
    logger.info(
        f"{logger.name} logger setup complete with level {logging.getLevelName(_LOG_LEVEL)}."
    )
