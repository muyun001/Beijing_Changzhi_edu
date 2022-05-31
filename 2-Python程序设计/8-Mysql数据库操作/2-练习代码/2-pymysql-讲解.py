# 1、导包
import pymysql
import settings

# 2、创建连接
conn = pymysql.connect(**settings.MYSQL_CONFIG)

# 3、创建游标
cursor = conn.cursor()

# 4、执行sql语句
# sql = """
#     use cz_students;
# """
# cursor.execute(sql)

def create():
    sql = """
    create table cpvs10(
        id int auto_increment primary key ,
        name varchar(32),
        age int
    );
    """
    cursor.execute(sql)

def insert():
    sql = """
        insert into cpvs10
            (name)
        values
           ("zhangsan"),
           ("lisi"),
           ("wangwu"),
           ("zhoaliu");
       """
    cursor.execute(sql)

def update():
    sql = """
    update cpvs10 set age=20 where id = 3;
    """
    cursor.execute(sql)

def delete():
    sql = """
    delete from cpvs10 where id=4;
    """
    cursor.execute(sql)

def query():
    sql = """select * from cpvs10;"""
    cursor.execute(sql)
    # result = cursor.fetchall()  # 一次查询所有数据
    # for r in result:
    #   print(r)

    # result = cursor.fetchone()  # 一次查询一条数据
    # print(result)
    # result = cursor.fetchone()  # 一次查询一条数据
    # print(result)

    result = cursor.fetchmany(5)
    for r in result:
        print(r)

def main():
    # create()
    # insert()
    # update()
    delete()
    query()

    # # 关闭数据连接和游标连接
    conn.close()
    cursor.close()


if __name__ == '__main__':
    main()