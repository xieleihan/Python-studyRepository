"""
    继承的练习
"""

class Staff:
    id = None
    name = None
    def __init__(self, id, name):
        self.id = id
        self.name = name
        print("Staff构造函数")

class Father:
    children_name = None
    children_age = None
    def __init__(self, children_name, children_age):
        self.children_name = children_name
        self.children_age = children_age
        print("Father构造函数")

class Teacher(Staff, Father):
    def __init__(self, id, name, children_name, children_age):
        Staff.__init__(self, id, name)
        Father.__init__(self, children_name, children_age)
        print("Teacher构造函数")
    def __str__(self):
        return f"{self.id},{self.name},{self.children_name},{self.children_age}"

t = Teacher(1, "张三", "李四", 18)
print(t)