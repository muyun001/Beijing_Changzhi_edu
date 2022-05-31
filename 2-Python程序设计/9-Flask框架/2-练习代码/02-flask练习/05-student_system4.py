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
    ]
}


@app.route('/')
def hello():
    return redirect(url_for("user_list"))


@app.route('/user/')
def user_list():
    return person


@app.route('/add/', methods=["GET", "POST"], strict_slashes=False)
def add():
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
    return redirect(url_for('user_list'))


@app.route('/delete/<int:uid>')
def delete(uid):
    # {"uid": 4, "name": "叶平", "age": 18, "gender": 1},
    for s in person['student']:
        if s['uid'] == uid:
            person['student'].remove(s)
            return redirect(url_for('user_list'))

    return f"没有找到uid为{uid}的人！<a href='/user/'>点击此处可以回到主页面</a>"


# http://127.0.0.1:5000/edit?uid={uid}&age={age}
@app.route('/edit')
def edit():
    uid = int(request.args.get("uid"))
    age = int(request.args.get("age"))
    for s in person['student']:
        if s['uid'] == uid:
            s['age'] = age
            return redirect(url_for('user_list'))
    return f"没有找到uid为{uid}的人！<a href='/user/'>点击此处可以回到主页面</a>"


@app.route('/query')
def query():
    uid = int(request.args.get("uid"))
    for s in person['student']:
        if s['uid'] == uid:
            return s
    return f"没有找到uid为{uid}的人！<a href='/user/'>点击此处可以回到主页面</a>"


if __name__ == '__main__':
    app.run(debug=True)
