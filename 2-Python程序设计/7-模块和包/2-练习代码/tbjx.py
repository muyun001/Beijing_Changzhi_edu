# 设置作为模块被全部调用时，只能引入的变量
#__all__ = ["x", "get"]
# 单下划线定义的变量，不能被模块外程序使用
_age = 123
x = "太白金星"
print("from the tbjx.py")
def read1():
    print("tbjx模块： %s" % x)
def change():
    global x
    x = "barry"

def get():
    print("foo文件中的x=", x)
    print("_age值为", _age)

