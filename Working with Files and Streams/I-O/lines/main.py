
print("-----------------------------------------------------------------1----")

with open("src/data/task1.txt", "r") as file:
    print(file.read())  # чтение и сразу  выводим
print("-----------------------------------------------------------------2----")

with open("./src/data/task2.txt", "r") as file:
    #чтение всех строки  
    lines = file.readlines() 
    #от третьей строки   
    todos = lines[2:]  
    print(len(todos))  #количество оставшихся строк  
print("-----------------------------------------------------------------3----")

with open("./src/data/task3.txt", "r") as file:
    lines = file.readlines()  # прочитать все 

odd_lines = lines[0::2]  #нечётные 
even_lines = lines[1::2]  #чётные

for line in odd_lines:
    print(line.strip())  #убираем лишние переносы строк
for line in even_lines:
    print(line.strip())
print("-----------------------------------------------------------------4----")

with open("src/data/task4.txt", "r") as file:
    file.seek(1622)  #переходим к нужной позиции
    print(file.read(13))  #читаем 13 символов(до 1634)
print("-----------------------------------------------------------------5----")
with open("src/data/task5.txt", "r") as file:
    first_line = file.readline().strip()  #читаем первую строку и убираем \n
                #в самое ачало
    file.seek(0)  
    count = 0
    for char in first_line:
        # считаем символы
        count += 1  

    print(first_line)
    print(count)
print("----------------------------------------------------------6---")

lengths = [] 

with open("src/data/task6.txt", "r") as file:
    for line in file:
        count = 0
        for char in line.strip():  
            count += 1
        lengths.append(count)  

print(lengths)