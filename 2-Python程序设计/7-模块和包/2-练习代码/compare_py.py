"""
输出__name__ 变量，查看变量的值

"""
print("输出compare_py的变量__name__:", __name__)
# 直接执行当前文件：__name__ 的值为 __main__
def test_a_b(a,b):
    if a/b >10:
        print("好")
    else:
        print("坏")

if __name__ == "__main__":
    test_a_b(1,0)
    print("你正直接执行compare_py.py文件")

