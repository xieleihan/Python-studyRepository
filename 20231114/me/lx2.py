"""
    类方法和静态方法的装饰器
"""

class Student:

    @classmethod
    def class_method(cls):
        print('class method')
        print(cls)

    @staticmethod
    def static_method():
        print('static method')

s = Student()
s.class_method()
Student.class_method()
Student.static_method()
s.static_method()