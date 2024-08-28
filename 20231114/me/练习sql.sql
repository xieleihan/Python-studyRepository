-- 创建数据库
create database python;

-- 这里调用自己的数据库
use python;

-- 创建表
create table students(
	ID int primary key auto_increment,
    Name varchar(20) not null,
    Python float default 50.0,
    Java float default 60.0,
    C float default 0.0
);

-- 插入数据
insert into students(Name,Python,Java,C) values ("张三",90.5,60,55),
("李四",100,88,66),
("王五",77,58,43)
;

-- 查询数据
select * from students;
select Name,Python from students;
select ID,Name,Python from students where Python >=80;

-- 更新数据
update students set C = 60 where ID=1;

-- 删除数据
delete from students where id =3;

-- 删除全部数据
truncate table students;