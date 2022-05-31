# !/usr/bin/python3
import pymysql
# 隐藏密码模块
import getpass


class ActionMysql:
    def __init__(self, host, user, password, database, port=3306, charset='utf8'):
        # 打开数据库连接
        self.conn = pymysql.connect(
            host=host,  # 本地为localhost
            port=port,  # 端口号
            user=user,  # 账号
            password=password,  # 密码
            database=database,
            charset=charset)  # 数据库名
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self, sql):
        """
        执行查询，返回一条数据
        """
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            return res
        except Exception as e:
            print("fetch_one error:", e)
            return None

    def safe_fetch_one(self, sql, params):
        """
        防止sql注入的方法
        """
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchone()
        except Exception as e:
            print("safe_fetch_one error:%s" % e)
            return None

    def find_exists(self, sql):
        """
        执行查询返回结果是否存在
        """
        try:
            self.cursor.execute(sql)
            row_count = self.cursor.rowcount
            # 判断查询结果是否大于0
            if row_count:
                return True
        except Exception as e:
            print("fetch_one error:", e)
        return False

    def __del__(self):
        """
        执行数据库连接删除操作
        """
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    # 实例化mysql操作对象
    my_mysql = ActionMysql()
    while True:
        user_name = input("账号>>>")
        # pwd = input("密码>>>")
        # 调用隐藏密码模块 ,在pycharm的IDE中无效
        pwd = getpass.getpass("pwd>>>")
        #sql = 'select * from user where user_name="%s" and pwd="%s"' % (user_name, pwd)
        sql = 'select * from user where user_name=%s and pwd=%s'
        if my_mysql.safe_fetch_one(sql, (user_name, pwd)):
            print('登录成功，欢迎', user_name)
            break
        else:
            print('登录失败重新登录')
