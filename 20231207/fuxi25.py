"""
    文件的拷贝
"""

# 打开文件
fr = open('fuxi25.txt', 'r', encoding='utf-8')
fw = open('fuxi25_copy.txt', 'w', encoding='utf-8')
# 循环遍历
for line in fr:
    # 写入一行
    fw.write(line)
    # 刷新
    fw.flush()
fr.close()
fw.close()