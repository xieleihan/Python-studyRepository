"""
    os模块目录操作
"""

# 导入模块
import os

# 创建单级目录
if not os.path.exists("./a"):
    os.mkdir("./a")

# 重命名目录
os.rename("./a", "./b")

# 删除目录
os.rmdir("./b")

# 创建多级目录
os.makedirs("./a/b/c")
os.makedirs("./d/e/f/h.txt")
# 删除多级目录
os.removedirs("./a/b/c")
os.removedirs("./d/e/f/h.txt")