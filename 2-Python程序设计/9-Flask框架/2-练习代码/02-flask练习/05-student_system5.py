import json

from flask import Flask, redirect, request, url_for

app = Flask(__name__)

"""
k - v
k:student
v: []

[]中有两个元素：{a的信息},{b的信息}, {c的信息}, {d的信息}
"""

person = {
    "student": [
        {"sid": 1, "name": "崔昊元", "age": 18, "gender": 2, "score": 89},
        {"sid": 2, "name": "牛皓冬", "age": 18, "gender": 1, "score": 79},
    ]
}


@app.route('/')
def hello():
    return "欢迎来到学生系统，点击<a href='/user/'>这里</a>进行跳转。"


@app.route('/user')
def user_list():
    return person
    # return json.dumps(person, ensure_ascii=False)


# POST
@app.route('/user/add', methods=["GET", "POST"])
def add():
    if request.method == "GET":
        s_info = request.args.to_dict()
    else:
        s_info = request.form.to_dict()

    if not s_info.get('sid'):
        return "sid不能为空！点击<a href='/user'>这里</a>回用户页面。"

    # 转int类型
    for k, v in s_info.items():
        if v.isdigit():
            s_info[k] = int(v)

    person['student'].append(s_info)
    # todo bug：重新get访问/user/add
    response = redirect(url_for('user_list'))
    return response


@app.route('/delete/<int:sid>')
def delete(sid):
    for s in person['student']:
        if s['sid'] == sid:
            person['student'].remove(s)
            return redirect(url_for('user_list'))

    return f"未找到sid是{sid}的信息，点击<a href='/user'>这里</a>回用户页面。"



if __name__ == '__main__':
    app.run(debug=True)
