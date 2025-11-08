import logging  # Импортируем библиотеку для логирования
import smtplib  # Библиотека для отправки email
from email.mime.text import MIMEText  # Форматирование email сообщения
import sqlite3  # Работа с базой данных SQLite
import os  # Для работы с переменными окружения

# Создаем свой обработчик логов
class CustomHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)  # Форматируем сообщение лога
        print(f'Пользовательский обработчик: {log_entry}')  # Выводим в консоль
        
        # Если уровень ошибки высокий, отправляем email и сохраняем в базу
        if record.levelname == 'ERROR' or record.levelname == 'CRITICAL':
            self.send_email_notification(log_entry)
            self.save_to_database(log_entry)

    def send_email_notification(self, log_entry):
        sender_email = "your_email@example.com"  # Почта отправителя
        receiver_email = "receiver_email@example.com"  # Почта получателя
        password = os.getenv("EMAIL_PASSWORD")  # Пароль берем из переменных окружения

        subject = "Critical Error Notification"  # Тема письма
        body = f"Произошла критическая ошибка:\n\n{log_entry}"  # Текст письма
        msg = MIMEText(body, _charset="utf-8")  # Создаем сообщение с кодировкой utf-8
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        try:
            # Подключаемся к SMTP-серверу и отправляем email
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sender_email, password)  # Логинимся
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Отправляем
            server.quit()  # Закрываем соединение
            print("Email успешно отправлен.")
        except Exception as e:
            print(f"Ошибка при отправке email: {e}")

    def save_to_database(self, log_entry):
        conn = sqlite3.connect('logs.db')  # Подключаемся к базе данных (создается, если нет)
        c = conn.cursor()
        
        # Создаем таблицу, если её нет
        c.execute('''CREATE TABLE IF NOT EXISTS logs (
                        levelname TEXT,
                        message TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        
        # Разбираем уровень лога (не самый лучший способ, но новичок так мог бы сделать)
        log_parts = log_entry.split(' - ')
        if len(log_parts) > 1:
            level = log_parts[1]
        else:
            level = 'UNKNOWN'
        
        # Вставляем данные в таблицу
        c.execute("INSERT INTO logs (levelname, message) VALUES (?, ?)", (level, log_entry))
        conn.commit()  # Сохраняем изменения
        conn.close()  # Закрываем соединение
        print("Лог записан в базу данных.")

# Создаем логгер и добавляем к нему наш обработчик
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования
custom_handler = CustomHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
custom_handler.setFormatter(formatter)
logger.addHandler(custom_handler)

# Тестируем логгер
logger.info("Информационное сообщение")
logger.error("Ошибка! Что-то пошло не так.")
