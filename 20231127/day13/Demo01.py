"""
    使用PyMySQL进行数据库数据的操作（CRUD）
    作者：jack
    日期：23.11.21


    1. 安装PyMySQL
    2. 导入
"""
import pymysql

def get_connection():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3366,
        db="python",
        user="root",
        password="root123456"
    )
    # conn = pymysql.Connection(
    #     host="127.0.0.1",
    #     port=3366,
    #     db="python",
    #     user="root",
    #     password="root123456"
    # )
    return conn

# 测试
# print(get_connection())

# 插入数据
def insert_data(name, age, salary):
    sql = f"insert into students(name, age, salary) values ('{name}', {age}, {salary})"
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute(sql)
    conn.commit()
    conn.close()
    return rows

# 修改数据
def update_data(id, name, age, salary):
    sql = f"update students set name='{name}', age={age}, salary={salary} where id={id}"
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute(sql)
    conn.commit()
    conn.close()
    return rows

def delete_data(id):
    sql = f"delete from students where id={id}"
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute(sql)
    conn.commit()
    conn.close()
    return rows

def query_all_data():
    query = "select * from students"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    all = cursor.fetchall()
    # print(all, type(all))
    conn.commit()
    conn.close()
    return all

def query_by_id(id):
    sql = f"select id, name, age, salary from students where id={id}"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    one = cursor.fetchone()
    conn.commit()
    conn.close()
    return one

one = query_by_id(5)
for col in one:
    print(col, end=" ")
print()



# all = query_all_data()
# for row in all:
#     for col in row:
#         print(col, end=" ")
#     print()

# rows = delete_data(1)
# if rows > 0:
#     print("删除成功")
# else:
#     print("删除失败")

# rows = update_data(1, "李四", 22, 20000.99)
# if rows > 0:
#     print("修改成功")
# else:
#     print("修改失败")


# rows = insert_data("张三",33, 10000.99)
# if rows > 0:
#     print("插入成功")
# else:
#     print("插入失败")

