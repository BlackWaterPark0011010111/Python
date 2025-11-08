import logging
from logging import StreamHandler, FileHandler, Formatter

def setup_Log():
    logger = logging.getLogger("MyLoggger")
    logger.setLevel(logging.DEBUG)

    log_formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s' )

    console_handler = StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(log_formatter)

    file_handler = FileHandler("app.log", encoding="utf-8")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(log_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    if not logger.hasHandlers():
        print("Logger has no handlers()у логера нет разработчиков ")
    return logger