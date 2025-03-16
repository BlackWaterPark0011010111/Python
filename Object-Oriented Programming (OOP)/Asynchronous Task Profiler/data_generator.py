import random


def generate_data(size=10**6):    #Создаёт список случайных чисел чтобы получить набор случайных чисел для дальнейшей обработки/анализа

    return [random.randint(0, 100) for _ in range(size)]