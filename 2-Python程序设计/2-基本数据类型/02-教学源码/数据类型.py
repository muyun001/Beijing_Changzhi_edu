# int类型
a = 1

# str类型
s = "huangboxun"
print(s)

# list类型
names = ["zhangsan","lisi","wangwu"]

# bool类型
# True  -- 1
# False  -- 0

# int(True) 把True转为int类型
print(int(True))  # 1
print(int(False))  # 0

# set集合
"""
set集合
1.无序性
2.使用大括号
3.元素不可重复
"""
s = {"a","b","c","d","a","b"}
print(s)

# 去重
l = ["a","b","c","d","a","b"]
l = list(set(l))

s = set(l)
l = list(s)
print(l)

# dict
# 键值对  -- key-value  -- kv
d = {"name":"zhangsan","age":19, "home":"beijing"}
print(d["home"])

# bytes 电脑能识别到的就是字节流

# 算数运算
a = 67
b = 10
sum = a + b
sum = a - b
sum = a * b
sum = a / b

sum = a // b  # 6  // 是取整操作。求模运算
sum = a % b  # 7  % 是曲余操作。求余运算

a = 2
b = 3
sum = a ** b # 求幂运算。  a^b
print(sum)


# 比较运算
a = 10
b = 20
a > b
a < b
a >= b
a <= b
a == b
a != b

# 赋值运算
a = 10
b = 20
a += b  # 等价于 a = a + b
print(a)
a -= b  # 等价于 a = a - b
a *= b  # 等价于 a = a * b
a /= b  # 等价于 a = a / b
a //= b  # 等价于 a = a // b
a %= b  # 等价于 a = a % b
a **= b  # 等价于 a = a ** b

# 逻辑运算
# and or not
"""
True and True --> True
True and False --> False

True or True --> True
True or False --> True

not True  --> False
not False --> True
"""

# 成员变量
# in 、not in
l = ["a", "c", "b", "d"]
l = "abcd"
print("a" not in l)

# str不可修改
a = "abcd"
print(id(a))
a = "abc"
print(id(a))

# a[start:end]
a = "abcde"
print(a[0:3])
print(a[3:])
print(a[-3:])

# 多行字符串
a = """
abc
def
efg
"""

# 字符串拼接
a = "abc"
b = "def"

print(a+b)

print("a" * 50)

# 列表list
l = [1,2,3,4]
l = ["a","b","c","d"]
l = [[1,2,3,4],[1,2,3,4],["a","c","b","d"]]  # 二维列表

# append
l = [1,2,3,4]
s = 5
l.append(s)  #  将s作为一个元素放入l
print(l)

s = [5]
l.append(s)
print(l)

# extend()
l = [1,2,3,4]
l2 = [3,4,5,6]

# l.extend(l2)   # 将l2中的所有元素放入l
l.append(l2)
print(l)

l[1] = "z"
print(l)

del l[3]
print(l)

# in
print("z" in l)

# input() 可以接受我们使用键盘输入的内容
# name = input("请输入姓名：")
# print("姓名是",name)

# 判断是不是17岁
# age = input("输入年龄：")
# print(type(age))
# age = int(age)
# print(type(age))
# if age == 17:
#     print("是17岁")
# else:
#     print("不是17岁")

print("a",end="")
print("b",end="")
print("c")

# 占位符%
# %s : 替换字符串
# %f : 替换float类型
# %d : 替换int类型
name = "zhangsan"
age = 19
print("name:%s，age:%d" % (name, age))

# format()
print("name:{},age:{}".format(name, age))
print("name:{0},age:{1},name:{0},name:{0}".format(name, age))

# name = input('请输入您的名字：')
# print(f'您输入的名字是{name}')
# print(type(name))
#
# password = input('请输入您的密码：')
# print(f'您输入的密码是{password}')
# print(type(password))

name_list = ['Tom', 'Lily', 'Rose']

name_list.append('xiaoming')

# 结果：['Tom', 'Lily', 'Rose', 'xiaoming']
print(name_list)