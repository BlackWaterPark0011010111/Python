import logging
import sys
import os
import threading
import asyncio


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


logging.srcfile = None
logging.logThreads = False
logging.logProcesses = False
logging.logMultiprocessing = False
logging.logAsyncioTasks = False


class Phonecall:
    def __init__(self, caller, receiver, duration):
        self.caller = caller
        self.receiver = receiver
        self. duration = duration


    def __str__(self):
        return f"Звонок от {self.caller} к {self.receiver} продолжительностью {self.duration} секунд"

call = Phonecall("123-456-7890", "987-654-3210", 120)
logger.info(call)

def log_thread_info():
    logger.debug(f"Текущий поток: {threading.current_thread().name}, PID: {os.getpid()}")

async def log_asyncio_task():
    logger.debug(f"Ассинхронная задача: {asyncio.current_task().get_name()}, PID: {os.getpid()}")

async def main():
    log_thread_info()
    await log_asyncio_task()

asyncio.run(main())