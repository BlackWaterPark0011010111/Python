import logging

"""В этом  случае CustomMessage с методом __str__() возвращаем строку при попытке передать объект в лог."""

class CustomMessage:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Сообщение: {self.value}"

# Создаем объект с произвольными данными
message = CustomMessage(42)

# Логируем сообщение
logging.info(message)