""""""
"""
"def" 是创建一个普通函数的关键词
其实还有一种函数叫"匿名函数"，意思就是这个函数没有名字
"lambda" 是创建匿名函数的关键词
官网地址：https://docs.python.org/zh-cn/3/tutorial/controlflow.html#lambda-expressions
"""

"""
lambda的语法结构：
    lambda 参数:表达式
        - 参数数量可以是多个，但是表达式只能有一个，lambda表达式会自动将结果返回
    如：lambda s: s
    如：lambda x: x+1
    如：lambda x,y: x+y
"""

print(lambda s: s)  # <function <lambda> at 0x7fd7af5d0f70>
# 等同于：
g = lambda s: s
print(g)  # <function <lambda> at 0x7fd7af5d0f70>

# 可以在函数后面直接传递实参
ss = "hello world!"
(lambda s: print(s))(ss)

print("----------- 普通函数 / lambda函数 求参数y的平方-------------")
# 普通函数：
def cube(y):
    return y * y


print(cube(5))

# print(lambda y: y * y(5))  # <function <lambda> at 0x7fc028ed0f70>

# lambda函数
g = lambda y: y * y
print(g(5))

print("------------- lambda举例：传2个参数a,b，返回a+b ------------")
# 普通方式
def add(x, y):
    return x + y

print(add(3, 4))

# lambda
add = lambda x, y: x + y
print(add(3, 4))

print("------------ 小题：用lambda传三个参数，返回三个参数的乘积并打印出来 ---------")
c = lambda x, y, z: x * y * z
print(c(2, 3, 4))

print("--------------- 在函数内部使用lambda函数 ------------")


# 计算n的m次方：n**m
# def power(n):
#     b = lambda m: n ** m
#     return b

# 计算n的m次方：n**m
def power(n):
    return lambda m: n ** m


"""
n是底数
m是指数
"""

# 2的3次方
b = power(2)
print(b(3))

"""
lambda可以结合map()/reduce()/filter()等内置函数使用
"""
print("---------------- filter()结合lambda，取出列表中的偶数/奇数 -----------")
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# 普通方式
foo_fileter = lambda x: x % 2 == 0
new_foo = []
for i in foo:
    if foo_fileter(i):
        new_foo.append(i)
print("普通方式:", new_foo)

# lambda结合filter()
res = filter(foo_fileter, foo)
print("filter()--1:", list(res))

# 直接将lambda写入filter()函数中
res = filter(lambda x: x % 2 == 0, foo)
print("filter()--2:", list(res))

# 奇数
print("求列表奇数：", list(filter(lambda x: x % 2 != 0, [2, 18, 9, 22, 17, 24, 8, 12, 27])))

print("-------------- filter()结合lambda，取出列表中是3的倍数的元素 -----------")
l = [1, 2, 3, 4, 5, 6]
res = filter(lambda x: x % 3 == 0, l)
print(list(res))

print("-------------- map()结合lambda， 求列表中每个元素的平方 ----------")
numbers = [1, 2, 3, 4, 5]
squared = map(lambda num: num ** 2, numbers)
print(list(squared))

print("-------------- map()结合lambda， 求两个列表对应元素的差 ----------")
l1 = [2, 4, 6]
l2 = [1, 3, 5]
print(list(map(lambda x, y: x - y, l1, l2)))

print("-------------- map()结合lambda， 求三个列表对应元素的和 ----------")
print(list(map(lambda x, y, z: x + y + z, [2, 4, 10], [1, 3, 20], [7, 8, 30])))

print("-------------- reduce()结合lambda， 求列表中所有元素的累加和 ----------")
from functools import reduce
import operator

print(reduce(operator.add, [1, 2, 3, 4, 5]))  # 计算列表和：1+2+3+4+5
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))  # 使用 lambda 匿名函数

print("-------------- reduce()结合lambda， 求列表中所有元素的乘积 ----------")
numbers = [1, 2, 3, 4]
print(reduce(lambda a, b: a * b, numbers))

print("-------------- reduce()结合lambda， 求列表中的最大值/最小值 ----------")
numbers = [3, 5, 2, 4, 7, 1]
print("最小值:", reduce(lambda a, b: a if a < b else b, numbers))
print("最大值:", reduce(lambda a, b: a if a > b else b, numbers))

print("----------- 使用list.sort()函数对列表元素进行排序 -------")
# 排序
numbers = [3, 5, 2, 4, 7, 1]
# 使用列表自带的sort()函数
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# 使用sorted()函数
print(sorted(numbers))
print(sorted(numbers, reverse=True))
# print("------------ filter()举例： 过滤对象是列表B，过滤出既在B列表又在B列表的元素-------------")
#
# A = ['a', 'e', 'i', 'o', 'u']
# B = ['g', 'e', 'z', 'j', 'k', 's', 'u', 'r']
#
#
# def fun(s):
#     """判断s是否在列表A中"""
#     return True if s in A else False
#
#
# filtered = filter(fun, B)
# print(list(filtered))
#
#
# filtered = filter(lambda a:True if a in A else False, B)
# print(list(filtered))

print("----------- 使用list.sort()函数对元组进行排序 ------------")
l = [(2, 2), (3, 4), (4, 1), (1, 3)]


def takes_second(e):
    """获取列表的第二个元素"""
    return e[1]


# 指定第二个元素进行升序排序
l.sort(key=takes_second)
print(l)

# 降序排序
l.sort(key=takes_second, reverse=True)
print(l)

# 使用lambda匿名函数
l.sort(key=lambda l: l[0])
print("lambda匿名函数升序排序：", l)

# 使用lambda，降序排序
l.sort(key=lambda l: l[0], reverse=True)
print("lambda匿名函数降序排序：", l)

print("------------ 使用lambda，按照分数进行降序排序 ------------")
students = [
    ("小明", 600), ("小刚", 601), ("小雅", 524),
    ("小旭", 714), ("小章", 624), ("小白", 635),
    ("小赵", 480), ("小高", 580), ("小王", 542),
    ("小张", 430), ("小李", 590), ("小猴", 492),
]
students.sort(key=lambda x: x[1], reverse=True)
print(students)
