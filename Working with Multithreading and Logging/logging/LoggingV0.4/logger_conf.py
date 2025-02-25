import logging
import os
from logging.handlers import TimedRotatingFileHandler
from colorama import Fore, Style, init

init()

LOG_COLORS = {
    logging.DEBUG: Fore.BLUE,
    logging.INFO: Fore.GREEN,
    logging.WARNING: Fore.YELLOW,
    logging.ERROR: Fore.RED,
    logging.CRITICAL: Fore.MAGENTA,

}
class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_color = LOG_COLORS.get(record.levelno, Fore.WHITE)
        log_smg = super().format(record)
        return f"{log_color}{log_smg}{Style.RESET_ALL}"
    
class AppLogger:  # Было Logger, теперь AppLogger
    def __init__(self, log_dir="logs", log_file="connection.log", level=logging.DEBUG):
        os.makedirs(log_dir, exist_ok=True)
        self.logger = logging.getLogger("ConnectionLogger")
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Запись логов в файл
        file_handler = TimedRotatingFileHandler(os.path.join(log_dir, log_file),
                                                when="midnight", interval=1,
                                                backupCount=7, encoding="utf-8")
        file_handler.setFormatter(log_format)
        self.logger.addHandler(file_handler)

        # Логирование только ошибок
        error_handler = logging.FileHandler(os.path.join(log_dir, "errors.log"), encoding="utf-8")
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(log_format)
        self.logger.addHandler(error_handler)

        # Вывод в консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(CustomFormatter("%(asctime)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

    