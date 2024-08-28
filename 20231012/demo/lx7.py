tuple = ("java","python","cpp","goland")
# 索引访问
print(tuple[0])
print(tuple[-1])
# 获取索引
print(f"cpp在元组中的索引：{tuple.index('cpp')}")
# 元素数量
tuple = ("java","python","cpp","goland")
print(f"python在元组的数量：{tuple.count('python')}")
# 元组长度
print(f"元组长度:{len(tuple)}")
tuple = ("java","python","cpp","goland")
# while循环遍历
index = 0
while index < len(tuple):
    print(f"{tuple[index]}" , end = ' ')
    index += 1
print()
# for循环遍历
for ele in tuple:
    print(f"{ele}" , end = ' ')
print()