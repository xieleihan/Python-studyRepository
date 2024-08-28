"""
    类成员和实例成员
"""
class Student:
    id = 10
    name = "jack"
    def __init__(self,city,salary):
        self.city = city
        self.salary = salary

    @classmethod
    def class_method(cls):
        print("class_method")

    def instance_method(self):
        print("instance_method")

# 类成员
print(Student.id,Student.name)
Student.class_method()
# 实例成员
stu = Student("Hong Kong",10000)
print(stu.id,stu.name,stu.city,stu.salary)
stu.instance_method()