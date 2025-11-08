from for_connection import ServerConnection
from logging import Logger
from logger_conf import AppLogger





if __name__==  "__main__":
    logger = AppLogger().get_logger()
    logger.info("Тестовое сообщение: логгер работает!")
    connection = ServerConnection()
    connection.connect()

