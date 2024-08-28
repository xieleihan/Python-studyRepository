# 定义while循环来遍历列表里的元素
def list_element_print_while(list):
    index = 0
    while index < len(list):
        element = list[index]
        print(f"{list[index]}", end='')
        index += 1
    print()

# 定义for循环遍历列表元素的函数（元素）
def list_element_print_for(list):
    for ele in list:
        print(f"{ele}" , end='')
    print()

# 定义for循环遍历列表元素的函数（索引）
def list_element_print_for_index(list):
    for index in range(len(list)):
        ele = list[index]
        print(f"{ele}" , end='')
    print()

# 列表
list = ["java","python","cpp","goland"]
# 调用while循环函数
list_element_print_while(list)
# 调用for循环函数（元素）
list_element_print_for(list)
# 调用for循环遍历列表函数（索引）
list_element_print_for_index(list)