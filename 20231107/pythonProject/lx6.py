class Staff:
    def __init__(self,id,name,dep,salary):
        self.id = id
        self.name = name
        self.dep = dep
        self.salary = salary
        print("已经创建一个员工对象，并且做了初始化")

    def work(self,time):
        if time > 8 and time < 18:
            if time >12 and time < 14:
                self.eat()
            else:
                print(f"我是员工：{self.name},我在划水")
        else:
            self.sleep()

    def eat(self):
        print(f"我是员工{self.name}吃饭")

    def sleep(self):
        print(f"我是员工{self.name}摸鱼")

s = Staff(1,"lvzhitian","it",10000)

s.work(12)

# 测试
for i in range(8,20):
    s.work(i)