class Animal:

    def __init__(self, number_of_legs, number_of_eyes):
        self.number_of_legs = number_of_legs
        self.number_of_eyes = number_of_eyes

    def breathe(self):
        print("THIS ANIMAL IS BREATHING")

    def walk(self):
        print("THIS ANIMAL IS WALKNG")

    def summary(self):
        print(f"THIS ANIMAL HAS  {self.number_of_legs} legs and {self.number_of_eyes} eyes")
