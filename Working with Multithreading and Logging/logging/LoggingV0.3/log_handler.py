import logging

class FileLogHandler(logging.FileHandler):
    def __init__(self, filename):
        super().__init__(filename, encoding="utf-8")

    def emit(self, record):
        record.msg = f"logging file: {record.msg}"
        super().emit(record)
        