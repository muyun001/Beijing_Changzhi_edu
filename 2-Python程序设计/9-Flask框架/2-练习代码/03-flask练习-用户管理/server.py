import json

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

"""
k - v
k:student
v: []

[]中有两个元素：{a的信息},{b的信息}, {c的信息}, {d的信息}
"""

person = {
    "student": [
        {"uid": 1, "name": "崔昊元", "age": 18, "gender": 2},
        {"uid": 2, "name": "贾靖程", "age": 18, "gender": 2},
    ],
    "group": [
        {"gid": 1, "gname": "叶原枫", "gnum": 4},
        {"gid": 2, "gname": "琼玉", "gnum": 4},
        # {"gid": 3, "gname": "style", "gnum": 4},
        # {"gid": 4, "gname": "黑马", "gnum": 4},
    ]
}


@app.route('/')
def hello():
    return redirect(url_for("student_list"))


#################################### 对学生的增删改查 ####################################

@app.route('/student/')
def student_list():
    return person["student"]


@app.route('/student/add/', methods=["GET", "POST"], strict_slashes=False)
def student_add():
    if request.method == "GET":
        # 获取get请求传递过来的数据
        info = request.args
    else:
        # 获取post请求传递过来的数据
        info = request.form

    uid = info.get('uid')
    if uid != None:
        uid = int(uid)

    name = info.get('name')
    age = info.get('age')
    if age != None:
        age = int(age)

    gender = info.get('gender')
    if gender != None:
        gender = int(gender)

    new_s = {"uid": uid, "name": name, "age": age, "gender": gender}
    person['student'].append(new_s)
    return redirect(url_for('student_list'))


@app.route('/student/delete/<int:uid>')
def student_delete(uid):
    # {"uid": 4, "name": "叶平", "age": 18, "gender": 1},
    for s in person['student']:
        if s['uid'] == uid:
            person['student'].remove(s)
            return redirect(url_for('student_list'))

    return f"没有找到uid为{uid}的人！<a href='/user/'>点击此处可以回到主页面</a>"


# http://127.0.0.1:5000/edit?uid={uid}&age={age}
@app.route('/student/edit')
def student_edit():
    uid = int(request.args.get("uid"))
    age = int(request.args.get("age"))
    for s in person['student']:
        if s['uid'] == uid:
            s['age'] = age
            return redirect(url_for('student_list'))
    return f"没有找到uid为{uid}的人！<a href='/user/'>点击此处可以回到主页面</a>"


@app.route('/student/query')
def student_query():
    uid = int(request.args.get("uid"))
    for s in person['student']:
        if s['uid'] == uid:
            return s
    return f"没有找到uid为{uid}的人！<a href='/user/'>点击此处可以回到主页面</a>"


#################################### 对分组的增删改查 ####################################

@app.route('/group/')
def group_list():
    return person['group']


@app.route('/group/add', methods=["GET", "POST"], strict_slashes=False)
def group_add():
    # todo
    pass


@app.route('/group/delete/<int:gid>')
def group_delete():
    # todo
    pass


@app.route('/group/edit')
def group_edit():
    # todo
    pass


@app.route('/group/query')
def group_query():
    # todo
    pass


if __name__ == '__main__':
    app.run(debug=True)
