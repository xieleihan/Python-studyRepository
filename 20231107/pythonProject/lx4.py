"""
    魔术方法
"""

class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        print("已经创建一个学生对象，并且做了初始化")

    # __str__:默认输出类和内存地址
    def __str__(self):
        print("__str__(self)")
        return f"{self.name}{self.age}{self.address}"

    # 默认进行<,>会报错，所以需要魔术方法__lt__
    def __lt__(self,other):
        print("__lt__(self,other)")
        return self.age < other.age

    # 默认进行<=,>=会报错，所以需要魔术方法__le__
    def __le__(self,other):
        print("__le__(self,other)")
        return self.age <= other.age

    # 默认==是进行比较两个对象的内存地址
    def __eq__(self,other):
        print("__eq__(self,other)")
        return self.address == other.address

stu1 = Student("lvzhitian",20,"Hongkong")
stu2 = Student("lvzhitian2",30,"Macau")

# 默认调用的是__str__魔术方法
print(stu1)
print(str(stu1))

# 默认不能进行<,>比较
print(stu1 < stu2)
print(stu1 > stu2)

# 默认不能进行<=,>=比较
print(stu1 <= stu2)
print(stu1 >= stu2)

# 默认==比较的是两个对象
stu3 = stu1
stu4 = Student("lvzhitian3",40,"Taiwan")
print(stu1 == stu2)
print(stu1 == stu3)
print(stu1 == stu4)