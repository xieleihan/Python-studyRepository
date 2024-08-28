import DB
class User:
    @classmethod
    def register(cls,name, psw, udesc):
        conn, cursor = DB.DB.get_connection_cursor()
        sql = f"insert into users(name, psw, udesc) values('{name}', md5('{psw}'), '{udesc}') "
        try:
            rows = cursor.execute(sql)
            conn.commit()
            if rows > 0:
                print('注册成功')
            else:
                print('注册失败')
        except Exception as e:
            print(e)
            conn.rollback()
            print('注册失败')
        finally:
            DB.DB.close_connection_cursor(conn, cursor)
    @classmethod
    def login(cls,name, psw):
        sql = f"select * from users where name='{name}' and psw = md5('{psw}')"
        conn, cursor = DB.DB.get_connection_cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        conn.commit()
        DB.DB.close_connection_cursor(conn, cursor)
        if result:
            print("登录成功")
        else:
            print("登录失败")
    @classmethod
    def main_ui(cls):
        while True:
            print("-----------欢迎使用焦宁波的系统-------------------")
            print("----1、注册   2、登录    3、退出------------------")
            print("----------------------------------------------")
            choice = int(input("请输入你的选择："))
            if choice == 1:
                name = input("请输入用户：")
                psw = input("请输入密码：")
                udesc = input("请输入描述：")
                cls.register(name, psw, udesc)
            if choice == 2:
                name = input("请输入用户：")
                psw = input("请输入密码：")
                cls.login(name, psw)
            if choice == 3:
                print("退出系统")
                break