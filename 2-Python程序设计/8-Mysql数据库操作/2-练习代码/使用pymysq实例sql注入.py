"""
1.用户登录实例：
用户输入用户名和密码，判断用户账号是否正确，
如何正确，用户可以进行密码修改

2.直接进行密码修改
需要对用户的账号和原密码进行验证
1.让用户输入账号，判断账号是否存在。
2.让用户输入原始密码新密码
    如果原始密码正确，更改为新密码。
"""
import pymysql

print("""
        1. 登录
        2. 修改密码
    """)
selected = input("请选择操作方式>>>")
if selected == '2':
    # 让用户输入账号。判断账号是否存在
    user_name = input("请输入账号>>>").strip()
    print(user_name)

    #print(sql)
    # 1. 连接数据库
    conn = pymysql.connect(
        host='localhost',  # 127.0.0.1
        port=3306,
        user='root',
        password='123456',
        database='gm02',
        charset='utf8'
    )
    # 2.创建游标,可以传递参数
    cursor = conn.cursor()
    sql = 'select * from user where user_name=%s'
   #execute()函数本身就有接受SQL语句变量的参数位，只要正确的使用就可以对传入的值进行转义，从而避免SQL注入的发生
    #  使用execute()进行sql语句拼接,注意 占位符的引号，不需要引号
    # 如上sql，如果占位符使用引号,sql结果为:select * from user where user_name="\"user_name\""
    cursor.execute(sql, user_name)
    if cursor.fetchone():
        print("账号正确")
        while True:
            pwd = input("请输入原始密码>>>").strip()
            new_pwd = input("请输入新密码>>>").strip()
            re_pwd = input("请再次输入新密码>>>").strip()
            if new_pwd != re_pwd:
                print("2次密码不一致！")
                # 继续重新输入
                continue
            else:
                # 当2次一致时。# 拼接sql检查用户密码是否正确
                # sql = 'select * from user where user_name="{user_name}" and pwd="{pwd}"'
                sql = 'select * from user where user_name=%s and pwd=%s'
                # 执行操作
                #cursor.execute(sql)
                cursor.execute(sql, (user_name, pwd))
                # 判断返回结果
                if cursor.fetchone():
                    # 结果不为空.进行密码修改操作
                    # sql = f'update user set pwd="{new_pwd}" where user_name="{user_name}"'
                    sql = 'update user set pwd=%s where user_name=%s'
                    # 执行sql
                    # cursor.execute(sql)
                    cursor.execute(sql, (pwd, user_name))
                    # 事务提交
                    conn.commit()
                    print(f"'{user_name}'密码修改成功")
                    break
                else:
                    print(f"'{user_name}'原始密码错误")
                    continue
    else:
        print("账号错误")


