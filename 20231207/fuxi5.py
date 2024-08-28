"""
    分支语句
"""

# if 语句
age = input("请输入你的年龄：")
age = int(age)
if age <= 18:
    print("未成年")
elif age < 30:
    print("青年")
elif age < 50:
    print("中年")
else:
    print("老年")