"""
    继承：当一个类中定义的属性和方法需要在另一个类中直接使用，且该类和上一个类之间存在is a 的关系，就可以使用继承来实现属性和方法的重复使用
    - is a 的关系 Person Staff Staff is a Person（继承） Car is a cat（no）
    - 继承的实现
    class Student（person，staff）
"""

class Father:
    name = "jack"
    age = 40
    def teacher(self):
        print("teaching...")

class Son(Father):
    pass

s = Son()
print(s.name, s.age)
s.teacher()