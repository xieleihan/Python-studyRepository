"""
    文件读写
"""
with open("test.txt","r",encoding="UTF-8") as file:
    data = file.read()
    print(data)
with open("test.txt","r",encoding="UTF-8") as file:
    line = file.readline()
    print(line)
with open("test.txt","r",encoding="UTF-8") as file:
    lines = file.readlines()
    print(lines)