import pymysql
import settings

conn = pymysql.connect(**settings.MYSQL_CONFIG)
cursor = conn.cursor()

# sql = f"""
# select * from {settings.TABLE_NAME};
# """

# sql = f"""
# select * from {settings.TABLE_NAME} where id=1;
# """

# sql = f"""
# select * from {settings.TABLE_NAME} where 1=1;
# """

# sql = f"""
# select * from {settings.TABLE_NAME} where name="崔昊元";
# """

# sql = f"""
# select * from {settings.TABLE_NAME} where name="崔昊元" or age=18;
# """
# sql = f"""
# select * from {settings.TABLE_NAME} where name="崔昊元" or 1=1;
# """

# name = "崔昊元"
# sql = f"""
# select * from {settings.TABLE_NAME} where name='%s';
# """ % name

# name = '"崔昊元" or 1=1'
# sql = f"""
# select * from {settings.TABLE_NAME} where name=%s;
# """ % name

# print(sql)

# cursor.execute(sql)
# res = cursor.fetchall()
# for r in res:
#     print(r)

# 防止sql注入
name = '崔昊元'
age = '18'
# name = '"崔昊元" or 1=1'
sql = f"""
select * from {settings.TABLE_NAME} where name=%s;
"""
# cursor.execute(sql, name)
cursor.execute(sql, (name, age))


# sql = f"""
# select * from {settings.TABLE_NAME} where name=%s or age = %s;
# """
# cursor.execute(sql, [name, age])
res = cursor.fetchall()
for r in res:
    print(r)


cursor.close()
conn.close()
