"""
    继承：会先创建父类对象再创建子类的对象
"""

class Animal:
    def __init__(self):
        print("Animal is created")

class Cat(Animal):
    # 注意：如果子类显示的定义了构造函数，需要手动调用父类的构造函数，如果子类没有定义构造函数，则会自动调用父类的构造函数
    def __init__(self):
        # 第一种方法：类
        # Animal.__init__(self)
        # 第二种方法：super()
        super().__init__()
        print("Cat is created")

cat = Cat()