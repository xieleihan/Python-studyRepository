"""
    函数的内容
"""

# 自定义带参数有返回值的函数
def shopping(money, name, price, count):
    pay_money = price * count
    return_money = money - pay_money
    if return_money >= 0:
        print(f"购物小票\n商品名称：{name}\n商品单价：{price}\n商品数量：{count}\n商品总价：{pay_money}")
        return return_money
    else:
        print("余额不足，请充值")
        return -1

# 函数调用：接收返回值
money = shopping(100, "苹果", 10, 2)
print(f"找零：{money}")