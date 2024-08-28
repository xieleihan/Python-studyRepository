# 空列表
result = list()
# 数据列表
list = [1,2,3,4,5,6,7,8,9,10]
# def自定义函数
def get_evev_list(list,result):
    for ele in list:
        if ele % 2 == 0:
            result.append(ele)
# 调用函数
get_evev_list(list,result)
# 输出
print(result)