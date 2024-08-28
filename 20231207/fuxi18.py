"""
    将列表【1，2，3，4，5，6，7，8，9，10】中的偶数元素存储到另一个列表
"""
# 数据列表
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 自定义函数
def get_even_num(data):
    # 定义一个空列表
    result = list()
    # 遍历数据列表
    for num in data:
        # 判断数据是否为偶数
        if num % 2 == 0:
            # 将偶数添加到结果列表中
            result.append(num)
    # 返回结果列表
    return result
# 调用函数
x = get_even_num(data)
# 输出结果
print(x)
# [2, 4, 6, 8, 10]