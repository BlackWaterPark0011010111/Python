import getpass
#import sys
#import os 

def main():
    print("\nBasic input____________") 
    
    pwd = getpass.getpass("Enter password via getpass: ")  
   #pwd = getpass.getpass()  
    print(f"You entered password with length {len(pwd)}")  # показывает длинну пароля в  {len(pwd)} символов
   #print("Contents:", pwd)  # Содержимое
    
    print("\nRegular input __________")  #обычный ввод
    
    visible_pwd = input("Enter password via input: ")  # Введите пароль через input
    print(f"Visible input: {visible_pwd}")  # Видимый ввод
   #print("getpass length:", len(pwd), "| input length:", len(visible_pwd))  # Длина getpass | Длина input
    
    print("\nError handling____________")  #обработка ошибок
    
    try:
        test_input = getpass.getpass("Try to interrupt input (Ctrl+C): ")  # Попробуй прервать ввод
        print("Successful input! Length:", len(test_input))  #успешный ввод и  Длина
    except KeyboardInterrupt:
        print("\nInput was interrupted by user!")  #ввод был прерван пользователем
    except Exception as e:
        print(f"Error occurred: {e}")  #ошибка
    
    print("\nEdge cases_________") 
    
    empty_input = getpass.getpass("Try entering empty password (just Enter): ")  #попробуй ввести пустой пароль
   #empty_input = getpass.getpass(prompt="", stream=None)  #alternative  #альтернатива
    if not empty_input:
        print("You entered empty password!")  #пустой пароль
    else:
        print("You entered non-empty password with length", len(empty_input))  #ввели непустой пароль
    
    print("\nNon-password input_________")  # по вводу непарольных даннх
    
    number_input = getpass.getpass("Enter number secretly: ")  # скрытый ввод числа 
    try:
        number = int(number_input) 
        print(f"You entered number: {number}")
       #print("Square of number:", number**2)  #квадрат числа 
    except ValueError:    
        print("This is not a number!")  
     
    print("1. getpass securely hides input in console")  #getpass скрывает ввод
    print("2. May work incorrectly in IDE")  #в IDE может работать некорректно
    print("3. Suitable not only for passwords but other secret input")  #подходит не только для паролей
   #print("4. Additional research: ...")  #дополнительные исследования

if __name__ == "__main__":
    main()
   #test_additional_functions()