"""
    os模块文件读写
"""

# 导入模块
import os

# 写入文件
writer = os.open(path="./a.txt",flags=os.O_CREAT | os.O_WRONLY)

# 直接写入字符串会报错

content = b"this is a test"
os.write(writer, content)

# 读文件
reader = os.open(path="./a.txt", flags=os.O_RDONLY)
data = os.read(reader,os.path.getsize("./a.txt"))
print(data.decode("utf-8"))