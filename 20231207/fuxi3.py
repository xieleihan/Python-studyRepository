"""
    Python的输入输出函数
"""

# 输出函数
print("Hello World")
# 输入函数
name = input("请输入你的名字：")

# 简化后的输入输出
age = int(input("请输入你的年龄："))
salary = float(input("请输入你的工资："))
# 格式化输出
print("你的名字是：%s，你的年龄是：%d，你的工资是：%.2f" % (name, age, salary))
# 查看类型函数
print(f"{type(name), type(age), type(salary)}")
# 数据类型转换
# int()
age = int(input("请输入你的年龄："))
# float()
salary = float(input("请输入你的工资："))
# str()
name = str(input("请输入你的名字："))
print(f"你的名字是：{name},你的年龄是：{age},你的工资是：{salary}")

# 输入函数
# 输入函数的功能是从键盘获取用户的输入，并将用户的输入返回给程序。
# 输入函数的格式：
# input()
