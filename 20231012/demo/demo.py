"""
    这个主要进行list序列容器的学习
    list容器的特点：
    1.可以存储不同数据类型的数据
    2.有序存储（记录存储的数据）、索引
    3.数据可以重复
    4.可以进行增删查改
"""
# 定义空列表
list = []

# 增加
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
print(list,type(list))

# 列表的扩展
list.extend([6,7,8,9,10])
print(list,type(list))

# 指定位置插入
list.insert(0,11)
print(list,type(list))

# 使用+
list += ["hello","world"]
print(list)

# 使用*
list *= 3
print(list)

# 删除
list = ['odin', 'jack', 'lucy', 'andi', 'jame', 'peter']
del list[0]
print(list)
del list[-1]
print(list)
ele = list.pop(-3)
print(ele)
print(list)
list.remove("andi")
print(list)

# 改
list = ['odin', 'jack', 'lucy', 'andi', 'jame', 'peter']
list[2] = "merry"
print(list)

# 查
print(len(list))
list.append("odin")
list.append("odin")
print(list.count("odin"))
print(list[4], list[-4])
print(list)
print(list.index("odin"))

# 遍历
for ele in list:
    print(f"{ele} ", end='')
print()

# 清空
list.clear()
print(list)

"""
   主要进行tuple序列(容器)的学习
   作者：jack
   日期：23.10.10

   tuple容器的特点：
   1、可以存储不同数据类型的数据
   2、有序存储(记录存储的顺序)、索引[0,len-1]
   3、数据可以重复
   4、只能进行查询
"""

t = ("关羽", "张飞", "刘备", "赵云", "刘备")
print(t[0], t[-1])
print(len(t))
print(t.count("刘备"))
print(t.index("刘备"))

# 尝试修改元组的值
# t[-2] = "赵子龙"

# 当元组中只有一个数据的时候需要给该元素后面添加,
t = ('a',)
print(t, type(t))

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

"""
    set的用法
    特点：
    1.可以存储不同数据类型
    2.无序存储，不支持索引
    3.删除只能用pop
    4.不可以存储重复数据
    5.支持crud
"""
# 新建
s = set()
print(s,type(set))

# 增加
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s,type(s))
set1 = {"hello","world"}
print(set.union(set1))
print(s.difference(set1))

# 删除
s.remove(2)
print(s,type(s))
ele = s.pop()
print(ele,type(ele))

# 遍历
for ele in s:
    print(f"{ele} ", end='')
print()

# 改
s = {-1,-2,-3}
print(s)

# 查询长度
print(len(s))

# 再次遍历
for ele in s:
    print(f"{ele} ", end='')
print()

print(sorted(s))