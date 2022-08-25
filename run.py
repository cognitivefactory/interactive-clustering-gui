"""Script used to run the program."""


# ==============================================================================
# IMPORT PYTHON DEPENDENCIES
# ==============================================================================

import logging
import os
import re
import sys
from typing import Tuple

from loguru import logger
from uvicorn import Config, Server
from uvicorn.supervisors import ChangeReload

# ==============================================================================
# DEFINE GLOBAL VARIABLES
# ==============================================================================


FALSE_VALUES: Tuple[str, str, str, str, str] = ("", "0", "no", "off", "false")
LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "debug").upper())
JSON_LOGS: bool = os.environ.get("JSON_LOGS", "no").lower() not in FALSE_VALUES


# ==============================================================================
# INTERCEPT LOGS
# ==============================================================================
class InterceptHandler(logging.Handler):
    """Intercept logs."""

    _probe_log = re.compile("GET /(?:alive|ready)")

    def emit(self, record: logging.LogRecord) -> None:
        """
        Re-emit the intercepted log with Loguru.

        Args:
            record: The log record.
        """

        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno  # type: ignore

        # Find caller from where originated the logged message.
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = frame.f_back  # type: ignore[assignment]
            depth += 1

        message = record.getMessage()
        if level != "INFO" or not self._probe_log.search(message):
            logger.opt(depth=depth, exception=record.exc_info).log(level, message)


# ==============================================================================
# CONFIGURE LOGGING
# ==============================================================================
def setup_logging(serialize: bool = False) -> None:
    """
    Configure logging.

    Args:
        serialize (bool, optional): Whether to serialize logs to JSON. Defaults to `False`.
    """

    # Intercept everything at the root logger.
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(LOG_LEVEL)

    # Remove every other logger's handlers and propagate to root logger.
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    # Configure loguru.
    logger.configure(handlers=[{"sink": sys.stdout, "serialize": serialize, "level": LOG_LEVEL}])


# ==============================================================================
# RECONFIGURE UVICORN LOGGING
# ==============================================================================
class FixedLoggingConfig(Config):
    """
    Subclass of uvicorn config that re-configures logging.
    """

    serialize_logs = False

    def configure_logging(self) -> None:  # noqa: D102
        super().configure_logging()
        setup_logging(self.serialize_logs)


# ==============================================================================
# RUN APPLICATION
# ==============================================================================
def run(
    host: str = "127.0.0.1", port: int = 8080, log_level=LOG_LEVEL, json_logs: bool = JSON_LOGS, reload: bool = False
):  # noqa: S104
    """
    Run the Uvicorn server.

    Arguments:
        host (str, optional): The host to bind. Defaults to `"127.0.0.1"`.
        port (int, optional): The port to use. Defaults to `8080`.
        log_level: The log level.
        json_logs (bool, optional): Whether to serialize logs in JSON.
        reload (bool, optional): Whether to enable live-reload. Defaults to `False`.
    """
    FixedLoggingConfig.serialize_logs = json_logs
    config = FixedLoggingConfig(
        "cognitivefactory.interactive_clustering_gui.app:app",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
    )
    server = Server(config)
    setup_logging(serialize=json_logs)

    if reload:
        sock = config.bind_socket()
        ChangeReload(config, target=server.run, sockets=[sock]).run()
    else:
        server.run()
