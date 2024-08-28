"""
    数字序列
"""

# 数字序列
# Python中可以使用range（）函数返回一个数字序列
# range（n） return one [0,n)
# range（m,n） return one [m,n)
# range（m,n,s） return one [m,n,s)

# 示例
for i in range(10):
    print(i)

# 输出1-50之间所有偶数
for i in range(2, 51, 2):
    print(i)

for num in range(1, 51):
    if num % 2 == 0:
        print(num)
print("over")