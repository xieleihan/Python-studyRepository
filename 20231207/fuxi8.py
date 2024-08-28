"""
    随机生成一个1-10的随机数，给用户3次机会看是否可以猜中
"""

import random

target = random.randint(1, 10)
if int(input("请输入一个1-10的数字：")) == target:
    print("恭喜你，猜中了！1")
elif int(input("请输入一个1-10的数字：")) == target:
    print("恭喜你，猜中了！2")
elif int(input("请输入一个1-10的数字：")) == target:
    print("恭喜你，猜中了！3")
else:
    print(f"你输了，再接再厉！目标数字：{target}")