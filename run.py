"""Script used to run the program."""

import logging
import os
import re
import sys

from loguru import logger
from uvicorn import Config, Server
from uvicorn.supervisors import ChangeReload

FALSE_VALUES = ("", "0", "no", "off", "false")
LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "debug").upper())
JSON_LOGS = os.environ.get("JSON_LOGS", "no").lower() not in FALSE_VALUES


class InterceptHandler(logging.Handler):
    """Intercept logs."""

    _probe_log = re.compile("GET /(?:alive|ready)")

    def emit(self, record: logging.LogRecord) -> None:
        """
        Re-emit the intercepted log with Loguru.

        Arguments:
            record: The log record.
        """
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = frame.f_back  # type: ignore[assignment]
            depth += 1

        message = record.getMessage()
        if level != "INFO" or not self._probe_log.search(message):
            logger.opt(depth=depth, exception=record.exc_info).log(level, message)


def setup_logging(serialize=False):
    """Configure logging.

    Arguments:
        serialize: Whether to serialize logs to JSON.
    """
    # intercept everything at the root logger
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(LOG_LEVEL)

    # remove every other logger's handlers
    # and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    # configure loguru
    logger.configure(handlers=[{"sink": sys.stdout, "serialize": serialize, "level": LOG_LEVEL}])


class FixedLoggingConfig(Config):
    """Subclass of uvicorn config that re-configures logging."""

    serialize_logs = False

    def configure_logging(self) -> None:  # noqa: D102
        super().configure_logging()
        setup_logging(self.serialize_logs)


def run(host="0.0.0.0", port=8080, log_level=LOG_LEVEL, json_logs=JSON_LOGS, reload=False):  # noqa: S104
    """Run the Uvicorn server.

    Arguments:
        host: The host to bind.
        port: The port to use.
        log_level: The log level.
        json_logs: Whether to serialize logs in JSON.
        reload: Whether to enable live-reload.
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


if __name__ == "__main__":
    run()
