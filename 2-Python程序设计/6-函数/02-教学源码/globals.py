# 内置函数globals()
# global：全球、全局、整体的意思

"""
全局变量、局部变量的理解：
全局变量：可以被本程序所有对象或函数引用
局部变量：只能在一定范围内被引用
"""
# 举例：
a = 1  # 全局变量


def print_hello():
    global hello
    hello = "hello world!"  # 局部变量
    print(hello)


def use_test():
    print_hello()
    print(a)
    print(hello)


if __name__ == "__main__":
    use_test()

    print(globals())  # 输出所有的全局变量
    print(globals().get("hello", -1))
