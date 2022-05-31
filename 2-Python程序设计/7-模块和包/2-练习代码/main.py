import foo
"""
导入模块执行步骤
    1.执行foo.py 文件
    2.创建新的命名空间foo，将文件中的变量放到命名空间中
    3.可以命名空间调用内部的变量
"""
# 调用命名空间中的变量x
# print(foo.x)
#
# foo.get()
# x = 12
# print(foo.x)
# print(x)
# def get():
#     print("main.py文件中的get函数")
# foo.get()
# get()
x = 15
foo.change()
print("main.py中的x=", x)
print("foo.py中的x=", foo.x)
