"""
    data:2023-09-26
    这个文件实现的是ATM系统实现
"""
import random

# 函数的定义
def Save_monney(account , float_new_monney):
    """
    这个函数实现的是ATM机的存钱操作
    :param account: 这个地方传入账号的信息
    :param float_new_monney: 这个地方表示存入的金额
    :return: 账户余额
    """
    if float_new_monney > 0:
        return account + float_new_monney
    else:
        # 提示钞票error
        print("请取回无法识别的钞票")
        return None

def popup_monney(account ,float_new_monney):
    """
    这个功能实现的是ATM取款操作
    :param account: 这个参数传递账号信息
    :param float_new_monney: 这个地方表示存入金额
    :return: 账户余额
    """
    if float_new_monney <= account:
        return account - float_new_monney
    else:
        print("卡内余额不足，无法执行操作")

def Transfer(account , float_new_monney , new_account , new_float_new_monney):
    """
    这个函数实现的是转账操作
    :param account: 这个参数是传递的是操作者的信息
    :param float_new_monney: 这个参数传递的是操作者需要操作的金额
    :param new_account: 这个参数传递的是转账到账的人的信息
    :param new_float_new_monney: 这个参数传递的是转账到账人的金额
    :return: bool是否成功
    """

def Query_account(account):
    """
    这个函数主要是用于回弹用户个人的信息
    :param account: 这个参数需要给入用户的账号信息
    :return: 个人信息
    """
    # random.uniform用于返回一个随机的浮点数
    monney = random.uniform(10000,50000)
    return monney

def password(password):
    """
    这个函数实现的是对账号的验密
    :param password: 这个参数需要传递密码
    :return: bool值，true则允许接下来的操作
    """
    account_password = "230926"
    for a in range(1,7):
        if password[a] == account_password[a]:
            print("密码正确")
            return True
        else:
            print("密码错误")
            return None
        # else:
        #     print("你的密码有误，请重新输入")
        #     b = 3
        #     b -= 1
        #     print(f"还剩下{b}机会")
        #     if b == 0:
        #         print("你的账户已锁定")
        #         return False
        #     else:
        #         tv3 = input("请输入密码：")
        #         password(tv3)
            # for b in range(1,4):
            #     print(f"还剩下{3 - b}机会")
            #     if b == 3:
            #         print("你的账户已锁定")
            #         return False
            #     else:
            #         tv2 = input("请输入密码：")
            #         password(tv2)

def welcome():
    """
    这个函数主要是实现的是欢迎信息的打印，以及输出一个卡号
    由于暂时没加入数据库，使用随机数生成一个
    :return: 返回一个卡号，模拟机器读卡操作
    """
    print("欢迎使用银行ATM服务")
    print("请插卡")
    card_account=random.randint(10000000000000000,660000000000000000)
    return card_account

def Print():
    print("你可以进行其他操作")
    print(f"查询到你的卡号{card_account}里面的余额为：{monney}")
    print("=============================")
    print("输入1：存款\t输入2：取款")
    print("输入3：转帐\t输入4：退卡")
    print("=============================")

# main
# 系统调用

card_account = welcome()
tv2 = input("请输入密码：")
x = password(tv2)
monney = Query_account(card_account)
if x == True:
    Print()
    for a in range(1,100):
        i = int(input("请操作："))
        if i == 1:
            new_monney = float(input("请输入存入金额："))
            result = Save_monney(monney, new_monney)
            if result == None:
                print("请取走无法识别的钞票")
            else:
                print(f"存款成功！，你账户上余额{result}")
                monney = result
            Print()
            # i = int(input("请继续你的操作："))
        if i == 2:
            new_monney = float(input("请输入取款金额："))
            result = popup_monney(monney, new_monney)
            if result == None:
                print("取款需要储蓄账户余额充足")
            else:
                monney = result
                print(f"取款成功！，你账户上余额{result}")
            Print()
            # i = int(input("请继续你的操作："))
        if i == 3:
            new_monney = float(input("请输入转账金额："))
            result = popup_monney(monney, new_monney)
            if result == None:
                print("转账需要储蓄账户余额充足")
            else:
                monney = result
                Counterpart_account = input("请输入对方账户或卡号：")
                Counterpart_new_monney = Query_account(Counterpart_account)
                receiver = Counterpart_new_monney
                new_result = Save_monney(receiver, new_monney)
                print(f"转账成功！，你账户上余额{result}")
                print(f"对方账户{Counterpart_account}，现有余额{receiver}")
                print(f"查询到对方的卡号{Counterpart_account}，转账后余额为：{receiver+new_result}")
            Print()
            # i = int(input("请继续你的操作："))
        if i == 4:
            print("请取回你的卡")
            break

elif x == None:
    # tv2 = input("请输入密码：")
    # x = password(tv2)
    # if count == 3:
    #     print("账户被锁")
    for b in range(1,4):
        print(f"还剩{3-b}机会")
        if b == 3:
            print("账户被锁")
            print("请联系发卡行")
            break
        tv2 = input("请输入密码：")
        x = password(tv2)
else:
    print("请联系发卡行")

