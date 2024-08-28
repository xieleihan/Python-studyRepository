"""
    break and continue 关键字
"""

# break 关键字
# break 关键字的作用是跳出当前循环，结束循环。
for i in range(10):
    if i == 5:
        break
    print(i)

# continue 关键字
# continue 关键字的作用是跳过当前循环，继续下一次循环。
for i in range(10):
    if i == 5:
        continue
    print(i)