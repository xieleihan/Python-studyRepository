"""
    其他常用的魔术方法
"""

class Test:
    # __new__:实例化类时，自动调用，用于创建类的新实例
    def __new__(cls,*args,**kwargs):
        print("__new__(cls,*args,**kwargs)")
        print("new object")
        # 必要时，调用父类创建对象方法
        return super().__new__(cls)

    # __init__:实例化类时，自动调用，用于初始化类的新实例
    def __init__(self,*args,**kwargs):
        print("__init__(self,*args,**kwargs)")
        print("init object")
        super().__init__(*args,**kwargs)

    # __del__:销毁对象时，自动调用，用于释放资源，但是python会在执行完毕后，自动释放资源，所以其实也可以不用去管它
    def __del__(self):
        print("del object")

    # __call__:调用类时自动调用，用于调用类的方法
    def __call__(self,*args,**kwargs):
        print("__call__(self,*args,**kwargs)")
        print("call object")

# 创建并初始化实例
t = Test()
# 将实例当作函数调用
t()
# 销毁用例
del t