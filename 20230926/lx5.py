# 自定义带参数的函数
def print_data(data):
    for n in data:
        print(f"{n}", end='')
    print()
# 调用函数
print_data("hello world")
print_data(range(1,11))