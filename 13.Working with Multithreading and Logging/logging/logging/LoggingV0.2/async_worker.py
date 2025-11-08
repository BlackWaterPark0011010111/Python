import logging
import asyncio

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('async_worker')

async def async_task():
    logger.info('Начало задачи')

    try:
        await asyncio.sleep(2)  # Подождем 2 секунды
        
        # Тут ошибка, чтобы проверить обработку исключений
        raise ValueError('Что-то пошло не так!')

    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')  # Логируем ошибку

    logger.info('Конец задачи')

# Запускаем асинхронную функцию
asyncio.run(async_task())