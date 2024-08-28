"""
    类和对象
"""

# 定义类
class Person:
    # 属性
    name = None
    age = None
    friends = None
    # 构造函数
    def __init__(self, name, age, friends):
        self.name = name
        self.age = age
        self.friends = friends
    # 行为（函数）
    def introduce(self):
        print(f"")
        print(f"大家好，我叫{self.name}，今年{self.age}岁，我的好朋友是：{self.friends}")
# 定义对象
obj = Person("小明", 20, ["小红", "小黑"])
# 介绍自己
obj.introduce()