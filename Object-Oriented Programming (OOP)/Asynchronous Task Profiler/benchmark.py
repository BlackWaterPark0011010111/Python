#измерение времени работы
"""Здесь мы  измеряем и сравниваем производительность потоков, процессов и асинхронных задач, обрабатывающих данные.
 Что поможет понять, какой метод многозадачности лучше для разных сценариев."""

import time
import asyncio
from task_runner import run_threads, run_processes, run_async
from data_generator import generate_data

N = 10**6  # Для 1 миллиона операций,для заметных результатов при тестировании производительности или анализа

def benchmark():
    """Запускаем и сравнивает методы. потоки threads run_threads(N), , многопоточность threading,процессы processes/run_processes(N),
      multiprocessing.
Асинхронный метод async/asyncio.run(run_async(N)),длявыполнения асинхронно.все выводим в time/секундах"""
    print("Starting benchmarks...\n")

    start = time.time()
    run_threads(N)
    print(f"Threads: {time.time() - start:.4f} sec")

    start = time.time()
    run_processes(N)
    print(f"Processes: {time.time() - start:.4f} sec")

    start = time.time()
    asyncio.run(run_async(N))
    print(f"Async: {time.time() - start:.4f} sec")

if __name__ == "__main__":
    benchmark()
    