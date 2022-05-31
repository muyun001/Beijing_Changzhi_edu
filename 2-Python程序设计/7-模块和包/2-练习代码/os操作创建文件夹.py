# 创建20 30个文件夹，
# 每个文件夹中都有 代码 工学资料 课件+笔记 视频
import os
# 找到上级绝对路径
creat_path = os.path.dirname(os.getcwd())
print(creat_path)
# 循环传创建10个文件夹
for i in range(1, 31):
    # 定义文件夹名称
    dir_name = "day%s" % i
    # 拼接创建新文件夹的绝对路径
    dir_path = os.path.join(creat_path, dir_name)
    # 如果不存在创建文件夹，并在文件夹中创建相应的文件夹
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        os.mkdir(os.path.join(dir_path, "代码"))
        os.mkdir(os.path.join(dir_path,  "工学资料"))
        os.mkdir(os.path.join(dir_path, "课件+笔记"))
        os.mkdir(os.path.join(dir_path, "视频"))


