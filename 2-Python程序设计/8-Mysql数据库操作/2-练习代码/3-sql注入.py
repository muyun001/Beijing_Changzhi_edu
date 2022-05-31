import pymysql
import settings

conn = pymysql.connect(**settings.MYSQL_CONFIG)
cursor = conn.cursor()

# 1、先了解两个简单【永远都成立】的sql语句
sql = "select * from cz_s2 where 1=1;"
sql = "select * from cz_s2 where 1=1 or '';"

# 2、想要的结果
# name = "崔昊元"
# sql = "select * from cz_s2 where name = '崔昊元';"
# sql = "select * from cz_s2 where name = '%s';" % name
# cursor.execute(sql)
# result = cursor.fetchall()
# for row in result:
#     print(row)


# 3、但是sql被人篡改之后
name = "崔昊元" + "' or 1 = 1 or '"
sql = "select * from cz_s2 where name = '%s';" % name  # select * from cz_s2 where name = '崔昊元' or 1 = 1 or '';
print(sql)

cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
conn.close()
