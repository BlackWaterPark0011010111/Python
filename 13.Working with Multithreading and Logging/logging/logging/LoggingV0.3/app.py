import logging

from log_config import setup_Log
from log_handler import FileLogHandler
from logger_utils import CustomFilter

logger = setup_Log()

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
logger.exception("exception message")
adapter = logging.LoggerAdapter(logger, {"user": "Admin"})
adapter.info("sistem starting ")
logger.addFilter(CustomFilter())
logger.warning("This warning not gonna be recorded")
