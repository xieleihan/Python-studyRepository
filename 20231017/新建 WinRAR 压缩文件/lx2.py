# 字符串定义
str01 , str02 , str03 , str04 = 'javascript',"python","""css""",'''html'''
str05 = str("markdown")
print(str01,str02,str03,str04,str05)
print(type(str01),type(str02),type(str03),type(str04),type(str05))

# 常用方法
string = "hello world"

#获取字符串长度和指定字符出现的字数
print(len(string))
print(string.count('o'))

# 单词首字母大小写，全部大写，全部小写
print(string.capitalize())
print(string.upper())
print(string.lower())
print(string.swapcase())

# 数字转字符（ASCLL）
print(chr(97))
print(ord('a'))

# 字节串
bs = b"ABCD"
print(bs, type(bs))
print(bs[0])

# 中文
string = "人生苦短 我用Goland"
encode = string.encode("utf8")
print(encode)
decode = encode.decode("utf8")
print(decode)

# 去除左右空格
string = " java "
print(string.strip())
print(string.lstrip())
print(string.rstrip())

# 索引访问
string = "hello world"
print(f"{string[0]},{string[1]}")

# 返回索引
string = "hello world"
print(f"{string.index('l')},{string.rindex('l')}")

# 替换：replace（旧串，新串）
string = "hello world"
print(f"{string.replace('l','h')},{string.replace('l','h',1)}")

# 切割:split（指定分隔符）
string = "hello world"
print(f"{string.split('l')},{string.split('l',1)}")
print(f"{string.split('l',2)}")
print(f"{string.split('l',-1)}")

# 切片
string = "hello world"
print(f"{string[0:5]},{string[5:]}")

# 遍历
string = "hello world"
for i in string:
    print(i, end=" ")
print()

# 拼接
print("-".join(["hello", "world"]))
print(",".join(("hello", "world")))
print("jack"+ str(30)+str(True))

# 原始字符串：raw
path = "c:\\program_files\\works\\python\\set.py"
print(path)
path = r"c:\program_files\works\python\set.py"
print(path)

# 敏感词过滤
# 定义敏感词
not_words = ["tmd","sb"]
content = input("评论：")

# 过滤函数
def filter_content(words,string):
    for w in words:
        string = string.replace(w,"*")
    return string

print(f"过滤前：{content}")
result = filter_content(not_words,content)
print(f"过滤后：{result}")