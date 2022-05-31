from functools import reduce
import operator

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

l = [1, 2, 3, 4, 5, 6]
print(sum(l))
sum = 0  # 累加器 accumulator
for i in l:
    sum += i
print(sum)

# 普通方式2
l = [1, 2, 3, 4, 5, 6]
sum = 0


def my_add(x, y):
    return x + y


# operator.add()

for i in l:
    sum = my_add(sum, i)
print(sum)


# reduce()方式
def my_add(x, y):
    result = x + y
    print(f"{x}+{y}={result}")
    return result


l = [1, 2, 3, 4, 5, 6]
r = reduce(my_add, l)
print(r)

# reduce方式，使用operator.add()内置方法
l = [1, 2, 3, 4, 5, 6]
r = reduce(operator.add, l)
print(r)

print("-------- reduce()举例： 添加初始参数100，再累加为一个值 -----------")


def my_add(x, y):
    result = x + y
    print(f"{x}+{y}={result}")
    return result


l = [1, 2, 3, 4, 5, 6]
r = reduce(my_add, l, 100)
print(r)

print("--------- reduce() 举例：求0-100的值 -----------")


def add(x, y):
    return x + y


print("方法1：", reduce(add, range(0, 101)))

# 使用operator.add(x, y):求x+y
print("方法2：", reduce(operator.add, range(0, 101)))

# 小拓展:
# operator.add()可以拼接字符串
print(operator.add("hel", "lo"))
# operator.mul(x, y) :求x * y
print(operator.mul(3, 9))

print("-------- reduce()举例: 求字典中所有人年龄的累加和 ---------------")
ps = ({'name': '张三', 'age': 45, 'gender': 'male'},
      {'name': '李四', 'age': 76, 'gender': 'male'},
      {'name': '王武', 'age': 202, 'gender': 'female'},
      {'name': '陈六', 'age': 84, 'gender': 'female'})
sum_age = 0

# 普通方式
for i in ps:
    sum_age += i["age"]
print(sum_age)


# reduce()方式
def my_add(e1, e2):
    """求和"""
    sum_age = e1 + e2['age']
    print(f"{e1}+{e2['age']}={sum_age}")
    return sum_age


total_age = reduce(my_add, ps, 0)
print(total_age)

print("------------ reduce()举例: 把字典中男性和女性人员分别取出，放到列表中 ----------------")

ps = ({'name': '张三', 'age': 45, 'gender': 'male'},
      {'name': '李四', 'age': 76, 'gender': 'male'},
      {'name': '王武', 'age': 202, 'gender': 'female'},
      {'name': '陈六', 'age': 84, 'gender': 'female'})

# 普通方式
d = {'male': [], 'female': []}
for i in ps:
    if i["gender"] == "male":
        d['male'].append(i["name"])
    else:
        d["female"].append(i["name"])
print(d)


# reduce()方式
# 函数1
def my_group(s1, s2):
    if s2["gender"] == "male":
        s1["male"].append(s2["name"])
    else:
        s1["female"].append(s2["name"])
    print(s1)
    return s1


# 函数2
# def my_group(e1, e2):
#     print(e1)
#     e1[e2["gender"]].append(e2["name"])
#     return e1


d = {'male': [], 'female': []}
grouped = reduce(my_group, ps, d)
print(grouped)

print("---------- reduce()举例：求列表中的最大值 -----------")


def my_max_func(a, b):
    """返回a,b中较大的值"""
    return a if a > b else b


numbers = [3, 5, 2, 4, 7, 19]

# 普通方式
max_num = 0
for n in numbers:
    max_num = my_max_func(n, max_num)
print(max_num)

# reduce()方式
r = reduce(my_max_func, numbers)
print(r)

# 内置函数max()
print(max(numbers))

print("----------- reduce()举例：求列表中的最小值 ------------")
# 内置函数min()
print(min(numbers))
