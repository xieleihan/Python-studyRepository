"""
    创建类和对象
"""

# 类和对象
# 1.静态特征
# 2.动态行为

# 属性
class Person:
    name = None
    age = None
    friends = None
    # 构造函数
    def __init__(self, name, age, friends):
        self.name = name
        self.age = age
        self.friends = friends
    # 行为
    def introduce(self):
        print(f"大家好，我是{self.name},今年{self.age}岁，我朋友有{self.friends}")

# 定义对象
obj = Person("lichungan", 40 , ["hey", "you","hello"])

obj.introduce()