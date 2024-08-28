"""
    异常处理
"""

file = None
try:
    # 可能发生valueerror
    num1 = int(input('被除数：'))
    num2 = int(input('除数：'))
    # 可能发生除零错误
    result = num1 / num2
    print(f"{num1}/{num2}={result}")
    # 可能发生filenotfounderror
    file = open('test.txt', 'r',encoding='utf-8')
except (ValueError, ZeroDivisionError, FileNotFoundError) as e:
    if isinstance(e, ValueError):
        print('输入有误')
    if isinstance(e, ZeroDivisionError):
        print('除数不能为0')
    if isinstance(e, FileNotFoundError):
        print('文件不存在')
        # 创建该文件
        print("创建新文件")
        file = open('test.txt', 'w',encoding='utf-8')
        file.writelines('hello world')
    print(e)
else:
    print("读文件数据")
    print(file.readline())
finally:
    file.close()
    print("文件关闭")