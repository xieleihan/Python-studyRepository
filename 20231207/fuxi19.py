"""
    字典的遍历
"""

# 定义字典
dict = {"python":100,"java":90,"c++":70}

# key遍历
for key in dict.keys():
    print(f"{key} = {dict[key]}",end=" ")
print()

score = 0

# value遍历
for value in dict.values():
    print(f"{value}",end=" ")
    score += value
print(f"总分：{score}")

# item遍历
for k,v in dict.items():
    print(f"{k} = {v}",end=" ")
print()