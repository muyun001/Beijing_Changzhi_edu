# input函数

# a = input("请入一个值：")
# print(type(a))
# # 使用int(str)可以把str类型转成int类型
# # 但是，这里的str必须是可以转的
# a = int(a)
# print(type(a))
# print(a)

age = 17
# a = input("请输入你的年龄：")
# a = int(a)

"""
1.如果>17，则输出"猜的太大了，再小点试试"
2.如果<17，则输出"猜的太小了，再大点试试"
3.如果=17，则输出"恭喜你猜对了！"
"""
# if a > 17:
#     print("猜的太大了，再小点试试")
# elif a < 17:
#     print("猜的太小了，再大点试试")
# else:
#     print("恭喜你猜对了！")

a = ["a", "b", "c", "d"]

list1 = ["李白", "韩信", "程咬金", "百里玄策", "花木兰", "貂蝉"]
list2 = list1[:]
list3 = list1[-4:]
print(list2[-2:])
print(list3)

url = "https://www.baidu.com/s?wd="
word = "手机"

url = url+word
url = "https://www.baidu.com/s?wd={}"
url = url.format(word)
print(url)
