"""
    封装
"""
class Teacher:
    # 封装属性
    __id_card = "4542164641164"
    # 封装方法
    def __verify_edu(self):
        print("验证教师资格")
    # 封装的信息是内部其他方法使用的
    def entry_work(self):
        self.__verify_edu()
        print(self.__id_card)
        print("input")

# 创建对象
teacher = Teacher()
# 访问封装信息出错
# print（teacher.__id_card）
# 访问封装方法出错
# teacher.__verify_edu()
# 调用公开方法
teacher.entry_work()