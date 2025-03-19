import logging
import sys
from typing import ClassVar, Final
import os

__all__ = ["initialize_logger"]


_ENV_LOG_LEVEL_NAME: str | None = os.getenv("LOG_LEVEL")
_ENV_LOG_LEVEL: int | None = (
    logging.getLevelNamesMapping()[_ENV_LOG_LEVEL_NAME.upper()]
    if _ENV_LOG_LEVEL_NAME
    else None
)

_DEFAULT_LOG_LEVEL: Final[int] = logging.INFO
_DEFAULT_LOG_FORMAT: Final[str] = "%(levelname)-5s [%(name)s] %(message)s"

_LOG_LEVEL: Final[int] = _ENV_LOG_LEVEL or _DEFAULT_LOG_LEVEL


class _CustomFormatter(logging.Formatter):
    _SUBMODULE_PATH_DELIMITER: ClassVar[str] = "."
    _SUBMODULE_PATH_LIMIT: ClassVar[int] = 3

    @classmethod
    def _truncate_submodule_path(cls, path: str, limit: int) -> str:
        path = cls._SUBMODULE_PATH_DELIMITER.join(
            path.split(cls._SUBMODULE_PATH_DELIMITER)[-limit:]
        )
        return path

    def format(self, record):
        is_submodule: bool = self.__class__._SUBMODULE_PATH_DELIMITER in record.name
        if type(record.name) is str and is_submodule:
            record.name = self.__class__._truncate_submodule_path(
                record.name, self._SUBMODULE_PATH_LIMIT
            )
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
