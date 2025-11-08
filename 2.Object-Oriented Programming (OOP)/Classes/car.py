
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def describe(self):
        lio=f'its a {self.make},a model {self.model},and a year {self.year}'
        return lio.title()
    
    def read_odometer(self):
        print(f'it has {self.odometer} or smth somethng')

    def update(self,mileage):
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print('you cant rool back an odometer')
    def increment_odometer(self,miles):
        self.odometer+=miles

car=Car('bmw', 'a4', 2019)
print(car.describe())
car.read_odometer()
car.odometer=30
car.read_odometer()
car.update(23)
car.read_odometer()
car.update(23_500)
car.read_odometer()
car.increment_odometer(100)
car.read_odometer()
