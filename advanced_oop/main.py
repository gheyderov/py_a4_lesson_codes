from typing import Any


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} | Age: {self.age}"

    @property
    def agee(self):
        return self.age

    @agee.setter
    def agee(self, value):
        if value < 0:
            raise ValueError("Age must be more than zero!")
        self.age = value


class Employee(Person):

    _working_hours = '09:00 - 18:00'

    def __init__(self, first_name, last_name, age, department, salary):
        super().__init__(first_name, last_name, age)
        self.deparment = department
        self.salary = salary

    def raisee(self):
        raise_limit = 0.2
        result = self.salary + self.salary * raise_limit
        return result

    def __str__(self):
        return f"{self.first_name} {self.last_name} | Age: {self.age} Department {self.deparment} Salary {self.salary}"


class ComputerEngineer(Employee):

    def __init__(self, first_name, last_name, age, department, salary):
        super().__init__(first_name, last_name, age, department, salary)

    def raisee(self):
        raise_limit = 0.3
        result = self.salary + self.salary * raise_limit
        return result

    def __str__(self):
        return super().__str__()
    

class DataAlanytics(Employee):

    def __init__(self, first_name, last_name, age, department, salary):
        super().__init__(first_name, last_name, age, department, salary)

    def raisee(self):
        raise_limit = 0.4
        result = self.salary + self.salary * raise_limit
        return result

    def __str__(self):
        return super().__str__()
    




# c = ComputerEngineer('John', 'Doe', 30, 'IT', 3000)
# d = DataAlanytics('Smith', 'Doe', 20, 'DATA', 5000)

# employee_list = [c, d]

# for employee in employee_list:
#     print(employee.raisee())


class Calculation1:

    def call(self):
        print('Calc1')


class Calculation2:

    def call(self):
        print('Calc2')


class Calculation3(Calculation1, Calculation2):

    def call(self):
        return super().call()
    


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def call(self):
        pass

    def go(self):
        pass



class Car(Vehicle):

    def call(self):
        print('This is a car')


v = Vehicle()
c = Car()

v.call()
c.call()