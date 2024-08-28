# 自定义函数
def str_len(str):
    count = 0
    for ch in str:
        count += 1
    return count
str01 = "time is monny"
str02 = "all for one,one for all"
str03 = "he laughs best who laugh last"
print(f"{str01}的长度：{len(str01)}")
print(f"{str02}的长度：{len(str02)}")
print(f"{str03}的长度：{len(str03)}")