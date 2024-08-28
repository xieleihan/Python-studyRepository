"""
    列表 索引
"""
list = ["java","python","cpp","goland"]
# 正向索引
print(f"{list[0]} {list[1]} {list[2]} {list[3]}")
# 反向索引
print(f"{list[-1]} {list[-2]} {list[-3]} {list[-4]}")
# 嵌套访问
list = [["java","python","cpp"],[1000,800,500]]
print(f"{list[0][2]} {list[-1][-1]}")