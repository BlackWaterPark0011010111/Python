class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f'{self.name} is sitting')

    def roll_over(self):
        print(f'{self.name} is rolling over')

my_dog=Dog('will', 6)
print(f'My dog is {my_dog.name}')
print(f'and he`s a {my_dog.age} years old')
my_dog.sit()
