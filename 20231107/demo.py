"""
    网络爬虫演示
    分析：
    1.导入对应的包，下面需要用到的有request，pyquery，json（json是标准的）
    2.获取请求
    3.查找数据
    4.清洗数据
    5.保存数据
    Warning：该演示仅作为学习使用，严格遵守中华人民共和国法律法规，不作为任何商业和非法行为，所有数据在学习过后删除。
"""

# 导入包
# 需要注意的是requests和pyquery是第三方包，需要安装
import requests
import pyquery
import json
import pymysql
import urllib.parse

# 数据库连接，游标
def get_connect():
    # 连接数据库
    conn = pymysql.connect(
        host='localhost',
        port=2280,
        user='root',
        password='password',
        db='city',
    )
    # 获取游标
    cursor = conn.cursor()
    return conn, cursor

# 关闭数据库连接和游标
def close_connect(conn, cursor):
    # 关闭游标
    if cursor:
        cursor.close()
    # 关闭数据库连接
    if conn:
        conn.close()

# 让用户输入自己需要的城市
city_name = input('请输入你要爬取的城市名称：')

# 构造cookies
cookies = {
    # quote()函数可以把字符串转成url编码
    # unquote()函数可以把url编码转成字符串
    "city_name" : urllib.parse.quote(city_name)
}

# 定义url
url = 'https://www.dongchedi.com/sales'

# 发送get请求，获取页面
res = requests.get(url, cookies=cookies)

# 测试
print(res, type(res))
# 页面响应请求判断
if res.status_code == 200:
    print(url)
    print('请求成功')
    html = res.text
    # 把网页请求的页面html源码给保存下来
    with open('./dongchedi.html', 'w', encoding='utf-8') as f:
        f.write(html)
    # 对该页面的数据进行查找
    query = pyquery.PyQuery(html)
    # 调用方法，获取对应class类的相应内容
    lis = query.find(".hot-sales-rank_item__UZthc")
    # print(lis, type(lis))
    # 设置数据容器为字典，来存放爬虫读取的数据
    datas = []
    # 遍历
    for item in lis.items():
        num = item.find(".hot-sales-rank_item-rank__1r1pX").text()
        # 这里需要注意并集选择器
        name = item.find(".hot-sales-rank_item-info-title__JSnDI.line-1").text()
        price = item.find(".hot-sales-rank_item-info-price__2Gbyg").text()
        cost = item.find(".hot-sales-rank_item-sales-volume__19dk3").text()
        # 打印测试
        # print(num, name, price, cost)
        # 封装数据
        car = {
            'num': num,
            'name': name,
            'price': price,
            'cost': cost
        }
        datas.append(car)
    for car in datas:
        print(car)
    # 存储数据
    string_data = json.dumps(datas, ensure_ascii=False)
    # print(string_data)
    with open('./dongchedi.json', 'w', encoding='utf-8') as f:
        f.write(string_data)

    # 数据库的表数据
    # -- 创建表
    # create table demo(
    # 	id int primary key auto_increment,
    #     city varchar(20) not null,
    #     num int not null,
    #     name varchar(100) not null,
    #     price varchar(100) not null,
    #     cost int not null
    # );

    #连接数据库
    conn, cursor = get_connect()
    # 把数据传入数据库里面的表
    for car in datas:
        sql = 'insert into demo(city, num, name, price, cost) values (%s, %s, %s, %s, %s)'
        cursor.execute(sql, (city_name, car['num'], car['name'], car['price'], car['cost']))
        conn.commit()
    # 关闭连接
    close_connect(conn, cursor)
    # success
    print('input database success')

else:
    print('请求失败')
