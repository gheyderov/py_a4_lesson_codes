from users import user_list
from datetime import datetime

class Person:

    count = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        Person.count += 1

    def get_fullname(self):
        return f'{self.name} {self.surname}'
    
    @staticmethod
    def greet():
        return 'Hello World!'
    
    @classmethod
    def get_fullname_from_str(cls, fullname_str, age):
        name, surname = fullname_str.split('-')
        return cls(name, surname, age)
    
    @classmethod
    def get_age_from_bday(cls, name, surname, bday):
        age = datetime.now().year - bday
        return cls(name, surname, age)

    def __str__(self):
        return self.name
    
# 'Mammad-Mammadov', 35
# 'Mammad', 'Mammadov', 1995

    
p1 = Person('Ali', 'Aliyev', 30)
p2 = Person('Samir', 'Mammadov', 20)
p3 = Person.get_fullname_from_str('Mammad-Mammadov', 35)
p4 = Person.get_age_from_bday('Mammad', 'Mammadov', 1995)

for user in user_list:
    p = Person.get_fullname_from_str(user[0], user[-1])
    print(p.get_fullname())

print(p1.get_fullname())
print(p2.get_fullname())
print(p3.name)
print(p3.surname)
print(p4.age)
print(Person.count)
