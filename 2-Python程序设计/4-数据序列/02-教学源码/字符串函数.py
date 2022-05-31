"""
字符串api
"""
# c = "I'm Tom"
# print(c)

# c = 'I\'m Tom'   # 转义符  \
# print(c)

# c = "hello \nworld!"  # \n 的意思是换行符
# print(c)

# c = "hellawblrd!"
# print(c[2:-1:2])
# # print(c[-1:2:-2])

# c = "hell world!"
# print(c.find("ello"))  # 返回查找字符串所在的下标
# print(c.find("llo", 0))
# print(c.find("llo", 4))  # 从下标为4的位置开始查找，若找不到则返回-1
# print(c.find("r", 2, 7))  # 从下标为2的位置开始查找，到下标为（7-1）的下标为止，若找不到则返回-1

# c = "hello world!"
# print(c.index("helo"))  # 如果找到则返回首字母所在下标，找不到则报错：ValueError: substring not found


c = "hello world!"
# print(c.count("o"))  # 计数

"""
in
"""
print("hello" in c)

if "" in "":
    pass

l = "12345"
if "5" in l:
    print(111)
else:
    print(2)
