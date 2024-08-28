"""
    python异常处理
"""
# NameError
# 名字找不到
# print(name)
# ZeroDivisionError
# 除零
# print(12/0)
# IndexError
# 类型错误
# print("jack"[10000])
# FileNotFoundError
# 文字找不到
# file = open("jnb.json", mode="r")

num1 = int(input("被除数: "))
num2 = int(input("除数: "))
try:
    rel = num1 / num2
    print(rel)
except ZeroDivisionError as e:
    print(e)
    print("除数为零了，请注意！")
else:
    print("继续执行程序！")
finally:
    print("关闭资源")