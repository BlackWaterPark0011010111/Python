import logging

logger = logging.getLogger('module_a')

def function_a():
    logger.debug('Запущена функция A')
    try:
        2 / 1  # Исключение для логирования 
    except ZeroDivisionError:
        logger.exception('Ошибка в функции A')
    logger.info('Функция A завершена')