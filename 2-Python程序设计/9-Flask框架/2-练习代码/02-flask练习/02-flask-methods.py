import json

from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        name = request.args['name']
        return f"此次请求是使用的get方法, {name}"
    else:
        name = request.form['name']
        return f"此次请求是使用的post方法, {name}"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        name = request.args.get("name")
        age = request.args.get("age")
        gender = request.args.get("gender")
        user = {"name": name, "age": age, "gender": gender}
        return f"get:{json.dumps(user, ensure_ascii=False)}"

    # post方法
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")

    if not name or not age or not gender:
        return "没有参数"
    user = {"name": name, "age": age, "gender": gender}
    return f"post:{json.dumps(user, ensure_ascii=False)}"


# @app.route("/api/put/<int:id>", methods=["PUT"])
# def put(id):
#     print(type(id))
#     return f"上传参数 {id}"
#
#
# @app.route("/api/delete/<int:ID>", methods=["DELETE"])  # 方式2
# def getPath(ID):
#     print(type(ID))
#     return f"测试值为 {ID}"


if __name__ == '__main__':
    app.run(debug=True)

