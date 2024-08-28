"""
    数据库连接
"""

from pymysql import Connection
# 获取数据库连接
conn = Connection(
    host='localhost',
    port=2280,
    user='root',
    password='password',
    db='python',
    charset='utf8'
)
# 打印对象
print(conn)
# 获取主机信息
print(conn.get_host_info())
# 获取数据库版本
print(conn.get_server_info())
# 关闭连接
conn.close()