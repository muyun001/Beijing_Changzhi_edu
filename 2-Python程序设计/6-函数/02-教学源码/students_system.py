# 学生管理系统

# 定义功能界⾯函数
def info_print():
    print('---------- 请选择功能 ------------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('-' * 20)
    # 等待存储所有学员的信息


students = list()


def add_info():
    """添加学员函数"""

    # 1. ⽤户输⼊：学号、姓名、⼿机号
    new_id = input('请输⼊学号：')
    new_name = input('请输⼊姓名：')
    new_tel = input('请输⼊⼿机号：')
    # 2. 判断是否添加这个学员：如果学员姓名已经存在报错提示；如果姓名不存在添加数据
    global students
    # 2.1 不允许姓名重复：判断⽤户输⼊的姓名 和 列表⾥⾯字典的name对应的值 相等 提示
    for i in students:
        if new_name == i['name']:
            print('此⽤户已经存在')
            # return作⽤：退出当前函数，后⾯添加信息的代码不执⾏
            return
    # 2.2 如果输⼊的姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    info_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}
    # print(info_dict)
    # 列表追加字典
    students.append(info_dict)
    print(students)


def del_info():
    """删除学员"""
    # 1. ⽤户输⼊要删除的学员的姓名
    del_name = input('请输⼊要删除的学员的姓名：')
    # 2. 判断学员是否存在：存在则删除；不存在提示
    # 2.1 声明info是全局变量
    global students
    # 2.2 遍历列表
    for i in students:
        # 2.3 判断学员是否存在：存在执⾏删除(列表⾥⾯的字典)，break：这个系统不允许重名，删除了⼀个后
        # ⾯的不需要再遍历；不存在提示
        if del_name == i['name']:
            # 列表删除数据 -- 按数据删除remove
            students.remove(i)
            break
    else:
        print('该学员不存在')
        print(students)


def modify_info():
    """修改学员信息"""
    # 1. ⽤户输⼊想要修改的学员您的姓名
    modify_name = input('请输⼊要修改的学员的姓名：')
    # 2. 判断学员是否存在：存在修改⼿机号；不存在，提示
    # 2.1 声明info是全局
    global students
    # 2.2 遍历列表，判断输⼊的姓名==字典['name']
    for i in students:
        if modify_name == i['name']:
            # 将tel这个key修改值，并终⽌此循环
            i['tel'] = input('请输⼊新的⼿机号：')
            break
    else:
        # 学员不存在
        print('该学员不存在')
        # 3. 打印info
        print(students)


# 查询学员信息函数
def search_info():
    """查询学员信息"""
    # 1. ⽤户输⼊⽬标学员姓名
    search_name = input('请输⼊要查询的学员的姓名：')
    # 2. 检查学员是否存在：存在打印这个学员的信息；不存在则提示
    # 2.1 声明info为全局
    global students
    # 2.2 遍历info，判断输⼊的学员是否存在
    for i in students:
        if search_name == i['name']:
            # 学员存在：打印信息并终⽌循环
            print('查询到的学员信息如下---------------')
            print(f"学员的学号是{i['id']}, 姓名是{i['name']}, ⼿机号是{i['tel']}")
            break
    else:
        # 学员不存在的提示
        print('查⽆此⼈...')


# 显示所有学员信息
def print_all():
    """显示所有学员信息"""

    # 1. 打印提示字
    print('学号\t姓名\t⼿机号')
    # 2. 打印所有学员的数据
    for i in students:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


while True:
    # 1. 显示功能界⾯
    info_print()
    # 2. ⽤户输⼊功能序号
    user_num = input('请输⼊功能序号：')
    # 3. 按照⽤户输⼊的功能序号，执⾏不同的功能(函数)
    # 如果⽤户输⼊1，执⾏添加；如果⽤户输⼊2，执⾏删除... -- 多重判断
    if user_num == "1":
        add_info()
    elif user_num == "2":
        del_info()
    elif user_num == "3":
        modify_info()
    elif user_num == "4":
        search_info()
    elif user_num == "5":
        print_all()
    elif user_num == "6":
        # print('退出系统')
        # 程序要想结束，退出终⽌while True -- break
        exit_flag = input('确定要退出吗？yes or no')
        if exit_flag == 'yes':
            break
    else:
        print('输⼊的功能序号有误')
