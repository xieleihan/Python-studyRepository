"""
    装饰器的封装
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        print("get")
        return self.__age

    @age.setter
    def age(self,age):
        print("set")
        self.__age = age

s = Student("zhangsan", 18)
s.age = 21
print(s.age)