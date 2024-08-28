"""
    ATM
"""

# 存款
def set_money(num):
    global money
    if num > 0:
        money += num
        print(f"存款成功,{num}元")
    else:
        print("存款失败")
# 取款
def get_money(num):
    global money
    if money >= num:
        money -= num
        print(f"取款成功,{num}元")
    else:
        print("取款失败")
# 查询
def query_money():
    print(f"余额:{money}元")
# 登录
def login():
    global name
    name = input("请输入你的姓名:")
    psw = input("请输入你的密码:")
    if "lvzhitian" == name and "123456" == psw:
        global tag
        tag = True
    else:
        tag = False
        print("登录失败")
        login()
    print(f"欢迎{name}登录")
# home
def home():
    print("1.存款\n2.取款\n3.查询\n4.退出")
    op = int(input("请输入你的选择:"))
    if op == 1:
        set_money(int(input("请输入存款金额:")))
        home()
    elif op == 2:
        get_money(int(input("请输入取款金额:")))
        home()
    elif op == 3:
        query_money()
        home()
    elif op == 4:
        print("退出")
    else:
        print("输入有误")

# 定义全局变量
money = 10000
name = None
tag = False

# 登录
login()
# 循环
# while tag:
#     home()