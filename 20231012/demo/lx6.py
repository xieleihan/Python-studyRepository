# 变量元组
tuple = ("java","python","cpp","goland")
print(tuple)
print(type(tuple))
# 嵌套元组
tuple = (("java","python"),("cpp","goland"))
print(tuple)
print(type(tuple))
# 元组嵌套列表
tuple = ("java",["python","cpp","goland"])
print(tuple)
print(type(tuple))
# 注意：定义只有一个元素的元组时该元素的后面必须加英文逗号，不然是字符串
tuple = ("java",)
print(tuple)
print(type(tuple))
tuple = ("java")
print(tuple)
print(type(tuple))