"""The application in this file will read the command line options using argparse.
This application should support positional arguments and be called like this: ./app3.py [FIRST_NAME] [LAST_NAME] [AGE]
If age is not specified, it should be assumed that it is 100. If the last name is not specified, it should be assumed that it is "Hanson". If the first name is not specified, should be assumed that it is "Larry".
This application should also support the option --fast. It should print "fast mode enabled" if this is one of the options.
The app should then output the text "Hello [FIRST_NAME] [LAST_NAME]! I see that you have had [AGE + 1] birthdays."."""


import argparse

parser = argparse.ArgumentParser()#создаем  сам парсер


parser.add_argument('first_name', nargs='?', default='Larry', help='First name')
parser.add_argument('last_name', nargs='?', default='Hanson', help='Last name')
parser.add_argument('age', nargs='?', default=100, type=int, help='Age')

parser.add_argument('--fast', action='store_true', help='Enable fast mode')
#добавляем опцию --fast


args = parser.parse_args()#парсим аргументы
#теперь args содержит все переданные пользователем данные.

if args.fast:
    print("fast mode enabled")
# здесь мы формируем строку с именем, фамилией и возрастом +1.
print(f"Hello {args.first_name} {args.last_name}! I see that you have had {args.age + 1} birthdays.")
"""
Он принимает имя, фамилию и возраст в командной строке, то есть 3 позиционных аргумента и мы также можем
 включить "быстрый режим" с флагом --fast.
Если какие-то данные не будут переданы,то  программа подставляет значения по умолчанию:
Имя: "Larry"
Фамилия: "Hanson"
Возраст: 100
 и после этого в скрипта мы добавляем +1 к фозрасту ( {args.age + 1}) и выводим приветствие 

parser.add_argument('first_name', nargs='?', default='Larry', help='First name')
parser.add_argument('last_name', nargs='?', default='Hanson', help='Last name')
parser.add_argument('age', nargs='?', default=100, type=int, help='Age')
Добавляем флаг --fast  - это флаг, который можно просто включить при запуске.

parser.add_argument('--fast', action='store_true', help='Enable fast mode')
Если его указать, args.fast станет True, иначе — False.
проверяем флаг --fast
if args.fast:
    print("fast mode enabled")
и если запустить python app3.py --fast, программа напечатает "fast mode enabled".
Если флаг не указан, этот блок просто пропускается.

если мы запускаем без аргументов  ->  python app3.py   ->   Hello Larry Hanson! I see that you have had 101 birthdays.
(значения по умолчанию)
python app3.py Alice ->  Hello Alice Hanson! I see that you have had 101 birthdays.
python app3.py Alice Smith  ->  Hello Alice Smith! I see that you have had 101 birthdays.
python app3.py Alice Smith 25  ->  Hello Alice Smith! I see that you have had 26 birthdays.

"""