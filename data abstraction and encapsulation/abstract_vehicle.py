from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car starts with key ")
class bike(vehicle):
    def start(self):
        print("bike starts with self start button ")
c=car()
c.start()
b=bike()
b.start()