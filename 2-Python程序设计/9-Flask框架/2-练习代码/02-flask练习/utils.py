import pymysql

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


def read_from_mysql():
    sql = """
        select * from cz_s2;
        """
    cursor.execute(sql)
    res = cursor.fetchall()
    return res
