# 导包
import pymysql
import traceback

# 1、连接数据库
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="cz_students",
    charset="utf8"
)

# 2、创建游标,可以传递参数
cursor = conn.cursor()


# 3、sql 创建表 user
def create_table():
    """创建表"""
    cursor.execute("DROP TABLE IF EXISTS cpvs7")
    sql = f"""
    create table cpvs7(
        id int auto_increment primary key comment "学号",
        name varchar(32) not null comment "姓名",
        age int default 18 comment "年龄"
    );
    """
    cursor.execute(sql)
    conn.commit()


def insert():
    """插入数据"""
    # sql = f"""insert into cpvs7 (name) values  ("张三"), ("李四"), ("王五");"""
    sql = f"""insert into cpvs7 (name) values  (%s), (%s), (%s);"""
    cursor.execute(sql, ("111", "222", "333"))
    conn.commit()


def query():
    """查询数据"""
    sql = """
    select 
        * 
    from 
        cz_s
    """
    cursor.execute(sql)
    res_tuple = cursor.fetchone()  # 获取一条数据
    print(res_tuple)
    res_tuple = cursor.fetchone()  # 获取一条数据
    print(res_tuple)
    # res_tuple = cursor.fetchmany(2)   # 获取多条数据
    # res_tuple = cursor.fetchall()  # 获取所有数据
    # print(res_tuple)  # tuple
    # for i in res_tuple:
    #     print(i)


def update():
    # sql = """update cpvs7 set age=19 where id=3; """
    # cursor.execute(sql)

    # 另一种写法
    sql = """update cpvs7 set age=%s where id=%s;"""
    cursor.execute(sql, (19, 2))
    conn.commit()


def main():
    # create_table()
    # insert()
    query()
    # update()
    cursor.close()
    conn.close()  # 关闭数据库连接


if __name__ == '__main__':
    main()
