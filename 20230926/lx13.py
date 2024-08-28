# 定义一个求和函数
def add(args):
    sum = 0
    for n in args:
        sum += n
    return sum
# 定义形参为函数的函数
def print_result(func,*args):
    # 输出函数参数和数据类型
    print(f"{func}{type(func)}")
    result = func(args)
    print(f"{args}的累加值{result}")
# 调用函数
print_result((add,1,2,3,4,5))
print_result((add,1,2,3,4,5,6,7,8,9,10))