"""
str.format()

使用{}作为占位符，没有格式要求
"""
# name = "zhangsan"
# age = 19
# print("name:{}, age:{}".format(name, age))
# print("name:{0}, age:{1}".format(name, age))
# print("name:{name}, age:{age}".format(name=name, age=age))
# print(f"name:{name}, age:{age}")
# print("*"*50)
"""
1. 猜年龄：
设置一个年龄为17。使用键盘输入一个年龄，
如果大于17就打印“猜的太大了，再小点试试”，
如果小于17就打印“猜的太小了，
再大点试试”，如果猜对了就打印“恭喜你猜对了！”
"""
age = int(input("请输入年龄："))
# print(type(age))
# # print(age)
#
# if age > 17:  # str类型和int类型无法进行大小的比较
#     print("猜的太大了，再小点试试")
# age = "17"
# print(age)
# print(type(age))
# age = int(age)
# print(type(age))


# 单分支：
# if age > 17:
#     print("猜的太大了，再小点试试")


# 双分枝
# 猜对就打印"猜对了"，否则打印猜错了
# if age == 17:
#     print("猜对了")
# else:
#     print("猜错了")

# 多分枝
if age > 17:
    print("猜的太大了，再小点试试")
elif age < 17:
    print("猜的太小了，再大点试试")
else:
    print("猜对了")

"""
2.写程序，成绩有ABCDE5个等级，与分数的对应关系如下：
    A    90-100
    B    80-89
    C    60-79
    D    40-59
    E    0-39
要求用户输入0-100的数字后，你能正确打印他的对应成绩等级。
如果输入的分数不在上述选项中，则输出"您输入的分数有误。"
"""
# and 和 or 的区别
score = int(input("please input score:"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 60 <= score <= 79:
    print("C")
elif 40 <= score <= 59:
    print("D")
elif 0 <= score <= 39:
    print("E")
else:
    print("您输入的分数有误。")

# if score >= 100 and score <= 0:
#     pass

"""
3.实现用户输入用户名username和密码password,
当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
"""


"""
4. 猜年龄进阶版：
设置一个年龄为17。使用键盘输入一个年龄，如果大于17就打印“猜的太大了，再小点试试”，
如果小于17就打印“猜的太小了，再大点试试”，如果猜对了就打印“恭喜你猜对了！”
使用for循环，如果猜对则直接退出循环；猜错的情况最多出现4次，第5次猜错时退出循环。
"""
