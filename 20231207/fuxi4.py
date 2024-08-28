"""
    基础语法练习
"""

# 下面主要是对输入的三门成绩进行求和和求平均
name = input("请输入你的名字：")
chinese = int(input("请输入你的语文成绩："))
math = int(input("请输入你的数学成绩："))
english = int(input("请输入你的英语成绩："))
# 格式化先打印
print("你好，%s，你的语文成绩是：%d，数学成绩是：%d，英语成绩是：%d" % (name, chinese, math, english))
# 计算平均分
average = (chinese + math + english) / 3
print("你的平均分是：%.2f" % average)
# 计算总分
total = chinese + math + english
print("你的总分是：%d" % total)
# 全部打印
print("你好，%s，你的语文成绩是：%d，数学成绩是：%d，英语成绩是：%d，你的平均分是：%.2f，你的总分是：%d" % (name, chinese, math, english, average, total))