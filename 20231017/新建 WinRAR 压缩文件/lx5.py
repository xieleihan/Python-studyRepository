"""
    读取文件
"""

# 1.打开文件
file = open("./text.txt" , mode="r")

# 2.读取
print(file.read())

# 3.读一行数据
# print(file.readline())
# print(file.readline())
# print(file.readline())
# 这个地方要注意，如果上面全读完，下面就读不到数据，因为，指针会移出有数据的地方

# 4.读数据
print(file.readlines())

# 5.遍历
for line in file.readlines():
    print(line , end=" ")
print()

# 读数据的时候，跳过几个
file.seek(6)
print(file.read(6))
