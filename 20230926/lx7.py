# 自定义函数
def welcome():
    print("欢迎来到这里")
    print("让我们开启学习")
# 调用函数
result = welcome()
print(f"默认返回值：{result}\nNone字面量类型：{type(result)}")

# 有返回值函数显示返回None
def div(x,y):
    if y == 0:
        return None
    else:
        return x/y
# 调用函数
result = div(10,3)
print(f"10/3={result}")
result = div(10,0)
print(f"10/0={result}")