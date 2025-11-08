class Restaurant:
    def __init__(self, name, type):
        self.name=name
        self.type=type
        self.number_served = 0 
    def describe(self):
        print(f'This is a {self.name} restaurant and its a {self.type} restaurant')

    def served(self):
        print(f'Well weve got {self.number_served}')
    def open_restaurant(self):
        print(f'A {self.name} is open now!')

restaurant=Restaurant('BlakWater','italian')
restaurant.describe()
print(f'A name of this place is  {restaurant.name} ')

print(f'And its a {restaurant.type} type')
restaurant.describe()
restaurant.open_restaurant()
restaurant1=Restaurant('Fire','German')
restaurant1.describe()
restaurant1.open_restaurant()


restaurant.number_served = 15
restaurant.served()

class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.name=name
        self.type=type
        self.flavors=['chocolate','vanilla','berry']
    def flavor(self):
        print(f'What type do u preffer?: {self.flavors} ?')
ice_cream=IceCreamStand('Jack`s','american')
ice_cream.flavor()