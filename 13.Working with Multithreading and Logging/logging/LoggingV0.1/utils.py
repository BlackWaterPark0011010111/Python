import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(console_handler)

logger.debug("Это сообщение уровня DEBUG (не отобразится)")  # Не будет видно, т.к. уровень INFO
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")

def do_something():
    logger.info("THIS IS INFO MESSAGE  ")
    logger.debug("prepare")
    logger.info("doing")
    logger.warning("im done")

if __name__== "__main__":
    do_something()