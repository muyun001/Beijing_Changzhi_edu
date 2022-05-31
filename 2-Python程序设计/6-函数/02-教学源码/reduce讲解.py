"""
reduce(): 减少；归纳为
    - 功能：对参数序列中元素进行累积。
    - 语法：reduce(函数, 可迭代对象, 初始参数)
        - 函数：用于实现判断的函数，可以为 None。
        - 可迭代对象：如列表、range 对象等
        - 初始参数：可选
        - 返回值：返回一个值
    - 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
    得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
"""

print("--------- reduce()举例： 把列表中的所有元素累加 ------------")
# 普通方式

# l = [1, 2, 3, 4, 5, 6]
# print(sum(l))

# l = [1, 2, 3, 4, 5, 6]
# sum = 0  # 累加器 accumulator
# for i in l:
#     sum += i
# print(sum)
from functools import reduce

# 普通方式2
# l = [1, 2, 3, 4, 5, 6]
# sum = 0
#
#
# def my_add(x, y):
#     return x + y
#
#
# for i in l:
#     sum = my_add(sum, i)
# print(sum)


# reduce()方式
# def my_add(x, y):
#     result = x + y
#     print(f"{x}+{y}={result}")
#     return result
#
#
# l = [1, 2, 3, 4, 5, 6]
# r = reduce(my_add, l)
# print(r)

# reduce方式，使用operator.add()内置方法
# l = [1, 2, 3, 4, 5, 6]
# r = reduce(operator.add, l)
# print(r)

print('----------------- reduce: 1-100的和 ---------------')


def my_add(x, y):
    result = x + y
    print(f"{x}+{y}={result}")
    return result


r = reduce(my_add, range(0, 100 + 1))
print(r)

# 设置初始值
r = reduce(my_add, range(0, 100 + 1))
print(r)
