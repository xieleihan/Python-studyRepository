"""
    继承（多继承）
"""

class Person:
    name = "Person"
    age = 18
    def eat(self):
        print("Person eat")

class Staff:
    name = "Staff"
    age = 20
    def eat(self):
        print("Staff eat")

class Coder(Person, Staff):
    pass

c = Coder()
print(c.name, c.age)
c.eat()