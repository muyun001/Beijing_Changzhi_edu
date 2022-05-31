"""
可迭代对象：
实现了__iter__方法的对象就叫做可迭代对象，比如：字符串，列表，元祖，字典，集合等等，都是可迭代对象。
可迭代对象，简单理解就是能够进行遍历的对象。

字符串、列表、字典、元祖、集合。

迭代 == 遍历
"""

"""
while循环
"""
# while True:
#     pass
#     break
#
#
#
# print(1)
import time

"""
使用while循环实现输出2-3+4-5+6…+100 的和
"""
# i = 2
# list_2 = []
# list_3 = []
# while i <=100:
#     if i % 2 == 0:#偶数
#         list_2.append(i)
#     else:
#         list_3.append(-i)
#     i += 1
# print(sum(list_2)+sum(list_3))
#
# i = 2
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i
#     i += 1
#
# print(sum)

"""
使用while循环实现输出2-3+4-5+6…+100 的和
"""
# i = 2
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i
#     i += 1
# print(sum)

"""
while 99 乘法表
"""
a = 1  # 1
b = 1  # 2
while b <= 9:  # 行循环
    a = 1
    while a <= b:
        print(f"{a}*{b}={a * b}", end="\t")
        a += 1
    print()
    b += 1

# for a in range(1, 10):  # hang
#     for b in range(1, 9+1):  # lie
#         if b <= a:
#             print(f"{b}*{a}={a * b}", end="\t")
#     print()

"""
7.
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前 20 项之和。
"""


