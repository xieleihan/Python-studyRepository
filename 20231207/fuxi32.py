"""
    构造函数
"""

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        print("创建一个学生对象，并做了成员属性")

stu01 = Student("Michael", 20, 98)
stu02 = Student("Bob", 22, 100)
print(f"{stu01.name}的年龄是{stu01.age}成绩是{stu01.score}")
print(f"{stu02.name}的年龄是{stu02.age}成绩是{stu02.score}")