""""
    异常处理
"""

try:
    # 可能发生valueerror
    num1 = int(input("被除数："))
    num2 = int(input("除数："))
    # 可能发生zerodiverror
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
except ValueError as e:
    print("输入有误，请重新输入")
    print(e)
except ZeroDivisionError as e:
    print("除数不能为0")
    print(e)

# 对上面进行简化
try:
    num1 = int(input("被除数："))
    num2 = int(input("除数："))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
except (ValueError, ZeroDivisionError) as e:
    if isinstance(e, ValueError):
        print("输入有误，请重新输入")
    elif isinstance(e, ZeroDivisionError):
        print("除数不能为0")