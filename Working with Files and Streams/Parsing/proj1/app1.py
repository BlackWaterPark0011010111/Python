"""The application in this file will read the command line options using sys.argv.
If one of the options is --help, it should output a small help text.
If one of the options is --fast is should print the text "fast mode enabled" to the command line.
If --fast is not one of the options it should print the text "slow mode enabled" to the command line."""

import sys
#python app1.py --help
if '--help' in sys.argv:# .argv, мы используем чтобы прочитать аргументы командной строки.
    #здесь мы роверяем, есть ли вообще аргумент --help в списке sys.argv.
    #если передам  --help параметр,то будем видеть вывод помощи.
    #если --fast,  то выводим "fast mode enabled", иначе — "slow mode enabled".
    print("This is a simple program to check the mode. Use --fast for fast mode and --help for help.")
elif '--fast' in sys.argv: # python app1.py --fast
    print("fast mode enabled")
else:
    print("slow mode enabled")