"""
    函数参数传递
"""

def position_param(name, age, isMarry):
    print(f"姓名：{name} 年龄：{age} 是否结婚：{isMarry}")

# 位置传参
position_param("张三", 18, True)
def keyword_param(name, age, isMarry):
    print(f"姓名：{name} 年龄：{age} 是否结婚：{isMarry}")

# 关键字传参: 形参名 = 实参名 支持乱序传递
keyword_param(isMarry=True, age=18, name="张三")

# 位置传参和关键字传参混合使用
keyword_param("张三", 18, isMarry=True)

def default_param(name, age, isMarry=False):
    print(f"姓名：{name} 年龄：{age} 是否结婚：{isMarry}")
# 默认值传参
default_param("nm",18)
default_param("nbcs",20,True)
# 可变参数（位置传参）
def sum(*args):
    # 参数以元组方式进行存储
    print(f"参数：{args} 类型：{type(args)}")
    sum = 0
    for i in args:
        sum += i
    return sum
# 调用可变参数函数（位置传参）
result = sum(1,2,3,4,5,6,7,8,9,10)
print(f"1-10累加和：{result}")
# 可变参数（关键字传参）
def staff_info(**kwargs):
    print(f"参数：{kwargs} 类型：{type(kwargs)}")
# 调用可变参数函数（关键字传参）
staff_info(name="张三", age=18, isMarry=True)
