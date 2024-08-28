"""
    copy文件
"""

source = open(file="./hello.txt",mode="r", encoding="utf-8")
# 注意下面的双引号需要一个转义字符，不然会以为是字符串而不是路径
copy = open(file=r"C:\Users\Public\Desktop\copy.txt", mode="w", encoding="utf-8")

# 边读边写
for line in source.readlines():
    copy.write(line)

# 刷新缓存和释放
copy.flush()
source.close()
copy.close()

print("success")
