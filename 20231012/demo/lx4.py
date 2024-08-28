list = []
print(list)
# 增加元素
list.append("java")
list.append("python")
print(list)
# 扩展列表
list.extend(["markdown","php"])
print(list)
# 插入元素
list.insert(1 , "js")
print(list)
# 修改元素
list[1] = "c"
list[-1] = "vc"
print(list)
# 元素数量
list.append("java")
list.append("git")
print(list)
count = list.count("java")
print(f"有{count}个")
# 元素索引
index = list.index("git")
print(f"git在列表中的索引：{index}")
# delete元素
del list[-1]
del_ele = list.pop(-1)
print(del_ele)
# delete元素（元素）
list.remove("c")
print(list)
# 清空列表
list.clear()
print(list)