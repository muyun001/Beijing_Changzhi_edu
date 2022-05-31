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

    """
    先把【意外情况】写在前面，并处理掉。
    
    if a:
        print(0)
        if b:
            print(00)
            if c:
                print(000)
                if d:
                    print(0000)
                else:
                    print(0001)
            else:
                if e:
                    print(0000)
                else:
                    print(0001)
        else:
            print(01)
    else:
        print(1)
    ----------------------    
        
    if not a:
        print(1)
        return
        
    print(0)
    if not b:
        print(01)
        return
            
    print(00)
    if not c:
        if not e:
            print(0000)
            return
        print(0001)
        return
        
    if not d:
        print(0000)
        return
        
    print(0001)
    """

    # 1、键入用户名和密码
    user_name = input("请输入用户名：")

    # 查询此用户是否存在，以及原密码是否正确。
    query_user_sql = f"""select * from {table_name} where user_name = "%s"""
    cursor.execute(query_user_sql, user_name)

    # 用户不存在
    if not cursor.fetchone():
        print("没有此用户")
        return

    # 如果用户存在：
    while True:
        pwd = input("请输入密码：")
        query_pwd_sql = f"""select * from {table_name} where user_name = '%s' and password = '%s'"""
        cursor.execute(query_pwd_sql, [user_name, pwd])

        # 密码错误的情况
        if not cursor.fetchone():
            print("密码错误！！ 请重新输入！")
            continue

        # 密码正确的情况
        while True:
            new_pwd1 = input("请输入新密码：")
            new_pwd2 = input("请再次输入新密码：")

            # 两次密码不相同，重新输入
            if new_pwd1 != new_pwd2:
                print("两次密码不相同！！请重新输入！！")
                continue

            # 两次密码相同，修改密码
            update_pwd_sql = f"""update {table_name} set password = "%s" where user_name = "%s"""
            cursor.execute(update_pwd_sql, [new_pwd1, user_name])
            print("密码修改成功！！！程序即将退出！")
            return


def main():
    update_pwd()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
