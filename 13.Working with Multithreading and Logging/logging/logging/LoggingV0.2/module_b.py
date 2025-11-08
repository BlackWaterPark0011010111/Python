import logging

logger = logging.getLogger('module_b')

def function_b():
    logger.debug('Запущена функция B')
    logger.warning('Предупреждение из функции B')
    logger.error('Ошибка из функции B')
    logger.critical('Критическая ошибка в функции B')
    logger.info('Функция B завершена')