"""
    集合的CRUD
"""
# 空集合
set = set()
print(set, type(set))

# 增
set.add("jack")
set.add("tom")
set.add("adin")
set.add("odin")
# 添加重复值
set.add("jack")

# 改：无法直接获取数据，因此无法修改
# 删：由于无序存储，所以随机删除（多次执行，结果不同）
ele = set.pop()
print(ele)
print(set)

# 查
print(f"{set}中有元素：{len(set)}个")
for ele in set:
    print(f"{ele}", end=" ")
print()

# 并集
print({1,2,3,4,5}.union({2,3,4,5,6}))
# 差集
print({1,2,3,4,5}.difference({2,3,4,5,6}))