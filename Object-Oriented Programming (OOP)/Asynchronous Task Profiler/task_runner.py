"""CPU-heavy task (cpu_heavy_task): Функция, которая выполняет вычисления на процессоре, создавая нагрузку.
Асинхронная задача async_task---- нагружаем процессор функцией cpu_heavy_task.
Запускаем в потоке thread_worker- при многозадачности по потоку для CPU-bound задач значительного прироста
 производительности не будет из-за GIL (Global Interpreter Lock) в Python
Мы запускаем в процессе process_worker, и процесс обеспечивает параллельность, потому что каждый 
процесс работает в своем собственном пространстве памяти и не ограничен GIL и дляля CPU-bound задач это лучше.
Запуск с использованием процессов (run_processes):здесь нам нужно использовать процессы для выполнения задачи,каждый
процесс работает в своем собственном адресном пространстве, и GIL не влияет на их параллельность,и улучшаем производительность для CPU-bound
асинхронная версия run_async--использует асинхронное выполнение, но  основная нагрузка все равно ложится на CPU.
Для CPU-bound задач использовуем процессы multiprocessing, потому что они обходят GIL и могут использовать несколько ядер процессора."""

import asyncio
import threading
import multiprocessing
import time

def cpu_heavy_task(n):

    count = 0
    for _ in range(n):
        count += 1

    return count

async def async_task(n):
   
    await asyncio.sleep(0)
    return cpu_heavy_task(n)

def thread_worker(n):
    """поток"""
    return cpu_heavy_task(n)

def process_worker(n):
    """процесс"""
    return cpu_heavy_task(n)

def run_threads(n, workers=4):
    """Запускаем задачу в потоках"""
    threads = []
    for _ in range(workers):
        t = threading.Thread(target=thread_worker, args=(n,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def run_processes(n, workers=4):
    """Запускаем задачу в процессах"""
    processes = []
    for _ in range(workers):
        p = multiprocessing.Process(target=process_worker, args=(n,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

async def run_async(n, workers=4):
    """Запускаем задачу асинхронно"""
    tasks = [async_task(n) for _ in range(workers)]
    await asyncio.gather(*tasks)