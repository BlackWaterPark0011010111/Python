from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__(4,2)# paws and eyes

    def breathe(self):
        super().breate()
        print("DOGS LOVE TO BREATHE WITH THEIR MOUTHS OPEN")

    def walk(self):
        super().walk()
        print("DOGS LOVE TO RUN")

