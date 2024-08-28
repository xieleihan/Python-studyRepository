import pymysql
class DB:
    @classmethod
    def get_connection_cursor(cls):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            port=3366,
            password='root123456',
            db='python',
            charset='utf8')
        # 获取游标
        cursor = conn.cursor()
        return conn, cursor
    @classmethod
    def close_connection_cursor(cls,conn, cursor):
        if cursor:
            cursor.close()
        if conn:
            conn.close()