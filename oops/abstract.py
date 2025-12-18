#ABSTRACTION (hinding internal details and showing only essential features)
from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class lion(animal):
    def make_sound(self):
        print("roar")

lion1 = lion()
lion1.make_sound()