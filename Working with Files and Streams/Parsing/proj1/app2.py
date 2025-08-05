"""The application in this file will read the command line options using getopt().
This application should accept the flags -h or --help to print a help text.
This application should let the user set a name with the option -n [NAME] or --name=[NAME].
If a name is given, the application should output Good Morning [NAME]!. If no name is specified, it should just output Good Morning folks!"""
#использование модуля getopt нужен  для обработки аргументов командной строки.
#Функция getopt.getopt(), в ней мы обрабатываем аргументы и разбивает их на список опций.
import getopt
import sys
#просто выводим функцию помощи
def print_help():
    print("Usage:")
    print("-h or --help    Show this help message.")
    print("-n or --name    Set the name.")

try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:", ["help", "name="])
except getopt.GetoptError:
    print("Invalid option")
    sys.exit(2)
 #обработка аргументов, сначала мы считываем аргументы,мы пропуская первый этосамо имя файла,передаем их в getopt.getopt(),
 #который разбирает короткие опции (-h и -n), где n: требует значение в виде имени например
#--help и --name разбирает длинные опции, но name=  он  тоже требует значение.
#потом мы проверяем, какие аргументы были переданы и если -h или --help, выводим просто справку и завершаем работу
#но если -n или --name, мысохраняем переданное имя,но если имени нет,то  по умолчанию используем "folks".

#нам нужно ввести -> 
# python app2.py -n K-9 (какоето имя например), то -n - это опция, а "K-9" - её значение.

name = "folks"
for opt, arg in opts:
    if opt in ("-h", "--help"):
        print_help()
        sys.exit()
    elif opt in ("-n", "--name"):
        name = arg

print(f"Good Morning {name}!")
