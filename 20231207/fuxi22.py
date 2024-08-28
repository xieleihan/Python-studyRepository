"""
    切片
"""

# 列表
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 开始索引
print(list1[4:])

# 结束索引
print(list1[:5])

# 区间索引
print(list1[2:5])

# 反向索引
print(list1[-1::-1])

# 省略索引
print(list1[:])

# 步长
print(list1[::2])
print(list1[1::-2])
print(list1[::-1])
print(list1[::-2])