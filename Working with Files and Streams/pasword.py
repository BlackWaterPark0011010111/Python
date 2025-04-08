
import getpass
#import sys
#import os 

def main():
    """Основная функция для тестирования getpass"""
    
    print("\n=== Тест 1: Базовый ввод ===")
    
    pwd = getpass.getpass("Введите пароль через getpass: ")
   #pwd = getpass.getpass()  
    print(f"Вы ввели пароль длиной {len(pwd)} символов")
   #print("Содержимое:", pwd)
    
    print("\n=== Тест 2: Обычный ввод ===")
    
    visible_pwd = input("Введите пароль через input: ")
    print(f"Видимый ввод: {visible_pwd}")
   #print("Длина getpass:", len(pwd), "| Длина input:", len(visible_pwd))
    
    print("\n=== Тест 3: Обработка ошибок ===")
    
    try:
        test_input = getpass.getpass("Попробуйте прервать ввод (Ctrl+C): ")
        print("Успешный ввод! Длина:", len(test_input))
    except KeyboardInterrupt:
        print("\nВвод был прерван пользователем!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    print("\n=== Выводы ===")
    print("1. getpass надежно скрывает ввод в консоли")
    print("2. В IDE может работать некорректно")
    print("3. Подходит не только для паролей, но и для другого скрытого ввода")
   #print("4. Дополнительные исследования: ...")  

if __name__ == "__main__":
    main()
   #test_additional_functions()