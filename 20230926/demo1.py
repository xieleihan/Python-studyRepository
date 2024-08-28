""""

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