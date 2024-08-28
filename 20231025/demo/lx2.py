"""
    文件指针
"""

with open(file="./data.txt", mode="r") as file:
    # 返回当前文件指针位置
    print(file.tell())
    print(file.read())
    # 移动文件指针位置
    file.seek(0)
    # 返回文件指针位置
    print(file.readline())