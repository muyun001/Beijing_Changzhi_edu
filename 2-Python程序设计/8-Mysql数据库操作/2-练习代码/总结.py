"""
1.pymysql是第三方模块，使用之前确定是否安装 pip install pymysql
2.需要导入pymysql    import pymysql
3. 需要操作mysql 需要2步  a、连接数据库   b、创建执行游标
4.  使用游标进行 操作

注意事项:
    对数据进行增删改都需要事务提交。
    sql语句防止sql注入
pymysql对应的方法

conn = pymsql.connect()
# 通过连接创建游标,可以带参数，如何是查询，需要返回是字典pymysql.cursors.DictCursor
cursor = conn.cursor()
# 通过游标对象 执行sql和返回结果
cursor.fetchone()
cursor.fetchall()
cursor.rowcount --- 属性

# 提交事务
conn.commit()

# 关闭游标和关闭数据库连接
cursor.close()
conn.close()
"""