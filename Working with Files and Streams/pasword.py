import getpass
import sys 

password = getpass.getpass("Введите пароль: ")  # основной способ
print("Пароль принят! (но не выводим его на экран)")
# password = getpass.getpass() 
# password = getpass.getpass(stream=sys.stderr)  # вывод подсказки в stderr (не всегда видно)
#не работает в юпитер #TODO: (разобраться потом)
# getpass.getpass() в PyCharm показывает ввод — это баг?

try:
    hidden_input = getpass.getpass("Попробуйте ввести текст скрыто: ")
    print(f"Длина ввода: {len(hidden_input)}") 
except Exception as e:
    print(f"Ошибка: {e}")  

visible_input = input("Теперь введите текст видимо: ")
print(f"Видимый ввод: '{visible_input}'")  # демонстрация разницы
username = getpass.getuser()  # получаем имя 
print(f"Ваш системный логин: {username}")

import os
os.environ['USER'] = 'test_user'  # попытка обмануть getuser()
print(f"Обманчивый логин: {getpass.getuser()}")  # всё равно вернёт настоящий


try:
    fake_password = getpass.getpass("Попробуйте ввести пароль (но не в консоли): ")
except getpass.GetPassWarning:
    print("Внимание: ввод может быть виден!") 
except Exception as e:
    print(f"Неожиданная ошибка: {e}")


hidden_number = getpass.getpass("Введите число скрыто: ")
try:
    number = int(hidden_number)
    print(f"Вы ввели число: {number}")
except ValueError:
    print("Это не число!")

try:
    secret = getpass.getpass("Нажмите Ctrl+C во время ввода: ")
except KeyboardInterrupt:
    print("\nCanceled by USER!")
print("Длина ввода: " + len(hidden_input))  # TypeError: can only concatenate str to str 