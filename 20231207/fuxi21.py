"""
    去除列表中重复的元素
"""

result = set()
target = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("原始列表：",target)

# 遍历
for ele in target:
    result.add(ele)

# 输出
print("去重后的列表：",result)