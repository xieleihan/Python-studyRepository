"""
    使用python连接SQL操作 学习
    步骤解析：
    1.导入模块
    2.连接数据库，需要注意的是输入必要参数
    3.进行操作
    # 其实可以写一些其他的相关操作
"""

# 导入模块
import pymysql

# 连接数据库
def get_Connection():
    # 连接数据库
    conn = pymysql.connect(
        # host需要根据你的实际情况进行设置，比如本地的127.0.0.1或localhost，远程的192.168.1.100
        host='127.0.0.1',
        # 端口号 默认的是3306，但是我习惯性使用2280
        port=2280,
        # 用户名，默认root
        user='root',
        # 密码，我一般习惯使用password作为开发用，但是实际使用使用谷歌强加密密码
        password='password',
        # 数据库名,根据你使用情况去输入
        database='demo',
        # 字符编码，默认一般就是utf8，但是我推荐使用Unicode，因为它可以支持中文和外文字符
        charset='utf8'
    )
    # 返回连接对象
    return conn

# 测试
# print(get_Connection())

# 插入数据
def insert_data(name, age, salary):
    # 连接数据库
    conn = get_Connection()
    # 执行sql语句
    sql = f'insert into students(name,age,salary) values("{name}", {age}, {salary})'
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    nows = cursor.execute(sql)
    # 提交事务
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 返回影响行数
    return nows

# # 测试 插入数据
# text = insert_data('小明', 20, 10000)
# if text > 0:
#     print(f'insert success,影响了{text}行')
# else:
#     print('insert error')

# 更新数据
def update_data(id, name, age, salary):
    # 连接数据库
    conn = get_Connection()
    # 执行sql语句
    sql = f'update students set name="{name}", age={age}, salary={salary} where id={id}'
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    nows = cursor.execute(sql)
    # 提交事务
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 返回影响行数
    return nows

# # 测试 更新数据
# text = update_data(5, '小明', 20, 123)
# if text > 0:
#     print(f'update success,影响了{text}行')
# else:
#     print('update error')

# 删除数据
def delete_data(id):
    # 连接数据库
    conn = get_Connection()
    # 执行sql语句
    sql = f'delete from students where id={id}'
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    nows = cursor.execute(sql)
    # 提交事务
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 返回影响行数
    return nows

# # 测试 删除数据
# text = delete_data(6)
# if text > 0:
#     print(f'delete success,影响了{text}行')
# else:
#     print('delete error')

# 查询数据
def query_all_data():
    # 连接数据库
    conn = get_Connection()
    # 执行sql语句
    # * = id ,name ,age ,salary
    sql = f'select * from students'
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    cursor.execute(sql)
    # 获取查询结果，这里我们调用的是cursor里面的一个方法fetchall()，这个方法会把全部查询结果以元组的形式返回
    result = cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 返回行数
    return result

# # 测试 查询数据
# textlines = query_all_data()
# # 遍历所有的数据（下面是以元组嵌套元组的形式），元组确保了数据不会被修改，下面的循环把元组中的元组遍历出来
# for text in textlines:
#     # 下面的循环是把元组的元素遍历出来
#     for i in text:
#         print(i, end=' ')
#     print()

# 查询单行数据
def query_one_data(id):
    # 连接数据库
    conn = get_Connection()
    # 执行sql语句
    sql = f'select * from students where id={id}'
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    cursor.execute(sql)
    # 获取查询结果，这里我们调用的是cursor里面的一个方法fetchone()，这个方法会把其中一行查询结果以元组的形式返回
    result = cursor.fetchone()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # 返回行数
    return result

# # 测试 查询单行数据
# text = query_one_data(1)
# # 由于只是查询了一条数据，所以数据容器只有一个元组
# for i in text:
#     print(i, end=' ')
# print()