"""
1、添加学生
2、删除学生
3、修改
4、查询(有条件的查询)
5、查询所有
6、退出系统
"""

"""
学生字段：
id、姓名、年龄、性别、手机号
"""
# student_list = []
student_list = [
    {'id': '1', 'name': '1', 'age': '1', 'gender': '1', 'tel': '1'},
    {'id': '2', 'name': '2', 'age': '2', 'gender': '2', 'tel': '2'},
    {'id': '3', 'name': '3', 'age': '3', 'gender': '3', 'tel': '3'},
    {'id': '4', 'name': '4', 'age': '4', 'gender': '4', 'tel': '4'},
]


def add_s():
    """添加学生"""
    id = input("请输入id：")
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    gender = input("请输入性别：")
    tel = input("请输入手机号：")
    if not id or not name or not age or not gender or not tel:
        print("任何字段都不可为空！！添加失败!")
        return

    new_s = {"id": id, "name": name, "age": age, "gender": gender, "tel": tel}
    student_list.append(new_s)


def delete_s():
    """删除学生"""
    id = input("请输入要删除的学生的id：")
    for s in student_list:
        if s["id"] == id:
            student_list.remove(s)
            return

    print("没有这个人！！！")


def update_s():
    """修改"""
    # {'id': '1', 'name': '1', 'age': '1', 'gender': '1', 'tel': '1'},
    id = input("请输入要修改学生的id：")
    for s in student_list:
        if s["id"] == id:
            tel = input("请输入新的手机号：")
            s["tel"] = tel
            return

    print("没有这个人！！")


def query_s():
    """查询"""
    id = input("请输入要修改学生的id：")
    for s in student_list:
        if s["id"] == id:
            print(s)
            return

    print("没有这个人！！")


def query_all():
    """查询所有学生"""
    for s in student_list:
        print(s)


def main():
    input("---------- 欢迎来到学生管理系统，按Enter键继续 ------------")
    while True:
        print('--------------')
        print("1、添加学生")
        print("2、删除学生")
        print("3、修改")
        print("4、查询")
        print("5、查询所有")
        print("6、退出系统")
        print('--------------')

        num = input("请输入功能序号：")
        if num == "1":
            add_s()
        elif num == "2":
            delete_s()
        elif num == "3":
            update_s()
        elif num == "4":
            query_s()
        elif num == "5":
            query_all()
        elif num == "6":
            # exit_sys()
            break
        else:
            print("输入错误，请重新输入！！")


if __name__ == '__main__':
    main()
    # add_s()
    # print(student_list)
    # delete_s()
    # update_s()
    # print(student_list)
