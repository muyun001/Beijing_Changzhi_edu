import pymysql
import settings

"""
工具模块
"""
file_path = "files/hello.txt"
conn = pymysql.connect(**settings.MYSQL_CONFIG)


def read_file():
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(s):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(s)


def create_table():
    cursor = conn.cursor()
    sql = """
        
    """
    cursor.execute(sql)
    cursor.close()
