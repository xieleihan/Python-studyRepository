import switch

accounts = {
    "11111111":80000,
    "22222222":100
}
class ATM:
    def query_money(self,account):
        if accounts[account]:
            print(f"{account},有{accounts[account]}")
        return accounts[account]
    def set_money(self,account,money):
        yuer = None
        if accounts[account]:
            accounts[account] += money
            print(f"{account} 存储 {money} 成功。")
            yuer = accounts[account]
        return yuer, money

    def get_money(self, account, money):
        yuer = None
        if accounts[account]:
            if accounts[account] >= money:
                accounts[account] -= money
                print(f"{account} 取出 {money} 成功。")
                yuer = accounts[account]
        return yuer, money

atm = ATM()

acc = input("Enter account:")
print("1:存钱；2：取钱；3：查询")
x = int(input("Enter"))

if(x == 2):
    try:
        yuer, money = atm.get_money(acc, 10000)
        print(f"余额:{yuer} 取出:{money} Happy去")
    except KeyError as e:
        print("账号不存在")
        print(e)
if(x == 1):
    try:
        yuer, money = atm.set_money(acc, 10000)
        print(f"余额:{yuer} 存入:{money} ")
    except KeyError as e:
        print("账号不存在")
        print(e)

if(x == 3):
    try:
        yuer= atm.query_money(acc)
        print(f"余额:{yuer}")
    except KeyError as e:
        print("账号不存在")
        print(e)

"""
    后面自己去补充
"""