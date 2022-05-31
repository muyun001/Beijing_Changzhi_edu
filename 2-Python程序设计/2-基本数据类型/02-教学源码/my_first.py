#数值类型： int
#字符串类型：str
#定义方式：1.单引号 ''  2.双引号""
my_str = '我们都"是一家人'
print(my_str)
my_num = "12"
count = 2
#字符串的拼接 +
my_name = "小明"
str1 = "正在学python"
#字符串拼接后 必须赋值给变量
str2 = my_name +str1
print(str2)
print(my_name *2)
my_name3 = my_name *3
print("name_name3=",my_name3)
#count + my_num
# 使用type() 查看变量类型
my_num = "12"
count = 2
print("my_num类型",type(my_num))
print("count类型",type(count))
print("int转化后my_num类型",type(int(my_num)))
my_name = "小明"
print("my_name类型",type(my_name))
#print("int转化后my_name类型",type(int(my_name)))
print("str转化后count类型",type(str(count)))
count = 12
my_name = "小明"
str3 = str(count) + my_name
print(str3)

