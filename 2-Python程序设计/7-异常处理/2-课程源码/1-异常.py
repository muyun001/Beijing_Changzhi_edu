"""
我们目前可能会遇到的异常：
1、文件找不到：FileNotFoundError
2、0作为除数，产生异常：ZeroDiversionError
3、值的异常：ValueError
"""
# open('test.txt', 'r')

# print(2/0)

# print(int("hello"))

# try:
#     a = int(input("please input first num:"))
#     b = int(input("please input second num:"))
#     result = a / b
# except ValueError as e1:
#     print("必须键入整型数字！！")
# except ZeroDivisionError as e2:
#     print("程序出错！不可以将0作为除数！！")
# else:
#     print(result)

"""
登陆功能：
1、用户名和密码不可为空
2、密码不能小于8位数
"""


def login():
    username = input("please input username:")
    password = input("please input password:")
    if not username or not password:
        raise Exception("用户名和密码不可为空！")

    if len(password) < 8:
        raise Exception("密码不能小于8位数！")

    if username == "zhangsan" and password == "12345678":
        print("登陆成功")
    else:
        print("用户名或密码错误！")


def main():
    try:
        login()
    except Exception as e:
        print("出现异常！", e)
    else:
        print('登陆成功！')

if __name__ == '__main__':
    main()
