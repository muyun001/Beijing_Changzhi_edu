dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# print(dict1.keys())

# for i in dict1.keys():
#     print(i)

# for v in dict1.values():
#     print(v)

# for i in dict1.items():
#     # print(i)
#     print(i[0])
#     print(i[1])

# for k, v in dict1.items():
#     print(k, v)


# files = open("", "r")
# files.read()
# files.close()
#
# with open("", "r") as f:
#     f.read()
file = open("hello.txt", "r")
"""
指针在哪，就从哪开始进行读/写
r:文档开始的位置
w:文档开始的位置
a: 文章末尾的位置
"""

with open("hello.txt", "r", encoding="utf-8") as file:
    file.read()

file = open("hello.txt", "r", encoding="utf-8")
file.read()
file.close()
