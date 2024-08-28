file = "./demo"
try:
    string = "hello"
    index = int(input("输入索引: "))
    print(string[index])
    filename = input("输入文件名: ")
    file = open(filename,mode="r", encoding="UTF-8")
    print(file.read())
except TypeError as e:
    print(e)
    print("类型错误")
except IndexError as e:
    print(e)
    print("索引越界")
except FileNotFoundError as e:
    print(e)
    print("指定的文件不存在")
finally:
    if file:
        file.close()
    else:
        print("errors")