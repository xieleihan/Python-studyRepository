"""
    跑步练习
"""

day = 1
# 外层循环
while day <= 7:
    print(f"周{day}跑步")
    distance = 1
    # 内层循环
    while distance <= 5:
        print(f"第{distance}公里", end=" ")
        distance += 1
    day += 1
    print()
print("跑步结束")