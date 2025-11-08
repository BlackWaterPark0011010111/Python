
import os
import logging
import logging.config
import threading
import asyncio
import sys
from module_a import function_a
from module_b import function_b
from async_worker import async_task
from handlers import logger as handlers_logger


log_dir = os.path.join("logging/Logger/LoggingV0.2")#Здесь мы указываем и создаем путь к нашей папке где будет зраниться файл с логами"""
os.makedirs(log_dir, exist_ok=True)  # Создаст папку, если её нет
log_file = os.path.join(log_dir, "app.txt")# Файл, куда будем записывать логи

sys.stdout.reconfigure(encoding='utf-8')   # Эта строка создаёт папку, если её нет
sys.stderr.reconfigure(encoding='utf-8')  # Файл, куда будем записывать логи

def setup_logging():

    """
    Настраиваем логирование: куда и в каком формате будем записывать логи.
    """

    logging.config.dictConfig({
        'version': 1, # Версия конфигурации логирования
        'disable_existing_loggers': False,
        'formatters': {
            'standard': { # Подробный формат с точным временем (добавляем путь к файлу и строку)
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d'
            },
        },
        'handlers': {  # Обработчики логов (куда отправлять логи)
            'console': {  # Логи в консоль
                'level': 'DEBUG',  # Выводим всё от DEBUG и выше
                'class': 'logging.StreamHandler',  # Потоковый обработчик (консоль)
                'formatter': 'standard',  # Используем стандартный формат
                'stream': sys.stdout,  # Выводим в стандартный поток (консоль)
            },
            'file': {  # Логи в файл
                'level': 'DEBUG',  # Записываем всё от DEBUG и выше
                'class': 'logging.FileHandler',  # Файловый обработчик
                'filename': log_file,  # Имя файла для логов
                'formatter': 'detailed',  # Используем подробный формат
                'encoding': 'utf-8',  # Чтобы поддерживать кириллицу
                'mode': 'a',  # Открываем файл в режиме "дописать" (append), а не перезаписывать
            },
        },
        'loggers': {  # Настраиваем сами логгеры
            '': {  # Главный логгер (основной)
                'handlers': ['console', 'file'],  # Логи и в консоль, и в файл
                'level': 'DEBUG',  # Выводим всё от DEBUG и выше
                'propagate': False  # Не передаём дальше
            },
            'module_a': {  # Логгер для module_a
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': False
            },
            'module_b': {  # Логгер для module_b (но пишем только ошибки!)
                'handlers': ['console', 'file'],
                'level': 'ERROR',
                'propagate': False
            },
            'async_worker': {  # Логгер для async_worker (ошибки)
                'handlers': ['console', 'file'],
                'level': 'ERROR',
                'propagate': False
            },
            
        }
    })

if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Пример записи логов
    logger.info("Приложение запущено")
    
    # Запуск многозадачности
    thread_a = threading.Thread(target=function_a)
    thread_b = threading.Thread(target=function_b)
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()

    # Асинхронная задача
    async def main():
        await async_task()

    asyncio.run(main())
    
    logger.info('Приложение завершено')
