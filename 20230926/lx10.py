# 全局变量
num = 10
def fun_test01():
    # 全局声明
    global num
    # 局部变量：同名
    num = 20
def fun_test02():
    # 全局声明
    global num
    # 局部变量：同名
    num = 30
# 全局环境
print(f"num={num}")
fun_test01()
fun_test02()
print(f"num={num}")