from german_shepard import GermanShepard
from animal import Animal
from dog import Dog
if __name__ == "__main__":
    animal = Animal(2, 2)  
    dog = Dog() 
    german_shepard = GermanShepard()  

    animal.summary()
    dog.summary()
    german_shepard.summary()

    animal.breathe()
    dog.breathe()
    german_shepard.breathe()

    animal.walk()
    dog.walk()
    german_shepard.walk()