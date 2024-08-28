"""
    数据容器CRUD
"""

# 定义一个空列表
list = []
print(list)

# 增
list.append("jack")
list.append("lucy")
print(list)
# 扩展列表
list.extend(["tom", "jerry"])
print(list)
# 插入元素
list.insert(1, "tom")
print(list)

# 改
list[0] = "jack"
list[-1] = "lucy"
print(list)

# 查
print(f"{list}容器中有：{len(list)}个元素")
list.append("andi")
print(f"{list}容器中有：{list.count('jack')}个jack，{list.count('lucy')}个lucy,{list.count('andi')}个andi元素")
# 查找指定元素的索引
print(f"list容器中jack的索引为：{list.index('jack')}")
# 报错
# valueerror：”jack“ is not in list

# 删
# 索引删除
del list[-1]
ele = list.pop(-1)
print(f"删除list容器中最后一个元素：{ele}")
# 元素删除
list.remove("jack")
print(list)

# 清空
list.clear()
print(list)