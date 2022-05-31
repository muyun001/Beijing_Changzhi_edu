"""
map()
    - map(）是一个python内置函数，你可以不使用循环就对'可迭代对象'中的元素进行遍历操作。
    - 使用形式：map(函数, 可迭代对象)
        - 可迭代对象：列表、字典、元组等等
        - 可迭代对象：可以使用for循环进行遍历的对象
    - 返回值：map对象
"""
# print("------------- map举例：将列表中所有元素+1 -------------")
# # 方法一
# nums = [1, 2, 3, 4, 5]
# new_nums = []
#
# for i in nums:
#     new_nums.append(i + 1)
#
# print(new_nums)

# 方法二
import struct

"""
new_nums = [2]
new_nums = [2, 3]
new_nums = [2, 3, 4]
new_nums = [2, 3, 4, 5]
new_nums = [2, 3, 4, 5, 6]
"""
# nums = [1, 2, 3, 4, 5]
# new_nums = [i+1 for i in nums]
# print(new_nums)
#
#
# # 方式三
# nums = [1, 2, 7, 4, 5]
#
#
# def add_one(num):
#     res = num + 1
#     print(num)
#     return res
#
#
# m = map(add_one, nums)  # <map object at 0x7fe9a21f8eb0>
# result = list(m)  # list[]  -- [2, 3, 4, 5, 6]
# print(result)

print("------------- map：使用三种方式，将列表中所有元素 * 3 -------------")
# 方式一
# nums = [1, 2, 7, 4, 5]
# new_nums = []
# for i in nums:
#     new_nums.append(i * 3)
# print(new_nums)

# 方式二
# nums = [1, 2, 7, 4, 5]
# new_nums = [i * 3 for i in nums]
# print(new_nums)

# 方式三
# nums = [1, 2, 7, 4, 5]
#
#
# def fun1(num):
#     return num * 3
#
#
# m = map(fun1, nums)
# print(list(m))

"""
map流程：
map：一对一的映射
"""

# print("-------------- map举例： 列表中每个str转为int, 使用内置函数int --------------")
# str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
#
# m = map(int, str_nums)  # map对象  <map object at 0x7f99a220ff10>
# print(list(m))  # [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
#
#
# print("-------------- map举例：列表中每个负数转为正数 ---------------")
# nums = [-1, -2, 0, 5, 6, -4]
# m = map(abs, nums)  # map对象
# print(list(m))

"""
题目：
求列表中每个数字的平方
需要自定义函数：求一个值的平方
使用map调用此函数，完成对列表中的每个元素求平方的功能
"""
# nums = [-1, -2, 0, 5, 6, -4]
# # def square(num):
# #     """ 求平方 """
# #     return num ** 2
#
# # m = map(square, nums)
# # m = map(abs, nums)
# m = map(str, nums)
# print(list(m))
#
# nums1 = [-1, -2, 0, 5, 6, -4]
# nums2 = [1, 2, 3, 4, 5, 6]
#
#
# def add(num1, num2):
#     return num1 + num2
#
#
# m = map(add, nums1, nums2)
# print(list(m))


print("---------- map举例：去掉每个元素中的空格 -----------")
with_spaces = ["processing ", "  strings", "with   ", " map   "]

# 去空格：str.strip()
# lstrip()   left
# rstrip()   right
# 方式一
new_list = []
for i in with_spaces:
    new_list.append(i.strip())
print(new_list)

# 方式二
new_list = [i.strip() for i in with_spaces]
print(new_list)

new_list = [i.strip() for i in with_spaces if i.strip()]
print(new_list)

# map方式
def delete_space(s):
    return s.strip()

m = map(delete_space, with_spaces)
print(list(m))


# str.strip()
m = map(str.strip, with_spaces)
print(list(m))
