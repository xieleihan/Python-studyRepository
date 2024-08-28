-- 创建数据库
create database python charset utf8mb3;
-- 使用数据库
use python;
-- 创建表
create table students(
	id int primary key auto_increment,
    name varchar(20) not null,
    age int default 18,
    salary float default 5000.99
);
-- 插入数据
insert into students(name, age, salary) values ('张三', 22, 1000),
                                               ('李四', 33, 3000),
                                               ('王五', 28, 2000),
                                               ('赵六', 34, 5000),
                                               ('梅西', 37, 1000000),
                                               ('C罗', 38, 4000000),
                                               ('詹姆斯', 33, 88888),
                                               ('焦宁波', 18, 10000000000000);
-- 查询数据
select * from students;
select * from students where id = 1;
select * from students where name = '梅西';
update students set age = 38 where name = '梅西';



-- 创建表存储用户注册信息
create table users(
	id int primary key auto_increment,
    name varchar(20) not null,
    psw varchar(400) not null,
    udesc varchar(100) default "测试"
);

select * from users;
select md5('123456');
select sha('焦宁波');
select sha2('张胜男',0)

