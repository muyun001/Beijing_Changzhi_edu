print("--------------------文件io操作------------------------")

"""
文件读写的步骤：
    - 打开文件，创建文件对象
        - f = open(file_path)
    - 对文件进行读写操作
        - f.read()
        - f.write()
    - 关闭文件
        - f.close()
"""

"""
文件读取：
f = open(file_path, "r")
    - f.read():
        - 一次性读取文件的所有内容，返回字符串
        - 刚开始时，指针在文件开头
        - 读取内容之后，指针在文件结尾，所以再次读取文件时，读到的内容为空
        - f.read(n): 读取前n个字符， 回车符（\n）也算一个字符

    - f.readline()：
        - 一次读取文件的一行内容，返回字符串（一般用于读取大文件）
        - 刚开始时，指针在文件开头
        - 读取内容之后，指针在下一行的开头，所以再次读取文件时，读到新一行的内容
        - f.readline(n):读取这一行的前n个字符，回车符（\n）也算一个字符
        - 一般使用while循环读取,当读取内容为空时退出

    - r.readlines()：
        - 一次读取文件的所有行，返回列表（一般用于读取小文件）
        - 刚开始时，指针在文件开头
        - 读取内容之后，指针在文件末尾
    
    - r.readable()：
        - 判断文件是否可读，返回bool类型
"""
# 1.打开文件，创建文件对象
file = open("25_io_test.txt", "r")
print("指针位置1:", file.tell())

# 2.读取文件
text = file.read()
print(type(text))  # str类型
print("text:", text)  # 一次性读取文件中的所有内容， 返回一个字符串
print(len(text))
print("指针位置2:", file.tell())
text2 = file.read()
print("text2:", text2)  # 读取到的内容为空

text2 = file.read(5)
print(len(text2))
print(text2)  # baidu

text3 = file.read(5)
print(len(text3))
print(text3)
###################################
# files.readline()
file = open("25_io_test.txt", "r")
print("指针位置1:", file.tell())

text_line_1 = file.readline()
print(text_line_1)
print("指针位置2：", file.tell())

text_line_2 = file.readline()
print(text_line_2)
print("指针位置3：", file.tell())

text_line_3 = file.readline(4)  # 读取这一行的前4个字符
print(text_line_3)
print("指针位置3：", file.tell())

while True:
    text = file.readline()
    if text.strip() == "":
        break
    print(text)  # 每次读取一行， 返回一个字符串
# 3.关闭文件
file.close()
exit()

file = open("25_io_test.txt", "r")
print("指针位置1:", file.tell())
# 读取所有行，返回一个列表
text = file.readlines()
print("指针位置2：", file.tell())

print(text)
print(type(text))

for t in text:
    pass
# 3.关闭文件
file.close()
exit()

print(file.readable())  # 判断文件是否可读，返回bool类型
# 3.关闭文件
file.close()

"""
文件写入
f = open(file_path, "w")
    - f.write()：
        - 刚开始时，指针在文件开头
        - 写入的数据是字符串类型
        - 写入数据后，指针在文件结尾
        - 写入数据会把之前内容覆盖掉

    - f.writelines()
        - 刚开始时，指针在文件开头
        - 写入的数据是列表类型
        - 写入数据后，指针在文件末尾
        - 写入数据会把之前内容覆盖掉

    - f.writeable(): 
        - 判断文件是否可写，返回bool类型
"""

print("-------------- files.read() --------------------")
# 1打开文件
file = open("25_io_test.txt", "r")
# 指针， files = open(file_path, "r") 的指针最开始的时候在文件开头
print("指针位置1：", file.tell())
# 2文件读取l
text = file.read()
print("text:", text)
# 指针
print("指针位置2：", file.tell())
text2 = file.read()
print("text2:", text2)
# 3关闭文件
file.close()

print("-------------- files.readline() --------------------")
file = open("25_io_test.txt", "r")
print("指针位置1：", file.tell())

text = file.readlines()
print(text)

print("指针位置2：", file.tell())
file.close()

print("-------------- files.readlines() --------------------")

file = open("25_io_test.txt", "r")
print("指针位置1：", file.tell())

text = file.readline()  # 每次读取一行
print(text)

print("指针位置2：", file.tell())

text2 = file.readline()
print(text2)

print("指针位置3:", file.tell())

file.close()

"""
文件的写入
files = open(file_path, "w")
files.write()
    - 刚开始时，指针在文件的开头，所以新写的内容会将原来的内容覆盖掉。
    - 写入类型是字符串
    - files.write()之后，指针在文件的末尾

files.writelines()
    - 刚开始时，指针在文件的开头，所以新写入的内容会将原来的内容覆盖掉。
    - 写入的类型是一个列表，可以在列表的每个元素后面加"\n"，可以实现写入多行
    - files.writelines()之后，指针在文件末尾。

files.writeable()
    - 判断文件是否可写。
"""
print("-------------- files.write() --------------------")
file = open("25_io_test.txt", "w")

print("指针位置1：", file.tell())

file.write("s")

print("指针位置2：", file.tell())

file.write("sougou")

print("指针位置3:", file.tell())

file.close()

print("-------------- files.writelines() --------------------")
file = open("25_io_test.txt", "w")
print("指针位置1:", file.tell())

file.writelines(["sougou\n", "sougou\n"])

print("指针位置2:", file.tell())

file.writelines(["baidu\n", "baidu\n"])

file.close()

print("-------------- files append 操作 --------------")
"""
# 从文件的最后追加内容
append()
    - 刚开始的时候，指针在文件的末尾
"""
file = open("25_io_test.txt", "a")  # 追加
print("指针位置1：", file.tell())

file.write("baidu")

print("指针位置2：", file.tell())

# 3.关闭文件
file.close()

print('-------------- 可读可写 --------------')
"""
可读可写
open(file_path, "r+")
    - 刚开始时指针在文件的开头
    - files.read()之后，指针在文件末尾
    - files.write()时，从末尾开始写，写入完成后，指针在文件末尾

open(file_path, "w+")
    - 在刚开始时，会格式化文件，把文件清空，所以读取文件时，读取内容为空
    - 在刚开始时，指针在文件开头
    - files.write()时，从文件开头开始写入,写入完成后，指针在文件末尾
    - 可以使用file.seek(0) 将指针移到文件开头
    - 使用file.seek(0)之后，可以正常file.read()文件

open(file_path, "a+")   append()追加
    - 在刚开始时，指针在文件末尾，所以直接读取文件，读取内容为空
    - files.write()时，从文件末尾写入数据，不会覆盖掉之前的内容。写入数据之后，指针在文件末尾
"""
file = open("25_io_test.txt", "r+")
print("指针位置1：", file.tell())

text = file.read()
print("text:", text)

print("指针位置2：", file.tell())

text2 = file.read()
print("text2:", text2)

file.write("sougou")

print("指针位置3：", file.tell())

file.close()

###################################################
file = open("25_io_test.txt", "w+")
print("指针位置1：", file.tell())

# text = files.read()
# print("text:", text)

file.write("baidu")

print("指针位置2：", file.tell())

# 改变指针位置
file.seek(0)
print("files.seek(0)之后,指针位置：", file.tell())

text2 = file.read()
print("text2:", text2)

print("指针位置3：", file.tell())

file.close()

###################################################
file = open("25_io_test.txt", "a+")
print("指针位置1：", file.tell())

text = file.read()
print("text:", text)

print("指针位置2：", file.tell())

file.write("sougou")

print("指针位置3：", file.tell())

file.close()

###################### with open()
# files = open("25_io_test.txt", "r")
with open("25_io_test.txt", "r", encoding="utf-8") as file:
    file.read()
# files.close()
