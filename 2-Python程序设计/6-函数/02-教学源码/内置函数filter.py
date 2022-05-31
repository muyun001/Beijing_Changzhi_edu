""""""
"""
filter():过滤器
    - 功能： 过滤可迭代对象中不符合条件的元素，返回由符合条件的元素组成的新的迭代器。
            filter() 把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False，来决定保留或丢弃该元素。
    - 语法：filter(函数，可迭代参数)
        - 用于实现判断的函数，可以为 None。
        - 可迭代对象，如列表、range 对象等
        - 返回值：返回一个迭代器对象
"""
print("------------ filter()举例：过滤出列表中的所有偶数 -----------")
l = [0, 1, 2, 3, 5, 8, 13]
even_numbers = []


# 普通方式
def is_even_number(i):
    """判断i是不是偶数"""
    # 第一种写法：
    # if i % 2 == 0:
    #     return True
    # return False

    # 第二种写法：
    # return  i % 2 == 0

    # 第三种写法：
    return i % 2 == 0


for i in l:
    if is_even_number(i):
        even_numbers.append(i)

print("1 oushu_l:", even_numbers)

# filter()方式
f = filter(is_even_number, l)
print("2 oushu_l:", list(f))

# print("------------ filter()举例：过滤出列表中的所有奇数 -----------")
# l = [0, 1, 2, 3, 5, 8, 13]
# odd_numbers = []
#
#
# # 普通方式
# def is_odd_number(i):
#     """判断i是不是奇数"""
#     return i % 2 != 0
#
#
# for i in l:
#     if is_odd_number(i):
#         odd_numbers.append(i)
# print(odd_numbers)
#
# # filter()方式
# f = filter(is_odd_number, l)
# print(list(f))

print("------- filter()举例：过滤出 0~100 (包括 100) 之间的所有奇数 ---------")


def is_odd_number(i):
    """判断i是不是奇数"""
    return i % 2 != 0


f = filter(is_odd_number, range(101))
print(list(f))

print("------- filter()举例：筛选出列表中大于18的元素 -------------")
l = [5, 12, 17, 18, 24, 32]


def my_func(x):
    return x > 18


f = filter(my_func, l)
print(list(f))

print("------------ filter()举例： 过滤对象是列表B，过滤出既在B列表又在B列表的元素-------------")

A = ['a', 'e', 'i', 'o', 'u']
B = ['g', 'e', 'z', 'j', 'k', 's', 'u', 'r']


def fun(s):
    """判断s是否在列表A中"""
    return s in A


filtered = filter(fun, B)
print(list(filtered))

print("-------------- filter()举例：筛选出分数高于600的学生 ------------")
students = [
    ("小明", 600), ("小刚", 601), ("小雅", 524),
    ("小旭", 714), ("小章", 624), ("小白", 635),
    ("小赵", 480), ("小高", 580), ("小王", 542),
    ("小张", 430), ("小李", 590), ("小猴", 492),
]

# 普通方式
high_score_students = []
for s in students:
    if s[1] >= 600:
        high_score_students.append(s)
print(high_score_students)


# filter()方式
def is_high(i):
    """超过600分返回True，否则返回False"""
    return i[1] >= 600


f = filter(is_high, students)
print(list(f))

print("-------------- filter()举例：筛选出分数低于500的学生 ------------")
# 普通方式

# filter()方式


print("--------------- filter()举例：找出列表中为'True'的元素--------------")
l = [None, "", "py", [], [1, 2, 3], 0, 10, {}, {"name": "张三"}]
f = filter(bool, l)
print(list(f))

# 引出
if not "":
    print(1)
else:
    print(2)

# print("--------------- filter()举例：--------------")
#
#
# class Course:
#     """
#     课程类
#     """
#     def __init__(self, course_id):
#         self.course_id = course_id
#
#
# def is_chosed(course_id):
#     course = list(filter(lambda c: c.course_id == course_id, course_list))
#     if len(course) > 0:
#         return True
#     return
#
#
# if __name__ == '__main__':
#     course_list = []
#     for i in range(1, 10):
#         course_list.append(Course(i))
#
#     print(is_chosed(7))
#     print(is_chosed(10))
