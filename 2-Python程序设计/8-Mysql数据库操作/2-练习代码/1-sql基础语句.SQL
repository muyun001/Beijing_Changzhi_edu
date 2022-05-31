-- 命令行进入数据库
/*
要求：数据库服务器是打开状态
mysql -u用户名 -p密码
如：mysql -uroot -p123456
*/


-- 创建数据库
-- create database cz_students if not exists default character set "utf8";

-- 查看所有数据库
show databases;

-- 使用user_system数据库进行操作
use user_system;

-- 查看所有数据表
show tables;

-- 数据类型
/*
tinyint:微整型数值
int：整型
bigint:大整型
float:浮点型
text:文本类型
longtext:长文本类型
date:日期类型
datetime:日期时间类型
*/

-- 创建表
create table cz_students
(
    id          int         not null primary key auto_increment comment "id",
    name        varchar(32) not null comment "姓名",
    age         tinyint     not null default 17 comment "年龄",
    gender      tinyint     not null default 1 comment "性别：1男生，2女生",
    create_time datetime             default now() comment "创建时间",
    update_time datetime             default now() comment "更新时间"
);

-- 删除表
drop table cz_students;

/*
增删改查
crud:create\read\update\delete
*/

-- 添加数据
-- 1、一次添加一条数据
insert into cz_students(`name`, `age`, `gender`)
values ("崔昊元", 18, 2);
-- 2、一次性添加多条数据
insert into cz_students(`name`, `age`, `gender`)
values ("牛皓冬", 18, 1),
       ("贾靖程", 17, 2),
       ("王孝天", 18, 1),
       ("陈观绅", 18, 1);

-- 删除数据
delete
from cz_students
where `id` = 1;

-- 改
update cz_students
set age        = 19,
    update_time=now()
where name = "陈观绅";

-- 查询
-- 查询所有信息
select *
from cz_students;

-- 查询所有女生的信息
select *
from cz_students
where gender = 2;

-- 查询所有人的姓名、年龄
select name, age
from cz_students;

-- 查询女生的姓名、年龄
select name, age
from cz_students
where gender = 2;

-- 查询数据有多少条
select count(id)
from cz_students;

/*
第一张表：cz_group  【存储分组信息的表】
id\group_name\num\create_time\update_time
id、组名、人数、创建时间、更新时间

第二张表：cz_students   【存储学生信息的表】
id\name\age\gender\hobby\birthday\email\tel\face\nick_name\group_id\create_time\update_time
id、姓名、年龄、性别、兴趣爱好、生日、邮箱、手机、头像、昵称、分组的id、创建时间、更新时间

第三张表：cz_account    【存储账户信息的表】【要求：此表的用户名和students表的昵称是相同的，密码统一为123456】
id\student_id\user_name\password\create_time\update_time
id、用户id、用户名、密码、创建时间、更新时间
*/


create table cz_group
(
    id          tinyint     not null auto_increment primary key comment "id",
    group_name  varchar(64) not null comment "组名",
    num         int         not null default 0 comment "组内人数",
    create_time datetime             default now() comment "创建时间",
    update_time datetime             default now() comment "更新时间"
);

insert into cz_group(`group_name`)
values ("第一组"),
       ("第二组"),
       ("第三组"),
       ("第四组");



# create table cz_students2
# (
#     id          int         not null primary key auto_increment comment "id",
#     name        varchar(32) not null comment "姓名",
#     age         tinyint     not null default 17 comment "年龄",
#     gender      tinyint     not null default 1 comment "性别：1男生，2女生",
#     group_id    tinyint     not null comment "组id",
#     create_time datetime             default now() comment "创建时间",
#     update_time datetime             default now() comment "更新时间"
# );
#
# insert into cz_students2(`name`, `age`, `group_id`, `gender`)
# values ("牛皓冬", 18, 3, 1),
#        ("贾靖程", 17, 3, 2),
#        ("王孝天", 18, 2, 1),
#        ("陈观绅", 18, 4, 1);

-- 连表查询
select *
from cz_students2 as cs2
         left join cz_group cg on cg.id = cs2.group_id
where cg.group_name = "第三组";

create table cz_students.cz_account
(
    id          INT NOT NULL PRIMARY KEY auto_increment COMMENT "id",
    student_id  INT COMMENT "用户id",
    user_name   VARCHAR(20) COMMENT "用户名",
    password    VARCHAR(50) COMMENT "密码",
    creat_time  datetime DEFAULT NOW() COMMENT "创建时间",
    update_time datetime DEFAULT NOW() COMMENT "更新时间"
);

insert ignore into cz_students.cz_account
    (`student_id`, `user_name`, `password`)
values (1, "admin", 123456),
       (2, "admin", 123456),
       (3, "admin", 123456),
       (4, "admin", 123456),
       (5, "admin", 123456);

-- 连表查询
# alter table cz_s add group_id tinyint comment "分组id";
select *
from cz_s as cs
left join cz_group as cg on cs.group_id = cg.id
left join cz_account as ca on cs.id = ca.student_id;

-- 查看"第一组"人员的所有用户名和密码
# select cs.id,cs.name,ca.user_name,ca.password
# from cz_s as cs
# left join cz_group as cg on cs.group_id = cg.id
# left join cz_account as ca on cs.id = ca.student_id
# where cg.group_name="第一组";
#
#
# select cs.id,cs.name,ca.user_name,ca.password
# from cz_s as cs
# left join cz_group as cg on cs.group_id = cg.id
# left join cz_account as ca on cs.id = ca.student_id
# where cg.group_name="第一组";

select * from cz_s;
select * from cz_students.cz_group;
select * from cz_students.cz_account;
/*
题目：
查看"styles"组的所有成员的学号（id）、姓名、用户名、密码。
*/

/*
id、姓名：学生表（cz_s）
用户名、密码：账户表（cz_account）
"styles"组：分组表（cz_group）
*/

-- 学生表的group_id  <--> 分组表的id
-- 学生表的id  <--> 账户表的student_id

-- 通过left join写
select s.id, s.name, a.user_name, a.password
from cz_students.cz_s as s
left join cz_students.cz_group as g on s.group_id = g.id
left join cz_students.cz_account as a on s.id = a.student_id
where g.group_name="叶原枫";

-- 查询"叶原枫"组成员的所有信息
select
    *
from
     cz_s as s,
     cz_group as g,
     cz_account as a
where
    s.group_id = g.id
and s.id = a.student_id
and g.group_name="叶原枫";

-- 查询"叶原枫"组成员的id、姓名、用户名、密码、年龄、性别
select
    s.id,
    s.name,
    a.user_name,
    a.password,
    s.age,
    s.gender
from
     cz_s as s,
     cz_group as g,
     cz_account as a
where
    s.group_id = g.id
and s.id = a.student_id
and g.group_name="叶原枫";






# create database aaa;
# create table aaa(
#
# );
/*
数据库、数据表
数据库是可以包含多个数据表的。
*/


/*
创建表：
create table table_name(
    id int,
    name varchar(32),
    age int,
);
*/

create table cpvs(
    id int,
    name varchar(32),
    age int
);

-- 插入数据
insert into cpvs
    (id, name, age)
values
       (1, "zhangsan", 18),
       (2, "lisi", 18),
       (3, "wangwu", 18),
       (4, "zhoaliu", 18);

/*
主键：
外键：
*/

create table cpvs1(
    id int auto_increment primary key ,
    name varchar(32),
    age int
);

-- 插入数据
insert into cpvs1
    (name, age)
values
       ("zhangsan", 18),
       ("lisi", 18),
       ("wangwu", 18),
       ("zhoaliu", 18);


create table cpvs2(
    id int auto_increment primary key ,
    name varchar(32),
    age int default 18
);

-- 插入数据
insert into cpvs2
    (name)
values
       ("zhangsan"),
       ("lisi"),
       ("wangwu"),
       ("zhoaliu");

insert into cpvs2
    (name, age)
values
       ("wangermazi", 19);





create table cpvs3(
    id int auto_increment primary key comment "学号",
    name varchar(32) comment "姓名",
    age int default 18 comment "年龄"
);

-- 插入数据
insert into cpvs3
    (name)
values
       ("zhangsan"),
       ("lisi"),
       ("wangwu"),
       ("zhoaliu");

desc cpvs3;
desc cpvs2;


create table cpvs4(
    id int auto_increment primary key comment "学号",
    name varchar(32) comment "姓名",
    age int default 18 comment "年龄"
);

-- 插入数据
insert into cpvs10
    (name)
values
       ("zhangsan"),
       ("lisi"),
       ("wangwu"),
       ("zhoaliu");

insert into cpvs4
    (name)
values
       (null);

desc cpvs3;
desc cpvs2;



create table cpvs5(
    id int auto_increment primary key comment "学号",
    name varchar(32) not null comment "姓名",
    age int default 18 comment "年龄"
);

-- 插入数据
-- not null  仅仅是不能为null
insert into cpvs5
    (name)
values
      (null);

desc cpvs5;


create table cpvs6(
    id int auto_increment primary key comment "学号",
    name varchar(32) not null comment "姓名",
    age int default 18 comment "年龄"
);

show variables like '%autocommit%';