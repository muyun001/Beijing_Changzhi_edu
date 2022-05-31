"""
异常
FileNotFoundError: 路径问题。
绝对路径：\，/，//
"""
# 相对路径
# 引用hello1.txt
# with open("hello1.txt", "r", encoding="utf-8") as f:
#     print(f.read())
# # 引用hello2.txt
# with open("../hello2.txt", "r", encoding="utf-8") as f:
#     print(f.read())
# # 引用hello3.txt
# with open("../files/hello3.txt", "r", encoding="utf-8") as f:
#     print(f.read())

"""
目录结构：
2-课程源码
    - hello2.txt
    - files
        - hello3.txt
    - 源码
        - 1-异常讲解.py
        - hello1.txt
        
引用hello.txt的方式：hello1.txt
引用hello2.txt的方式：../hello2.txt
引用hello3.txt的方式：../files/hello3.txt
"""
# 绝对路径
# file_path = "/Users/Weston/Desktop/北京昌职/beijing_changzhi_edu/2-Python程序设计/7-异常处理/2-课程源码/files/hello3.txt"
# with open(file_path, "r", encoding="utf-8") as f:
#     print(f.read())

"""
课堂作业1：
1、测试相对路径和绝对路径文件的读取。
2、学习异常。
"""

"""
捕获异常
try:
    xxxxxxxx  # 尝试执行的语句
except:
    xxxxxxxx  # 如果发生错误，将要采取的措施
"""

# try:
#     f = open("text.txt", "r")
# except:
#     print("程序出现了异常！！！")
#
# # f = open("text.txt", "r")
# print('---------------------')


"""
捕获异常
try:
    xxxxxxxx  # 尝试执行的语句
except 异常的类型:
    xxxxxxxx  # 如果发生错误，将要执行的语句
"""
# try:
#     f = open("text.txt", "r")
# except FileNotFoundError as e:
#     print("程序出现了异常！！！", e)
#
# # f = open("text.txt", "r")
# print('---------------------')

"""
捕获异常
try:
    xxxxxxxx  # 尝试执行的语句
except 异常的类型:
    xxxxxxxx  # 如果发生错误，将要执行的语句
    
Exception是所有异常的父类。
"""
# print(1/0)

# try:
#     print(1/0)
# except Exception as e:
#     print("程序出现了异常！！！", e)
#
# # f = open("text.txt", "r")
# print('---------------------')


"""
捕获异常
try:
    xxxxxxxx  # 尝试执行的语句
except 异常的类型1:
    xxxxxxxx  # 如果发生错误，将要执行的语句
except 异常的类型2:
    xxxxxxxx  # 如果发生错误，将要执行的语句
except 异常的类型3:
    xxxxxxxx  # 如果发生错误，将要执行的语句
except Exception:
    xxxxxxx  # 如果发生的意料之外的异常，使用Exception去捕获，然后在这写处理措施
Exception是所有异常的父类。
"""

# import traceback
# try:
#     a = int(input("please input first number:"))
#     b = int(input("please input second number:"))
#     print(a / b)
# except ZeroDivisionError:  # 除以0的异常
#     b = int(input("程序出现了错误！！0不能作为除数！！！第二个值不能是0！！！ 请重新输入！！！"))
#     print(a / b)
# except ValueError:  # 不是整型数字的异常
#     a = int(input("一定要输入整型数字！！数字！！数字！！！请重新输入第一个值！！"))
#     b = int(input("一定要输入整型数字！！数字！！数字！！！请重新输入第二个值！！"))
#     print(a/b)
# except Exception:
#     traceback.print_exc()
#     # print("程序出现了其他报错！！！", e)
#
# print('---------------')


# print('-'*50)
# import traceback
# try:
#     a = int(input("please input first number:"))
#     b = int(input("please input second number:"))
#     print(a / b)
# except ZeroDivisionError:  # 除以0的异常
#
#     # 异常捕获是可以嵌套使用的
#     try:
#         b = int(input("程序出现了错误！！0不能作为除数！！！第二个值不能是0！！！ 请重新输入！！！"))
#         print(a / b)
#     except ZeroDivisionError:
#         b = int(input("怎么搞得，还是输入0！！！！，说了不能输入0！！！！再最后重新输入一次！！！"))
#         print(a / b)
#
# except ValueError:  # 不是整型数字的异常
#     a = int(input("一定要输入整型数字！！数字！！数字！！！请重新输入第一个值！！"))
#     b = int(input("一定要输入整型数字！！数字！！数字！！！请重新输入第二个值！！"))
#     print(a/b)
# except Exception:
#     traceback.print_exc()
#     # print("程序出现了其他报错！！！", e)
#
# print('---------------')


"""
try:
    xxx
except:
    xxx
else:
    xxx  # 如果程序不报错，正常执行的语句
"""
# try:
#     f = open("hello.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("程序出现了错误！！！文件不存在！！！")
# else:
#     print(f.read())


# # 个人习惯，不经常使用else
# try:
#     f = open("hello1.txt", "r", encoding="utf-8")
#     print(f.read())
# except FileNotFoundError:
#     print("程序出现了错误！！！文件不存在！！！")

"""
try:
    xxx
except:
    xxx
else:
    xxx  # 如果程序不报错，正常执行的语句
finally:  # 不管程序会不会报错，都要执行下面的语句
    xxx
"""
# try:
#     f = open("hello1.txt", "r", encoding="utf-8")
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("程序出现了错误！！！文件不存在！！！")
# finally:  # 最终
#     print("不管会不会报错，这一句都会执行")


"""
捕获异常的嵌套使用
"""
# 异常捕获是可以嵌套使用的
try:
    a = int(input("请输入第一个值【整型数字】："))
    b = int(input("请输入第二个值【整型数字】："))
    print(a / b)
except ZeroDivisionError:
    try:
        b = int(input("怎么搞得，还是输入0！！！！说了不能输入0！！！！再最后重新输入一次！！！"))
        print(a / b)
    except ZeroDivisionError:
        print('都说了不能输入0！！！！')

# index = 0
#
# while index < 100:
#     try:
#         pass
#     except:
#         pass
#     finally:
#         index += 1


"""
20220510:
作业1：
    异常的练习。
    命名：异常练习.py
作业2：
    学生管理系统
    命名：student_system.py
"""

def add_s():
    pass

def delete_s():
    pass

def update_s():
    pass

def query_s():
    pass

def query_all():
    pass


def main():
    all_students = []
    print("--------------------")
    print("1、添加")
    print("2、删除")
    print("3、更新")
    print("4、退出")
    print("--------------------")
    while True:
        num = input("请输入功能序号：")
        if num == "1":
            add_s()
        elif num == "2":
            pass
        elif num == "3":
            pass
        elif num == "4":
            break
        else:
            pass


if __name__ == '__main__':
    main()
