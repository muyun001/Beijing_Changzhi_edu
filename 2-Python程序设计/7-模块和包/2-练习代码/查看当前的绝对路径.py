import os
# 获取当前绝对路径
print(os.getcwd()) #E:\my_python\guangmao_class2\day13
# 获取当前的上级绝对路径
print(os.path.dirname(os.getcwd())) #E:\my_python\guangmao_class2
# 获取当前目录的上上级路径
print(os.path.dirname(os.path.dirname(os.getcwd()))) #E:\my_python
my_path = os.path.dirname(os.path.dirname(os.getcwd()))
# E:\my_python 创建test.txt文件 E:\my_python\test.txt

# with open(my_path+"\\test.txt", "w") as f:
#     f.write("asdfasdfasf")
# 拼接文件地址 ，如果牵扯到路径拼接，尽量使用os.path.join
new_file = os.path.join(my_path, "my_test", "test.txt")
# 判断文件夹是否存在，不存在，使用os模块创建文件夹
if not os.path.exists(os.path.join(my_path, "my_test")):
    os.mkdir(os.path.join(my_path, "my_test"))
print(new_file)
# open 以写文件的方式打开文件，文件不存在会创建文件，
# 但是文件夹如果不存在，不会创建文件夹，会报错
with open(new_file, "w") as f:
    f.write("asaaaaaaaaaaaaa")