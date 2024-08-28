"""
    使用for循环实现九九乘法表的输出
"""

# 外层循环控制行
for i in range(1, 10):
    # 内层循环控制列
    for j in range(1, i+1):
        # 输出九九乘法表
        print(f"{j}*{i}={j*i}\t", end=" ")
    print()