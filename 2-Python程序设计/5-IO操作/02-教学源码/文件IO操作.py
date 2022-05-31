import random

# file_path = "/Users/Weston/Desktop/北京昌职/BeijingChangzhi/1-前置课程/数据资料/孤勇者-陈奕迅.mp4"
# with open(file_path, "rb") as files:
#      print(files.read())
import time

"""
文件IO操作
"""
# # 1。打开文件，创建文件对象
# files = open("hello3.txt", "r", encoding="utf-8")
# # 查看指针位置
# print(files.tell())
# # 修改指针位置
# files.seek(1)
#
# # 2。读取文件
# lines = files.read()
# print(lines)
#
# # 3. 关闭文件
# files.close()

"""
写文件
open("hello3.txt", "w", encoding="utf-8")
"""
# files = open("hello3.txt", "w", encoding="utf-8")
# print(files.tell())
# files.write("python")
# files.close()

# files = open("hello3.txt", "a", encoding="utf-8")
# print(files.tell())
# files.write("hello")
# files.close()
"""
20220426晚自习任务：
1。 完成随机点名小程序1.1版本：
创建【所有学生列表all_student_list】，把所有学生名单放进去。
创建【已经被点名的学生列表called_list】，把已经点过名的学生名单放进去。
创建【未被点名的学生列表not_called_list】，把未被点到的学生名单放进去
【Tip：这里提供两种思路：
（1）使用集合，集合.pdf文件中有小案例；
（2）使用列表的 not in 的方式去循环判断】。
使用while实现循环随机点名，每次点名都是从"not_called_list"中随机点名，
每次点名后，按q退出循环，按其他键回车（或者直接回车）进行下一次点名。
当not_called_list为空时，需要清空called_list以回到初始状态。
命名格式：日期_组别_姓名_随机点名小程序1-1版本.py
# """
# mingdan = ['崔昊元', '贾靖程', '吴俊岳', '王浩羽', '吕梦丽', '李博远', '墨梓恒', '牛皓冬', '张阔', '孙佳奇', '郑佳睦', '王孝天', '付一鸣', '李蓉轩', '陈观绅', '赵鑫博', '张子豪', '叶平']
# files = open("students.txt", "r", encoding='utf-8')
# mingdan = files.read().split("\n")
# # dianguomde = []
# # meidiandaode = []
# file_meidiandaode = open("not_called_students.txt", "r+", encoding="utf-8")
# while True:
#     if input(' 开始点名按任意键回车，q退出') == 'q':
#         break
#     if meidiandaode == []:
#         meidiandaode.extend(mingdan)
#         dianguomde = []
#     else:
#         not_called_studnet = file_meidiandaode.read().split("\n")
#         name = random.choice(not_called_studnet)
#         dianguomde.append(name)
#         meidiandaode.remove(name)
#         print(name)


"""
2。 完成随机点名小程序1.2版本：
创建students.txt文件，把本班同学的名字放到文件中；
使用python读取数据，实现循环随机点名小程序。
命名格式：日期_组别_姓名_随机点名小程序1-2版本.py
"""
# # input("欢迎进入随机点名小程序！请按任意键开始！")
# files = open("students.txt", "r", encoding='utf-8')
# students_text = files.read()
# # print(students_text)
# student_list = students_text.split("\n")
# print(student_list)
#
# while True:
#     name = random.choice(student_list)
#     print(name)
#     time.sleep(0.5)
# if input("任意键继续，q退出！") == "q":
#     break


"""
写文件
gb2312
gbk...
"""
# files = open("hello3.txt", "w", encoding="utf-8")
# # 指针
# print("指针位置0：",files.tell())
# files.write("hello1\n")
# print("指针位置1：",files.tell())
# files.write("hello2\n")
# print("指针位置2：",files.tell())
# files.write("hello3\n")
# print("指针位置3：",files.tell())
# files.write("hello4\n")
# print("指针位置4：",files.tell())
# files.close()


# files = open("hello3.txt", "a", encoding="utf-8")
# # 指针
# print("指针位置0：", files.tell())
# files.write("hello1\n")
# print("指针位置1：", files.tell())
# files.write("hello2\n")
# print("指针位置2：", files.tell())
# files.write("hello3\n")
# print("指针位置3：", files.tell())
# files.write("hello4\n")
# print("指针位置4：", files.tell())
# files.close()


"""
【Tip：这里提供两种思路：
（1）使用集合，集合.pdf文件中有小案例；
（2）使用列表的 not in 的方式去循环判断】。
"""
# # 方法一
# a = [1, 2, 3, 4, 5, 6]
# b = [1, 2, 3]
#
# set_a = set(a)
# set_b = set(b)
# print(list(set_a-set_b))
#
# # 方法二
# a = [1, 2, 3, 4, 5, 6]
# b = [1, 2, 3]
#
# c = []
# for i in a:
#     if i not in b:
#         c.append(i)
#
# print(c)
"""
files.read()  # 读取所有内容，返回字符串
files.readline()  # 读取一行内容，返回字符串
files.readlines()  # 读取所有内容，返回列表
"""
# files = open("hello3.txt", "r", encoding="utf-8")
# print(files.read())
# print(type(files.read()))
# print(files.readline())
# print(type(files.readline()))
#
# print(files.readlines())
# print(type(files.readlines()))
# files.close()
#
"""
files.write()  # 写入字符串
files.writelines()  # 写入列表
"""
# files = open("hello3.txt", "w", encoding="utf-8")
# # files.write("Nothing")
# files.writelines(["hello\n", "python\n", "nothing\n"])
# files.close()
#
#
"""
判断是否可以进行读写操作
"""
# files = open("hello3.txt", "w", encoding="utf-8")
# print(files.readable())  # 判断是否可读
# print(files.writable())  # 判断是否可写
# files.close()


"""
files.read()  # 读取文件
files.write("hello")  # 将hello写入文件
"""
# # 1. 打开文件，创建文件对象
# # r:read()
# # w:write()
# # encoding:编码格式  utf-8
# # files = open("hello3.txt", "r", encoding="utf-8")
# files = open("hello3.txt", "w", encoding="utf-8")
#
# # 2。读取文件或写入文件
# # text = files.read()  # 读取全部数据，返回的是字符串
# # # print(text)
# # print(type(text))
#
# text = "Nothing`s gonna change my love for you."
# files.write(text)  # 将文件中的原内容清空之后，将字符串写入文件
#
# # 3。关闭文件
# files.close()

"""
# files.read()  # 读取全部数据，返回的是字符串
# files.readline()  # 读取一行内容，返回的是字符串
# files.readlines()  # 读取所有内容，返回的是列表
# """
# files = open("hello3.txt", "r", encoding="utf-8")
# line = files.readline()  # 读取一行内容，返回字符串
# print("line1", line)
#
# line2 = files.readline()  # 读取一行内容，返回字符串
# print("line2", line2)
#
# lines = files.readlines()  # 读取所有内容，返回列表
# print(lines)
# files.close()
#
# """
# files.write()  # 将字符串写入文件
# files.writlines()  # 将列表写入文件
# """
# files = open("hello3.txt", "w", encoding="utf-8")
# # files.write("hello")
# a = ["a", "b", "c", "d"]
# files.writelines([i + "\n" for i in a])
# files.close()
#
# """
# files.readable()  # 判断文件是否可读
# files.writable()  # 判断文件是否可写
# """
# files = open("hello3.txt", "r", encoding="utf-8")
# if not files.readable():
#     print("文件不允许读取")
#     exit()
# else:
#     print(files.read())
# #
# if not files.writable():
#     print("文件不允许写入数据")
#     exit()
# else:
#     files.write("hello")

"""
append()  追加
"""
# files = open("hello3.txt", "a", encoding="utf-8")
# print(files.tell())  # 查看指针的位置， 指针位置在文件最后
# files.write("python")
# print(files.tell())  # 查看指针的位置， 指针位置在文件最后
# print(files.readable())
# files.close()
#
"""
open(file_path, "r+")
- 刚开始时指针在文件的开头
- files.read()之后，指针在文件末尾
- files.write()时，从末尾开始写，写入完成后，指针在文件末尾
"""
# files = open("hello3.txt", "r+", encoding="utf-8")
# print("--------：", files.tell())  # 指针在文件开头
# print(files.read())
# print("++++++++：", files.tell())  # 指针在文件末尾
# print(files.read())

# files.write("bbb")
# print("********：", files.tell())  # 指针在文件末尾
# files.write("cccc")
# files.close()
#
# """
# open(file_path, "w+")
# - 在刚开始时，会格式化文件，把文件清空，所以读取文件时，读取内容为空
# - 在刚开始时，指针在文件开头
# - files.write()时，从文件开头开始写入,写入完成后，指针在文件末尾
# - 可以使用file.seek(0) 将指针移到文件开头
# - 使用file.seek(0)之后，可以正常file.read()文件
# """
# files = open("hello3.txt", "w+", encoding="utf-8")
# print("指针位置0：", files.tell())  # 指针在文件开头
# print(files.read())
# print("指针位置1：", files.tell())  # 指针在文件末尾
# print("----")
# print(files.read())
# print("----")
#
# print("指针位置0：", files.tell())
# files.write("hello")
# print("指针位置1：", files.tell())
# print(files.read())  # ？
# print("指针位置2：", files.tell())
# files.close()
#
#
# """
# - 在刚开始时，指针在文件末尾，所以直接读取文件，读取内容为空
# - files.write()时，从文件末尾写入数据，不会覆盖掉之前的内容。写入数据之后，指针在文件末尾
# """
# files = open("hello3.txt", "a+", encoding="utf-8")
# print("指针位置0：", files.tell())
# print(files.read())
# print("指针位置1：", files.tell())
#
# # 改变指针位置
# files.seek(0)
#
# print("移动指针之后的位置：", files.tell())
# print(files.read())
# print("指针位置3：", files.tell())
# files.write("python")
#
# files.close()


# files = open("hello3.txt", "r+")
# files.truncate(0)
# files.close()

"""
20220427任务：

【请严格按照命名要求对变量进行命名。】

1。 完成随机点名小程序1.3版本：
创建【“所有学生”文件“students.txt”】，把所有学生名单放进去；
创建【“已经被点名的学生”文件“called_students.txt.txt”】，把已经点过名的学生名字放进去；

【可选】创建【“未被点名的学生”文件“not_called_students.txt”】，把未被点到的学生名字放进去。

使用while实现循环随机点名小程序。
每次点名后，按q退出循环，按其他键回车（或者直接回车）进行下一次点名。

Tips:
1.每次点名后，都需要对文件进行删除和增加内容。


命名要求：
格式：日期_组别_姓名_随机点名小程序1-3版本.py
举例：20220427_四组_张三_随机点名小程序1-3版本.py
"""
"""
方法一：
"""
# input("欢迎进入随机点名小程序！任意键开始")
# f_students = open('students.txt', 'r', encoding='utf-8')
# f_called = open('called_students.txt', 'r+', encoding='utf-8')
#
# all_students = f_students.readlines()
#
# while True:
#     f_called.seek(0)
#     called_students = f_called.readlines()
#     print(called_students)
#
#     not_called_list = list(set(all_students) - set(called_students))
#     if not not_called_list:
#         f_called.truncate(0)
#         continue
#
#     name = random.choice(not_called_list)
#     print(name)
#
#     not_called_list.remove(name)
#     f_called.write(name)
#     f_called.flush()
#
#     time.sleep(0.2)
#     if input("q退出，其他键继续！") == "q":
#         break
#
# f_students.close()
# f_called.close()

"""
方法二：
"""
# f_students = open('students.txt', 'r', encoding='utf-8')
# f_called = open('called_students.txt', 'a', encoding='utf-8')
# f_not_called = open('not_called_students.txt', 'r+', encoding='utf-8')
#
# all_students = f_students.readlines()
#
# while True:
#     f_not_called.seek(0)
#     not_called_students = f_not_called.readlines()
#     print(not_called_students)
#
#     if not not_called_students:
#         f_not_called.writelines(all_students)
#         f_not_called.flush()
#         f_called.truncate(0)
#         continue
#
#     name = random.choice(not_called_students)
#     print(name)
#
#     # not_called_students 操作
#     not_called_students.remove(name)
#
#     f_not_called.truncate(0)
#     f_not_called.seek(0)
#     f_not_called.writelines(not_called_students)
#     f_not_called.flush()
#
#     # called_students操作
#     f_called.write(name)
#     f_called.flush()
#
#     time.sleep(0.3)
#     # if input("q退出，其他键继续！") == "q":
#     #     break
#
# f_students.close()
# f_called.close()
# f_not_called.close()
