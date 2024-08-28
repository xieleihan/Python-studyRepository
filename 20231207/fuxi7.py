"""
    月份季节的练习
"""

# 对输入的月份进行输出对应的季节
mouth = int(input("请输入月份："))
if mouth == 1 or mouth == 2 or mouth == 12:
    print("该月份为春季")
elif mouth == 3 or mouth == 4 or mouth == 5:
    print("该月份为夏季")
elif mouth == 6 or mouth == 7 or mouth == 8:
    print("该月份为秋季")
elif mouth == 9 or mouth == 10 or mouth == 11:
    print("该月份为冬季")
else:
    print("输入的月份有误")