# 小测试

# a = [1, 2, 3, 4, 5, 6, 7]

# 把[1，2，3]单独取出
# 使用切片 [start:end]

# print(a[0:3])  # 左闭右开

# a = ["a", "b", "c", "d", "e", "f", "g"]
# 把["a", "b", "c"]单独取出
# print(a[0:3])
# 把["b", "c", "d"]单独取出
# print(a[1:4])

# 把[ "e", "f", "g"]单独取出
# print(a[4:7])
# print(a[4:])

# print(a[-3:])
# print(a[-7:-4])


# 字符串的切片

# s = "Hello CPVS!"  # 11
# print("长度为：", len(s))
# # 把CPVS单独取出
# print(s[6:9])   # CPV
# print(s[6:10])  # CPVS

# 把o C单独取出
# print(s[5:7])
# print(s[4:7])
# 负数的方式取出
# print(s[-4:-7])
# print(s[-3:])
# print(s[-7:-4])

# 占位符
# a = "黄博勋"
# ss = "姓名：%s"
# print(ss % a)

# a = 10
# ss = "年龄: %d"
# print(ss % a)  # 年龄：10

# score = 98.5
# ss = "score: %f"
# print(ss % score)
# score = 98.5
# ss = "score: %.1f"  # 精确到小数点后1位
# ss = "score: %.2f"  # 精确到小数点后2位
# print(ss % score)

# format函数
# a = "黄博勋"
# ss = "姓名：{}"
# print(ss.format(a))

# age = 16
# ss = "age:{}"
# print(ss.format(age))

# score = 98.4
# ss = "score:{}"
# print(ss.format(score))

# name = "顾同"
# age = 18
# score = 98.7
# ss = "name:{}, age: {}, score: {}"

# 想要的结果："name:顾同, age: 18, score: 98.7"
# print(ss.format(name, age, score))
# print(ss.format(name), format(age), format(score))


# "".format()


# name = "顾同"
# age = 18
# score = 98.7
# ss = "name:{2}, age: {0}, score: {1}"
# # print(ss.format(name, score, age))
# print(ss.format(age, score, name))


name = "顾同"
age = 18
score = 98.7
ss = "name:{name}, age: {age}, score: {score}"
# print(ss.format(name, score, age))
# print(ss.format(b=age, c=score, a=name))
print(ss.format(name=name, age=age, score=score))

# 自己的姓名、年龄、性别、家庭地址，使用%占位符和format函数分别打印出来
# 使用切片把上述的字符串的第5到第12个字符取出来。
