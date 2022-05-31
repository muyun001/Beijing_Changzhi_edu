""""""
"""
map()
    - map(）是一个python内置函数，你可以不使用循环就可以编写简洁的代码。
    - 使用形式：map(函数, 可迭代对象)
        - 可迭代对象：列表、字典、元组等等
    - 返回值：map对象
"""
print("-------------- map举例： 列表中每个str转为int, 使用内置函数int --------------")
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
m = map(int, str_nums)
print(list(m))

print("-------------- map举例：列表中每个负数转为正数 ---------------")
nums = [-1, -2, 0, 5, 6, -4]
m = map(abs, nums)
print(list(m))

print("---------- map举例：求列表中每个数字的平方 -----------")


def square(x):
    """求x的平方"""
    return x ** 2


l = [1, 2, 3]
m = map(square, l)
print(m)  # <map object at 0x7feaeaf91ca0>
print(list(m))  # [1, 4, 9]

print("---------- map举例：求2个列表中相对应数字的乘积 -----------")
l_1 = [1, 2, 3]
l_2 = [3, 4, 5]


def chengji(x, y):
    """求乘积"""
    return x * y


m = map(chengji, l_1, l_2)
print(list(m))

print("---------- map举例：列表中每个元素改成大写 -----------")
# 普通方式
ds = ["a", "b", "c", "d", "e", "f"]
ds_upper = []
for direction in ds:
    d = direction.upper()
    ds_upper.append(d)
print(ds_upper)


# 使用map方式1
def to_upper(s):
    return s.upper()


ds_upper = map(to_upper, ds)
print(list(ds_upper))

# 使用map方式2
ds_upper = map(str.upper, ds)
print(list(ds_upper))

# # map使用匿名函数lambda
# ds_upper = map(lambda s: s.upper(), ds)
# print(list(ds_upper))

print("---------- map举例：列表中每个元素改成小写 -----------")
ds = ["D", "A", "Z", "EAST", "WEST", "NORTH", "SOUTH"]
m = map(str.lower, ds)
print(list(m))

print("---------- map举例：去掉每个元素中的空格 -----------")
with_spaces = ["processing ", "  strings", "with   ", " map   "]
print(list(map(str.strip, with_spaces)))

print("-------------- map举例： 取字典中key值 ---------------")
d = {1: 2, 2: 3, 3: 4}
print(list(map(int, d)))
print([i for i, j in d.items()])
