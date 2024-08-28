"""
    拷贝图片，注意是二进制的
"""

# 1.打开图片
sources = open(file=r"C:\Users\Administrator\Desktop\day08\911.jpg",mode="rb")
copyimg = open(file=r"C:\Users\Administrator\Desktop\copy.jpg",mode="wb")

# 2.边读边写
for line in sources.readlines():
    copyimg.write(line)

# 3.刷新缓存与释放连接
copyimg.flush()
sources.close()
copyimg.close()

print("success")