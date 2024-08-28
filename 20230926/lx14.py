# 定义函数为参数的函数
def call_func(func,x,y):
    result = func(x,y)
    print(f"{x}+{y}={result}")
# 调用函数：参数为匿名函数
call_func(lambda a,b:a+b,10,20)
# 匿名函数:赋值给有名函数
add = lambda a,b:a+b
print(f"{add}{type(add)}")
print(f"{add(-10,-20)}")