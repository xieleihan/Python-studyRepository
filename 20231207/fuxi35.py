"""
    继承
"""

class Father:
    def __init__(self):
        print("father构造函数")
class Son(Father):
    def __init__(self):
        Father().__init__(self)
        print("son构造函数")

son = Son()