"""
    函数递归
"""

# 计算数据n的阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# 输入要计算的数
n = int(input("请输入要计算的数："))
# 函数调用
result = factorial(n)
# 输出
print("阶乘结果为：", result)

# 计算第n个斐波那契数列
def fibonacci_num(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_num(n - 1) + fibonacci_num(n - 2)
# 输入要计算的位置
n = int(input("请输入要计算的位置："))
# 函数调用
result = fibonacci_num(n)
# 输出
print("第", n, "个斐波那契数列为：", result)