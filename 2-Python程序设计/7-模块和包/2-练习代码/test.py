db_type = input('(mysql/oracle)>>: ')
if db_type == 'mysql':
    import mysql as db
elif db_type == 'oracle':
    import oracle as db
else:
    print("输入错误")
    exit()
db.sqlparse()
db.connect()