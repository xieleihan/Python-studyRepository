"""
    写入文件
"""

# 1.打开文件
file = open("./hello.txt", mode="a", encoding="utf-8")

# 2.写数据
date = "\n1:this is my write data"
file.write(date)

# 3.写中文
date = "2:写入中文，我用goland"
file.write(date)

# 4.写入行
file.writelines("3:第一行\n4:第二行\n5:第三行")

# 5.刷新缓存
file.flush()
# 6.释放资源
file.close()

print("success")