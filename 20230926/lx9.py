# 全局变量
num00 = 10
def fun_test01():
    # 局部变量
    num01 = 20
    print(f"funt01局部变量：num01={num01}")
    print(f"funt01的全局变量：num00={num00}")
def fun_test02():
    # 局部变量
    num02 = 30
    print(f"funt01局部变量：num01={num02}")
    print(f"funt01的全局变量：num00={num00}")
# 全局环境
print(f"全局变量：num00={num00}")
fun_test01()
fun_test02()
# 访问局部变量：编辑器报错
# print(f"局部变量：num01={num01}")
# print(f"局部变量：num02={num02}")