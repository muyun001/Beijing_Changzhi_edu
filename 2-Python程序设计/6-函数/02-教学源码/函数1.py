"""
函数
"""

"""
用户管理系统
1。添加用户
2。删除用户
3。更新数据
4。查询
"""

# user_list = ['崔昊元', '贾靖程', '吴俊岳', '王浩羽', '吕梦丽', '李博远', '墨梓恒', '牛皓冬', '张阔', '孙佳奇', '郑佳睦', '王孝天', '付一鸣', '李蓉轩', '陈观绅',
#              '赵鑫博', '张子豪', '叶平']
#
#
# def add_user(name):
#     user_list.append(name)
#     print("现在的用户列表是：", user_list)
#
#
# def delete_user(name):
#     user_list.remove(name)
#     print("删除用户的函数已经完成，现在的用户列表是:", user_list)
#
#
# def update():
#     pass
#
#
# def query():
#     pass
# user_list = ['崔昊元', '贾靖程', '吴俊岳', '王浩羽', '吕梦丽', '李博远', '墨梓恒', '牛皓冬', '张阔', '孙佳奇', '郑佳睦', '王孝天', '付一鸣', '李蓉轩', '陈观绅',
#              '赵鑫博', '张子豪', '叶平']
#
#
# # 形式上的参数：形参
# def add_user(name1, name2):
#     user_list.append(name1)
#     user_list.append(name2)
#
#
# def delete_user():
#     user_list.remove("墨梓恒")
#
#
# # 实际上的参数：实参
# add_user("lisi", "zhangsan")
# print(user_list)

# 调用函数
# add_user()

# 调用函数的时候传递参数
# add_user("wangwu")
# delete_user("zhangsan")

# def aaa(number):
#     print(number ** 3)
#
#
# aaa(5)


# # 参数默认值
# def aaa(number1, number2=5):
#     # print(number1 ** number2)
#     res = number1 ** number2
#     # print(res)
#     return res
#
# result = aaa(2)
# print(result+1)
# a = aaa(3, 5)
# a = aaa(4, 5)
# a = aaa(5, 5)
# a = aaa(6, 5)
# a = aaa(2, 5)
# print(a)


# 函数的返回值
# def aaa(number1, number2=3):
#     # print(number1 ** number2)
#     res = number1 ** number2
#     return res
#
#
# aaa(2, 5)

"""
五一假期任务1：
一：自学钉钉群中"6-函数"文件夹下的三个pdf文件，并将练习源码上传至"作业提交-五一"文件夹下。命名格式：五一_组别_姓名_函数练习源码.py
二：完成以下作业：
1。创建一个函数，实现功能：打印5*6*9的结果。
2。创建一个函数，实现功能：传入2个整型数字，返回它们的和。
3。创建一个函数，可接收三个参数，实现功能：传入3个整型数字，返回它们的平均数。
4。创建一个函数，可接收三个参数，实现功能：传入3个整型数字, 最后一个参数的默认值设置为8，返回3个数字中的最小值。
5。创建一个函数，可接收一个参数，实现功能：传入1个列表（元素都是整型数字），将列表中的每个元素+1，并返回结果。
6。创建一个函数，可接收两个参数，实现功能：传入2个列表，将这2个列表中的元素放到一个列表中，并返回结果。
7。创建一个函数，使用可变参数，实现功能：传入2个列表，将这2个列表中的元素放到一个列表中，并返回结果。
8。创建一个函数，可接收一个参数，实现功能：传入1个列表，返回字典{"max":最大值,"min":最小值}
9。创建一个函数，可接收一个参数，实现功能：传入1个列表，返回字典{"max":最大值,"min":最小值}

# 重点是理解匿名函数（lambda）、内置高阶函数（map、reduce、filter、zip）的含义和用法
我把一些练习源码放到文件夹中，大家去练习，返校之后会【随机】请同学上台讲解。
"""
"""
1。创建一个函数，实现功能：打印5*6*9的结果。
"""

# def fun1():
#     """ 打印5*6*9的结果 """
#     print(5 * 6 * 9)
#
#
# fun1()
#
# """
# 2.创建一个函数，实现功能：传入2个整型数字，返回它们的和。
# """
#
#
# def fun2(number1, number2):
#     """
#     传入2个整型数字，返回它们的和
#     number1: 第一个整型数字
#     number2: 第二个整型数字
#     return: 两个整型数字的和
#     """
#     return number1 + number2
#
#
# print(fun2(1, 2))
#
# """
# 3。创建一个函数，可接收三个参数，实现功能：传入3个整型数字，返回它们的平均数。
# """
#
#
# def fun3(number1, number2, number3):
#     """
#     传入3个整型数字，返回它们的平均数
#     """
#     return (number1 + number2 + number3) / 3
#
#
# avg_num = fun3(1, 2, 3)
# print(avg_num)
#
# """
# 4。创建一个函数，可接收三个参数，实现功能：传入3个整型数字, 最后一个参数的默认值设置为8，返回3个数字中的最小值。
# """
#
#
# def fun4(num1, num2, num3=8):
#     """传入3个整型数字, 最后一个参数的默认值设置为8，返回3个数字中的最小值。"""
#     return min([num1, num2, num3])
#
#
# min_num = fun4(9, 10, 6)
# print(min_num)
#
# """
# 5。创建一个函数，可接收一个参数，实现功能：传入1个列表（元素都是整型数字），将列表中的每个元素+1，并返回结果。
# """
#
#
# def fun5(li):
#     """传入1个列表（元素都是整型数字），将列表中的每个元素+1，并返回结果"""
#
#     # new_list = []
#     # for i in li:
#     #     new_list.append(i + 1)
#     # return new_list
#     return [i + 1 for i in li]
#
#
# new_list = fun5([1, 2, 3])
# print(new_list)
#
# """
# 6。创建一个函数，可接收两个参数，实现功能：传入2个列表，将这2个列表中的元素放到一个列表中，并返回结果。
# """
#
#
# def fun6(li1, li2):
#     """传入2个列表，将这2个列表中的元素放到一个列表中，并返回结果"""
#     li1.extend(li2)
#     return li1
#
#
# l1 = [1, 2, 3]
# l2 = [2, 3, 4]
# new_list = fun6(l1, l2)
# print(new_list)
#
# print(l1.extend(l2))  # 返回结果为空
#
# """
# 7。创建一个函数，使用可变参数，实现功能：传入2个列表，将这2个列表中的元素放到一个列表中，并返回结果。
# """
#
#
# def fun7(*args):
#     """传入2个列表，将这2个列表中的元素放到一个列表中，并返回结果"""
#     tup = args[0]  # ([1, 2, 3], [2, 3, 4])
#     # print(tup)
#     l1 = tup[0]
#     l2 = tup[1]
#     l1.extend(l2)
#     return l1
#
#
# l1 = [1, 2, 3]
# l2 = [2, 3, 4]
# print(fun7((l1, l2)))
#
# """
# 8。创建一个函数，可接收一个参数，实现功能：传入1个列表，返回字典{"max":最大值,"min":最小值}
# """
#
#
# def fun8(li):
#     """传入1个列表，返回字典{"max":最大值,"min":最小值}"""
#     min_num = min(li)
#     max_num = max(li)
#     return {"max": max_num, "min": min_num}
#
#
# lis = [1, 2, 3, 4, 5]
# print(fun8(lis))

"""
可变参数
"""

# def fun10(name, *nums):
#     # num1, num2, num3 = nums
#     print(name)
#     print(nums)
#
#
# fun10(1, 2, 3, 4, 5)

"""
制作披萨
1。尺寸、种类（水果披萨、牛肉披萨等）、酱料、.........
"""

# def make_pizza(size, kouwei, *toppings):
#     """
#     制作披萨
#     toppings: 配料
#     """
#     print(f"尺寸是{size}")
#     print(f"口味是{kouwei}")
#     for t in toppings:
#         print(t)
#
#
# make_pizza(14, "水果披萨", "蕃茄酱", "xxx", "xxxxx", "xxxxxx")

"""
带有关键词的可变参数
** 可以把关键词和值都获取到。
获取key-value，及键值对
"""

# def person_info(name, age, **kw):
#     print('name:', name, 'age:', age, 'ps:', kw)
#
#
# person_info('张三', 22)  # name: 张三 age: 22 ps: {}
# person_info('张三', 23, city='上海')  # name: 张三 age: 23 ps: {'city': '上海'}
# person_info('张三', 23, gender='男', city='上海')  # name: 张三 age: 23 ps: {'gender': '男', 'city': '上海'}
# person_info('张三', 23, gender='男', city='上海', sroce=98)  # name: 张三 age: 23 ps: {'gender': '男', 'city': '上海'}


"""
可变参数：在创建函数的时候不知道会传入多个参数，所以写称可变的参数
*
"""

# def fun11(*student_info):
#     """ 学生信息 """
#
#     for i in student_info:
#         print(i)
#
#
# fun11("牛皓冬", 18, "男", "123456", 90)


# def fun11(name, age, *other_info):
#     """ 学生信息 """
#     print(name)
#     print(age)
#     for i in other_info:
#         print(i)
#
#
# fun11("牛皓冬", 18, "男", "123456", 90, "xxxxxx")


"""
可变参数的升级版：可以将关键词一块传入
**
"""
"""
{'name': '牛皓冬', 'age': 18, 'gender': '男', 'qizhong_score': 90, 'qimo_score': 50}

键值对
key-value
k-v

{
 'name': '牛皓冬',
 'age': 18,
 'gender': '男',
 'qizhong_score': 90,
 'qimo_score': 50
}
"""


# def fun12(name, age, **student_info):
#     """学生信息"""
#     print(name)
#     print(age)
#     print(student_info)
#
#
# # key-value 键值对
# fun12(name="牛皓冬", age=18, gender="男", qizhong_score=90, qimo_score=50)

"""
对字典进行遍历
"""
# student_info = {'name': '牛皓冬', 'age': 18, 'gender': '男', 'qizhong_score': 90, 'qimo_score': 50}
# print(student_info)  # {'name': '牛皓冬', 'age': 18, 'gender': '男', 'qizhong_score': 90, 'qimo_score': 50}
# 对字典的key进行遍历
# for k in student_info.keys():
#     print(k)

# 对字典的value进行遍历
# for v in student_info.values():
#     print(v)

# 对字典的key-value进行遍历
# for k, v in student_info.items():
#     print(f'{k}-{v}')
