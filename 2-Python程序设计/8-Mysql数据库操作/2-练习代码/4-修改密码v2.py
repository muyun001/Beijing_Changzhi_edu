import pymysql
import settings
import utils

conn, cursor = utils.get_cursor()
table_name = "cz_account"

def update_pwd():
    """
    1、键入用户名
    2、判断用户是否存在
        - 用户存在：
            - 输入原密码，判断愿密码是否正确
                - 如果原密码正确：
                    - 输入新的密码
                    - 再次输入新密码
                        - 如果两次密码相同：则修改密码
                        - 如果两次密码不相同，则重新输入密码
                - 如果原密码错误，则要求重新输入。
                （最多连续输错三次，达到3次的时候，就输出（"密码输错3次，请下次再尝试更改密码。"）， 程序退出！）
        - 用户不存在：
            - 直接输出（"没有此用户"）
    """
    # 1、键入用户名和密码
    user_name = input("请输入用户名：")

    # 查询此用户是否存在，以及原密码是否正确。
    query_user_sql = f"""
        select * from {table_name} where user_name = "%s"
        """ % user_name
    # 执行查询
    # print(query_user_sql)
    cursor.execute(query_user_sql)

    # 判断res是否有结果
    # 如果有结果：则说明用户存在
    if cursor.fetchone():
        # 如果用户存在：
        while True:
            pwd = input("请输入密码：")
            query_pwd_sql = f"""select * from {table_name} where user_name = '%s' and password = '%s'""" % (user_name, pwd)
            cursor.execute(query_pwd_sql)

            # 判断res是否有结果
            # 如果有结果：说明密码正确，则可以输入新的密码。
            if cursor.fetchone():
                while True:
                    new_pwd1 = input("请输入新密码：")
                    new_pwd2 = input("请再次输入新密码：")
                    if new_pwd1 == new_pwd2:
                        update_pwd_sql = f"""
                            update {table_name} set password = "%s" where user_name = "%s"
                            """ % (new_pwd1, user_name)
                        cursor.execute(update_pwd_sql)
                        print("密码修改成功！！！程序即将退出！")
                        # exit()
                        break
                    else:
                        print("两次密码不相同！！请重新输入！！")
                break
            else:
                print("密码错误！！ 请重新输入！")
            # 如果结果为空，则说明密码错误，要求用户重新输入密码。while循环/给一次输出错误的机会。
    else:
        # 如果结果为空：说明用户不存在
        print("没有此用户")


def main():
    update_pwd()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
