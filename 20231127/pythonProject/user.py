"""
    这是一个模拟用户登录注册的python
"""

# 导入模块
import pymysql
import os

# 创建数据库连接
def create_connection():
    """
        创建数据库连接
    """
    # 连接数据库
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='password',
        database='demo',
        charset='utf8'
    )
    # 创建游标
    cursor = conn.cursor()
    # 返回连接
    return conn, cursor

# 关闭数据库连接和关闭游标
def close_connection(conn, cursor):
    # # 关闭游标
    # cursor.close()
    # # 关闭连接
    # conn.close()
    # 得判断是否为关闭才行
    if cursor:
        cursor.close()
    if conn:
        conn.close()

# 用户注册=数据库插入一条新值
def register(acc,psw,udess):
    # 定义sql语句
    sql = f'insert into user(acc,psw,udess) values ("{acc}",md5("{psw}"),"{udess}")'
    conn, cursor = create_connection()
    try:
        # 执行sql语句
        nows = cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        # 注册成功
        if nows > 0:
            os.system('cls')
            print("register success")
        # 注册失败
        else:
            os.system('cls')
            print("register fail")
    except Exception as e:
        print(e)
        conn.rollback()
        # 注册失败
        os.system('cls')
        print("register fail")
    finally:
        # 关闭数据库连接和关闭游标
        close_connection(conn, cursor)

# 用户登录=数据库查询一条值
def login(acc,psw):
    # 定义sql语句
    sql = f'select * from user where acc="{acc}" and psw=md5("{psw}")'
    conn, cursor = create_connection()
    # 执行sql语句
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchone()
    # 提交
    conn.commit()
    # 关闭连接和游标
    close_connection(conn, cursor)
    # 登录成功
    if result:
        os.system('cls')
        print("login success")
    # 登录失败
    else:
        os.system('cls')
        print("login fail")

# 用户注销=数据库删除一条值
def logout(acc):
    # 定义sql语句
    sql = f'delete from user where acc="{acc}"'
    conn, cursor = create_connection()
    # 执行sql语句
    nows = cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
    # 注销成功
    if nows > 0:
        os.system('cls')
        print("logout success")
    # 注销失败
    else:
        os.system('cls')
        # 回滚
        conn.rollback()
        print("logout fail")

# 重置密码=数据库更新一条值
def reset_password(acc,psw,udess):
    # 查询acc对应的udess
    sql1 = f'select udess from user where acc="{acc}"'
    conn, cursor = create_connection()
    # 执行sql语句
    level = cursor.execute(sql1)
    conn.commit()
    # 对输入的udess和数据库中的udess进行比对
    if level != 0:
        sql = f'update user set psw=md5("{psw}") where acc="{acc}"'
        nows = cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        # 重置成功
        if nows > 0:
            os.system('cls')
            print("reset success")
        # 重置失败
        else:
            os.system('cls')
            # 回滚
            conn.rollback()
            print("reset fail")
    else:
        os.system('cls')
        print("鉴权失败")


# 用户操作页面
def main_ui():
    while True:
        print("==========user ui============")
        # 1.注册 2.登录 3.重置密码 4.注销 5.退出
        print("=====1.register 2.login======")
        print("=====3.remove password=======")
        print("======== 5.exit==============")
        print("=============================")
        choice = int(input("please input your choice:"))
        if choice == 1:
            acc = input("please input your acc:")
            psw = input("please input your psw:")
            udess = input("please input your udess:")
            register(acc,psw,udess)
        if choice == 2:
            acc = input("please input your acc:")
            psw = input("please input your psw:")
            login(acc,psw)
        if choice == 3:
            acc = input("please input your acc:")
            psw = input("please input your psw:")
            udess = input("please input your udess:")
            reset_password(acc,psw,udess)
        if choice == 5:
            print("exit system")
            os.system("cls")
            break

main_ui()