from flask import Flask, render_template, request, session, redirect
import time

app = Flask(__name__)
app.secret_key = "abcdefg"

students_info = [
    {'id': 1, 'name': 'alex', 'age': 22, 'sex': 'male', 'score': 88},
    {'id': 2, 'name': 'egon', 'age': 18, 'sex': 'male', 'score': 87},
    {'id': 3, 'name': 'xiaoming', 'age': 16, 'sex': 'female', 'score': 60},
    {'id': 4, 'name': 'wangwei', 'age': 31, 'sex': 'male', 'score': 13},
]


# def is_logined(func):
#     def inner(*args, **kwargs):
#         if session.get("is_login"):
#             if session["is_login"] + 3000 * 60 > time.time():
#                 return func(*args, **kwargs)
#             else:
#                 return "用户登录已过期"
#         return "你没有权限访问这个页面"
#
#     inner.__name__ = func.__name__
#     return inner


@app.route('/')
def hello_world():
    return redirect('/students_manage')


@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # 这里日后使用数据库存储管理员信息
        if username == "alex" and password == "123":
            session["is_login"] = time.time()
            return redirect("/students_manage")
        else:
            msg = "用户名或密码错误"
            return render_template("login.html", msg=msg)


@app.route("/students_manage")
# @is_logined
def students_manage():
    print(students_info)
    return render_template("students_manage.html", students=students_info)


@app.route("/student_add", methods=("GET", 'POST'))
# @is_logined
def student_add():
    if request.method == "GET":
        return render_template("student_add.html")
    else:
        print(request.form)
        user_dict = dict(request.form)
        # 前端处理数据，后端直接将数据存入内存
        if len(students_info):
            current_id = students_info[-1]["id"] + 1
        else:
            current_id = 1
        user_dict["id"] = current_id
        try:
            user_dict["age"] = int(user_dict["age"])
            user_dict["score"] = int(user_dict["score"])
        except ValueError:
            return "输入信息不正确"
        print(user_dict)
        students_info.append(user_dict)
        return redirect("/students_manage")


@app.route("/delete", methods=("GET", "POST"))
# @is_logined
def student_delete():
    # 1.获取删除的id
    # 2.删除数据
    # 3.重定向到学生管理界面
    del_ids = []
    if request.args.get("id"):
        del_id = int(request.args.get("id"))
        del_ids.append(del_id)
    elif request.json:
        del_ids = request.json
    print(del_ids)  # 需要删除的元素的id

    for i in range(len(students_info) - 1, -1, -1):
        if students_info[i]["id"] in del_ids:
            print(students_info.pop(i))

    return redirect("/students_manage")


@app.route("/edit", methods=("GET", "POST"))
# @is_logined
def student_edit():
    if request.method == "GET":
        edit_id = int(request.args.get("id"))
        for index, student in enumerate(students_info):
            if student["id"] == edit_id:
                edit_user = student
                break
        else:
            return "没有找到该用户"
        return render_template("student_edit.html", student=edit_user)
    else:
        # print(students_info)
        user_dict = dict(request.form)  # 原始数据
        # print(user_dict)
        # 前端处理数据，后端直接将数据存入内存
        for i in range(len(students_info)):
            if students_info[i]["id"] == int(user_dict["user_id"]):
                students_info[i]["name"] = user_dict["name"]
                students_info[i]["sex"] = user_dict["sex"]
                try:
                    students_info[i]["age"] = int(user_dict["age"])
                    students_info[i]["score"] = int(user_dict["score"])
                except ValueError:
                    return "输入信息不正确"
                break
        else:
            return "找不到该用户"
        return redirect("/students_manage")


if __name__ == '__main__':
    app.run(debug=True)
