from car import Car
class Battery():
    def __init__(self, battery_size=75,power=100):
        self.power=power
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size ==75:
            range=260
        elif self.battery_size==100:
             range=315
        print(f'this car can go about {range} miles')
    def upgrade_battery(self,battery_size=100):

        if self.battery_size!=100:
            range=100
            print('yes,we`ve got 100 power')
        else:
            print('Continue')


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=75
        self.battery = Battery()

    def describe_battery(self):
        print(f'This car has a {self.battery_size} -kwh battery')
        

my_tesla=ElectricCar('tesla', 'model s', 2019)
print(my_tesla.describe())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()

