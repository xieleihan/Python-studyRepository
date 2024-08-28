""""
    os模块文件操作
"""

# 导入模块
import os

# 创建文件（没有文件就创建文件）
open(file="a.txt", mode="w", encoding="utf-8")

# 重命名文件
os.rename("a.txt", "b.txt")

# 设置 休眠
os.sleep(10)

# 删除文件
os.remove("b.txt")