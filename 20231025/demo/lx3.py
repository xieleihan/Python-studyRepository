# 导入模块
import os

# 获取指定文件的绝对路径
abspath = os.path.abspath("001-os模块.py")
print(abspath)
# 获取路径中的文件名部分
file_name = os.path.basename(abspath)
print(file_name)
# 获取路径中文件夹部分
file_dir = os.path.dirname(abspath)
print(file_dir)
# 判断路径是否存在
is_exist = os.path.exists(abspath)
print(is_exist)
# 判断是否是文件
print(os.path.isfile(abspath))
# 判断是否是目录
print(os.path.isdir(abspath))