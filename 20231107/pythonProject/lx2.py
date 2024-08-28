# 定义学生类
class Student:
    # 成员变量
    name = None
    # 成员方法
    def say_hi(self):
        print(f"Hello, I am{self.name},happy")

# 创建类对象
stu1 = Student()
stu1.name = "lvzhitian"
stu1.say_hi()

# 创建类对象第二个
stu2 = Student()
stu2.name = "lvzhitian2"
stu2.say_hi()