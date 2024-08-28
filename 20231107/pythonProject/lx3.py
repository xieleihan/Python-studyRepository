""""
    创建对象：构造函数
"""

class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        print("已经创建一个学生对象，并且做了初始化")

stu1 = Student("lvzhitian",20,"Hongkong")
print(f"{stu1.name}{stu1.age}{stu1.address}")
stu2 = Student("lvzhitian2",30 ,"Macau")
print(f"{stu2.name}{stu2.age}{stu2.address}")