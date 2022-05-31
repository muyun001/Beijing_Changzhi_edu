import pymysql
import settings


def get_cursor():
    """获取数据库游标"""
    conn = pymysql.connect(**settings.MYSQL_CONFIG)
    cursor = conn.cursor()
    return conn, cursor
