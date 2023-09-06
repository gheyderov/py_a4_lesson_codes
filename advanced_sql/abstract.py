from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def call(self):
        pass


class Car(Vehicle):

    def go(self):
        print('You drive a car')

    def call(self):
        print('This is a car')


class Motorcycle(Vehicle):

    def go(self):
        print('You ride a motorcycle')

    

c = Car()
m = Motorcycle()


c.call()
m.go()