from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

# AbstractBaseClass 
class Astronaut(ABC):
    def __init__(self, name: str, experience: int):
        self._name = name  # Encapsulation
        self._experience = experience

    @property
    def name(self) -> str: 
        return self._name

    @property
    def experience(self) -> int:  
        return self._experience

    @abstractmethod
    def perform_task(self) -> str:  # Abstract method 
        pass

    def __str__(self) -> str:  # Magic method for string representation
        return f"{self.__class__.__name__}: {self._name}, Experience: {self._experience} years"

# Pilot Astronaut (inherits from Astronaut)
class Pilot(Astronaut):
    def perform_task(self) -> str:  # Polymorphism:
        return f"{self._name} is piloting the spaceship."

# Engineer Astronaut (inherits from Astronaut)
class Engineer(Astronaut):
    def perform_task(self) -> str:  # Polymorphism: 
        return f"{self._name} is repairing the spaceship."
