"""
    多态
"""

class Animal:
    def yell(self):
        pass

class Dog(Animal):
    def yell(self):
        print('汪汪汪')

class Cat(Animal):
    def yell(self):
        print('喵喵喵')

# 演示方式1
animal: Animal = Dog()
animal.yell()
animal: Animal = Cat()
animal.yell()
print("----------------")
# 演示方式2
animals: [Cat(), Dog()]
for animal in animals:
    animal.yell()