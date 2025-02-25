import socket
from logger_conf import AppLogger
from errors import handle_error
from settings import HOST, PORT


class ServerConnection:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.logger = AppLogger().get_logger()  # Исправленный импорт

    def connect(self):
        self.logger.info(f"Пытаемся подключиться к серверу {self.host}:{self.port}")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self.host, self.port))
            self.logger.info("Успешное подключение к серверу!")
            sock.close()
        except socket.timeout:
            self.logger.error(handle_error("timeout"))
        except socket.gaierror:
            self.logger.error(handle_error("gaierror"))
        except ConnectionRefusedError:
            self.logger.error(handle_error("refused"))
        except Exception as e:
            self.logger.error(f"{handle_error('unknown')}\nДополнительная информация: {e}")
