import requests
import json

students = [
    {"uid": 3, "name": "吴俊岳", "age": 18, "gender": 1},
    {"uid": 4, "name": "王浩羽", "age": 18, "gender": 1},
    {"uid": 5, "name": "吕梦丽", "age": 18, "gender": 2},
    {"uid": 6, "name": "牛皓冬", "age": 18, "gender": 1},
    {"uid": 7, "name": "张阔", "age": 18, "gender": 1},
    {"uid": 8, "name": "孙佳奇", "age": 18, "gender": 1},
    {"uid": 9, "name": "郑佳睦", "age": 18, "gender": 1},
    {"uid": 10, "name": "王孝天", "age": 18, "gender": 1},
    {"uid": 11, "name": "付一鸣", "age": 18, "gender": 1},
    {"uid": 12, "name": "李蓉轩", "age": 18, "gender": 2},
    {"uid": 13, "name": "陈观绅", "age": 18, "gender": 1},
    {"uid": 14, "name": "赵鑫博", "age": 18, "gender": 1},
    {"uid": 15, "name": "张子豪", "age": 18, "gender": 1},
    {"uid": 16, "name": "叶平", "age": 18, "gender": 1},
]


def add():
    uid = input("请输入uid：")
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    gender = input("请输入性别：")
    if not id or not name or not age or not gender:
        print("任何字段都不可为空！！添加失败!")
        return

    data = {
        "uid": uid,
        "name": name,
        "age": age,
        "gender": gender
    }

    url = "http://127.0.0.1:5000/add"
    response = requests.post(url, data=data)
    print(json.loads(response.text))


def delete():
    uid = input("请输入想删除的uid：")
    url = "http://127.0.0.1:5000/delete/" + uid
    res = requests.get(url)
    print(json.loads(res.text))


def edit():
    uid = input("请输入要编辑的uid：")
    age = input("请输入新的年龄：")
    url = f"http://127.0.0.1:5000/edit?uid={uid}&age={age}"
    res = requests.get(url)
    print(json.loads(res.text))


def query():
    uid = input("请输入要查询的uid：")
    url = f"http://127.0.0.1:5000/query?uid={uid}"
    res = requests.get(url)
    print(json.loads(res.text))


def query_all():
    url = "http://127.0.0.1:5000/user"
    res = requests.get(url)
    print(json.loads(res.text))


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
            add()
        elif num == "2":
            delete()
        elif num == "3":
            edit()
        elif num == "4":
            query()
        elif num == "5":
            query_all()
        elif num == "6":
            # exit_sys()
            break
        else:
            print("输入错误，请重新输入！！")


if __name__ == '__main__':
    # main()
    add()
