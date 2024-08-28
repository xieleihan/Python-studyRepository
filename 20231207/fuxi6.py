"""
    登录操作（简单）
"""

# 这个不能用于企业级
if input("请输入用户名：") == "admin" and input("请输入密码：") == "123456":
    print("登录成功")
else:
    print("登录失败")