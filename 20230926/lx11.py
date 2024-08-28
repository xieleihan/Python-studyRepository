# 定义多返回值函数
def test_return():
    return "jack",23,False
# 获取函数返回值
name,age,isMarry = test_return()
# 输出返回值和类型
print(f"name={name}{type(name)}")
print(f"age={age}{type(age)}")
print(f"ismarry={isMarry}{type(isMarry)}")