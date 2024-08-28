tuple = ("hello" , "12156000" , ["python","data","ai"])
# 修改元组中嵌套的列表元素 “ai”换成“world“
tuple [2][-1] = "world"
# 格式化输出
print(f"{tuple[0]},{tuple[1]},{tuple[2]}")
# 循环遍历
for ele in tuple[-1]:
    print(f"{ele}", end= ' ')
print()