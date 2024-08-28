def position_param(name,age,isMarry):
    print(f"姓名：{name}年龄{age}婚后{isMarry}")
# 位置传参：实参对应的形参的定义位置传递参数
position_param("jack",30,True)
def keyword_param(name,age,isMarry):
    print(f"姓名：{name}年龄{age}婚后{isMarry}")
# 关键字传参数：形参名=实参数。。。支持乱序传递
keyword_param(name="andi",age=26,isMarry=False)
keyword_param(isMarry=True,age=35,name="doci")
# 位置传参和关键字混用
keyword_param("mark",isMarry=False,age=28)
def default_param(name,age,isMarry=False):
    print(f"姓名{name}年龄{age}婚后{isMarry}")
# 默认值传参
default_param("petre",18)
default_param("jame",age=32,isMarry=True)
# 可变参数位置传参
def sum(*args):
    print(f"参数：{args}类型{type(args)}")
    sum = 0
    for n in args:
        sum += n
    return sum
# 调用可变参数
result = sum(1,2,3,4,5)
print(f"1~5的累加和{result}")
result = sum(1,2,3,4,5,6,7,8,9,10)
print(f"1~10的累加和{result}")
# 可变参数（关键字传参）
def staff_info(**kwargs):
    # 参数以字典方式存储
    print(f"参数：{kwargs}类型：{type(kwargs)}")
# 调用可变参数
staff_info(name="ldis",age=12)
staff_info(name="dafsdv",age=12,isMarry = False)