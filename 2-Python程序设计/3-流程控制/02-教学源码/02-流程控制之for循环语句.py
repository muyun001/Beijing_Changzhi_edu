"""
可迭代对象：
实现了__iter__方法的对象就叫做可迭代对象，比如：字符串，列表，元祖，字典，集合等等，都是可迭代对象。
可迭代对象，简单理解就是能够进行遍历的对象。

字符串、列表、字典、元祖、集合。

迭代 == 遍历
"""
# s = "Hello world!"
#
# # 作用域
# for j in s:
#     print(j)

# my_list = [1, 2, 3, 4]

# my_listB=[]
#
# for i in my_list:
#     my_listB.append(i+5)
#
# print(my_listB)

# append()
# li = [1,2,3]
# a = 4
# li.append(a)
# print(li)

# 写法2
# my_listB = [i + 5 for i in my_list]  # [6, 7, 8, 9]
# print(my_listB)

# my_list = ["a","b","c","d","e","f"]
# my_listB = [] # 创建一个新的列表
# my_listB = list()  # 创建一个新的列表
#
#
# for c in my_list:
#     my_listB.append(c+'hello')  # "bhello"
#     # print(c)
#
# print(my_listB)


# my_listB = [b + "hello" for b in my_list]
# print(my_listB)

"""
range()

1.range(end)
从0开始遍历，一直到end-1结束。
"""
# for i in range(100+1):
#     print(i)

# for i in range(0, 100+1):
#     print(i)

# for i in range(50, 100+1):
#     print(i)

# 第三个参数：step,步长
# for i in range(50, 100+1, 3):
#     if i == 56:
#         break  # 退出循环
#     print(i)
# print("end")
#
# for i in range(50, 100+1, 3):
#     if i == 59:
#         continue  # 结束本次循环，直接进行下一轮循环
#     print(i)
#
#
# print("end")

"""
作业1：猜年龄进阶版：
设置一个年龄为17。
使用键盘输入一个年龄，
如果大于17就打印“猜的太大了，再小点试试”，
如果小于17就打印“猜的太小了，再大点试试”，
如果猜对了就打印“恭喜你猜对了！”

要求：使用for循环，如果猜对则直接退出循环；猜错的情况最多出现4次
"""

# age = 17
# for _ in range(4):  # 0,1,2,3,4
#     guess_age = int(input("please input age:"))
#     if guess_age > age:
#         print()
#     elif guess_age<age:
#         print()
#     else:
#         print()
#         break

"""
作业2：
需求：打印50-100间的奇偶数
分析：
奇数位不能被2整除的数，能被2整除的为偶数
"""
"""
奇数：1，3，5，7，9   ->    奇数  % 2 = 1
偶数：2，4，6，8 ->    奇数  % 2 = 0

求余：
56 / 10  = 5.。。。。6
32 / 10  = 3.....2

3 / 2 = 1....1
5 / 2 = 2....1
7 / 2 = 3...1
"""

# print(1 % 2)
# print(3 % 2)
# print(5 % 2)
# print(7 % 2)
# print(9 % 2)
# print(11 % 2)
#
#
# print(2 % 2)
# print(4 % 2)
# print(6 % 2)
# print(8 % 2)
# print(10 % 2)
# print(12 % 2)

# for i in range(50, 100+1):
#     if i % 2 == 1:
#         print(i, "是奇数")
#     else:
#         print(i, "是偶数")


"""
作业3：
从 100 米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第 10 次落地时，共经过多少米？
第 10 次反弹多高？
"""
"""
初始高度100m
1.50 = 100 * 1/2
2.25 = 50*1/2 = 100 * (1/2)^2
3.12.5 = 25*1/2 = 100 * (1/2)^3
...
n. 100 * (1/2)^n
"""
init_high = 100
sum = 100
for n in range(1, 10):
    print(f"第{n}次弹起")
    high = 100 * (1 / 2) ** n
    sum += high * 2

print(sum)
print(high)

# high = 100
# li = [high]
# for i in range(2, 11):
#     li.append(high * 2)
#     high /= 2
# print(sum(li))

"""
作业4：
需求：一栋楼有5层，每层8间屋子，要求你把本楼所有的房间号打印一遍， 格式“1层-104”， “2层-205“
分析：需要循环嵌套
"""
"""
for循环的嵌套
"""
# for i in range(1, 5 + 1):
#     for j in range(1, 8 + 1):
#         print(f"{i}层-{i}0{j}")
#         # print("{a}层-{b}0{c}".format(a=i, b=i, c=j))
#         # print("%d层-%d0%d"%(i, i, j))

"""
11. [“百钱百鸡”]问题：
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只？
"""
"""
只买公鸡，能买20个
只买母鸡，能买33个
只买小鸡，能买300个
"""
for num_gj in range(21):  # 数量
    for num_mj in range(34):
        for num_xj in range(101):
            if num_gj + num_mj + num_xj == 100 and num_gj * 5 + num_mj * 3 + num_xj * 1/3 == 200:
                print(f"公鸡{num_gj}只，母鸡{num_mj}只，小鸡{num_xj}只")



