""""
    这是阶乘计算
"""
def jiechen(i):
    if i == 1:
        return i
    else:
        x = i * jiechen(i-1)
        return x
x = int(input("请输入要被阶乘的数："))
num = jiechen(x)
print(f"结果是：{num}")

"""
    这里写的是2023-09-25晚上课堂内容回顾
"""
import random
# 斐波那契数列，这个很关键
def inputnum():
    # 这个是调用函数来进行输入
    x = int(input(""))
    return x
def Fibonacci(i):
    # 这个是调用函数求斐波那契
    if i < 0:
        # 第一个判断是判断负数，如果是负数，则调用函数重新输入
        print(f"输入有误，请输入一个非负数")
        print(f"请输入你要输出对应的斐波那契数：", end='')
        fibonacci = inputnum()
        # 这个地方需要定义一个全局变量，可以回到输出结果
        global a
        a = fibonacci
        return fibonacci
    elif i == 0:
        return 1
    elif i == 1:
        return 1
    elif i == 2:
        return 2
    else:
        x = Fibonacci(i-1) + Fibonacci(i-2)
        return x
def Sum_Fibonacci(i):
    if i == 0:
        return 1
    elif i == 1:
        return 2
    elif i == 2:
        return 4
    else:
        # 运用到了求和公式
        x = 0
        x = 2*Fibonacci(i)+Fibonacci(i-1)-1
        return x
print(f"请输入你要输出对应斐波那契数：（这里指的是F（value））:", end='')
# 调用函数，传递数据进入变量
fibonacci = inputnum()
# 赋值给a
a = fibonacci
# 然后进行计算
num = Fibonacci(fibonacci)
sumnum = Sum_Fibonacci(fibonacci)
print(f"F({a})={num}")
print(f"第{a+1}个斐波那契的数是{num}")
print(f"前{a+1}项的和是{sumnum}")
print(f"验证序列")
for b in range(0,a+1):
    print(f"{Fibonacci(b)} ", end='')


# 作者: 南秋SouthAki
# 链接: https://southaki.cn/2023/09/26/Python%E5%AD%A6%E4%B9%A0Day5-2023-09-26-2/
# 来源: SouthAki🍉
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。