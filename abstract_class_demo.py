from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
    @abstractmethod
    def make_sound(self) -> None: pass
    
    def display(self):
        print(f"Name:{self.name}")
        
        
class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    def make_sound(self) -> None:
        print("Woof!")

doggy=Dog("doggy")
doggy.display()
doggy.make_sound() 