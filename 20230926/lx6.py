# 自定义带参数有返回值函数
def shopping(monney , name , price, count):
    pay_money = price * count
    return_money = monney - pay_money
    if return_money >= 0:
        print(f"购物小票\n商品：{name}\n数量：{count}\n消费：{pay_money}")
        return return_money
    else:
        print("金额不足，请重新支付")
        return -1
# 函数调用：接收返回值
money = shopping(100,"足球",44.5,2)
print(f"找零：{money}")
# 函数调用：接收返回值
money = shopping(100,"足球",44.5,3)
print(f"找零：{money}")