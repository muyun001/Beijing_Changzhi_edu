print('模块foo==>')
x = 1


def get():
    print("foo文件中的x=", x)


def change():
    global x
    x = 0
