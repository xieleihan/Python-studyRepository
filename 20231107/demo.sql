-- 创建数据库
create database city;
-- 使用数据库
use city;
-- 创建表
create table demo(
	id int primary key auto_increment,
    city varchar(20) not null,
    num int not null,
    name varchar(100) not null,
    price varchar(100) not null,
    cost int not null
);

-- 查询数据
select * from demo;