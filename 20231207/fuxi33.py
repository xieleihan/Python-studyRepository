""""
    魔术方法
"""

class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    # __str__:默认输出类和内存地址
    def __str__(self):
        return f"name={self.name},age={self.age},score={self.score}"

    # 默认进行<>会报错
    def __lt__(self, other):
        return self.score < other.score

    # 默认进行<=,>=会报错
    def __le__(self, other):
        return self.score <= other.score

    # 默认==比较的是两对象的内存地址
    def __eq__(self, other):
        return self.score == other.score

stu01 = Student("zs",18,99)
stu02 = Student("lisi",18,93)
# 默认调用的是__str__魔术方法
print(stu01)
print(str(stu01))
# 默认调用的是__lt__魔术方法
print(stu01 < stu02)
print(stu01 > stu02)
# 默认调用的是__le__魔术方法
print(stu01 <= stu02)
print(stu01 >= stu02)
# 默认调用的是__eq__魔术方法
stu03 = stu01
stu04 = Student("wanwu",18,80)
print(stu03 == stu04)
print(stu01 == stu03)
print(stu01 == stu04)