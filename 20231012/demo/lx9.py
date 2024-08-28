"""
    这里是dictionary字典容器
    特点：
    1.存储键值，key和value可以是任意类型，key不可以为字典
    2.key可以访问value，不支持索引
    3.key不能重复，不可以存储重复的数据
    4.支持crud
"""
# 增
dic = {}
dic["name"] = "jack"
dic["age"] = 23
print(dic)

# 改
dic["age"] = 24
print(dic)

# 删
del dic["age"]
print(dic)

# 查
print(dic["name"])

# 重建
dic.clear()

# 老师的
# 增加
dict = {}
print(dict)

dict["python"] = 100
dict["java"] = 60
dict["js"] = 80
print(dict)

# 删除
del dict["python"]
print(dict)
ele = dict.pop("js")
print(ele,type(ele))
print(dict)

# 修改
dict["python"] = 90
print(dict)

# 查询
for key in dict:
    print(key, dict[key])
print()

for name in dict.keys():
    print(f"{name}" ,end='')
print()

for key,value in dict.items():
    print(f"{key} = {value}" ,end=' ')
print()

sum = 0
for value in dict.values():
    sum += value
print(f"{sum}")

dict.clear()