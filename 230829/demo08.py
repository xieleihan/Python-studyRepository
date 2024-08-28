"""
this is demo08,demo is type and look
"""
# 整数
age = 10
# 字符串
name = 'Jack'
# 小数
salary = 4500.3
# bool
isMarry = True

# print
print(name)

# many print
print("姓名：",name,"年龄：",age,"小数：",salary,"婚否：",isMarry)

# date type look
print(type(name),type(age),type(salary),type(isMarry))
print(type("Jack"),type(20),type(45000.4),type(True))

# 9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end='')
    print()

# 循环
for a in range(1,100):
    print(a,'\t')
    if a%10==0:
        print("\n")
