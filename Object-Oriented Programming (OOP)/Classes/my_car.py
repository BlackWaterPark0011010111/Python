from car import Car
from electric_car import ElectricCar
from electric_car import ElectricCar as EC
                #модуль.имя класса
                #если импортируем класс дочерний то и класс родитель тоже,потому что ему нужен доступ к классу родителю
                # потому что при создании экземпляра,будет ошибка

my_new_car=Car('audi','a4',2019)
print(my_new_car.describe())
my_new_car.odometer=23
my_new_car.read_odometer()
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.describe())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.describe())
##my_tesla = ElectricCar('tesla','roadster', 2019)
#print(my_tesla.describe())
my_tesla=EC('tesla','roadster',2019)