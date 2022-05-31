from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/login/')
def login1():
    return "login"

@app.route('/login/<name>/<pwd>')
def login2(name=None, pwd=None):
    if name == "admin" and pwd == "admin":
        return f"管理员登陆成功！"
    return "登陆失败"


@app.route("/login/")
@app.route('/login/<name>/<pwd>')
def login3(name=None, pwd=None):
    if not name and not pwd:
        return "login"
    if name == "admin" and pwd == "admin":
        return f"管理员登陆成功！"
    return "登陆失败"

@app.route('/login', methods=['GET', 'POST'])
def login4():
    print(request.method)
    if request.method == "GET":
        return "get方法"
    return "post方法"

# 查询路径
@app.route('/path')
def path():
    # return url_for('login1')
    # return url_for('login2', name='zhangsan', pwd="123")
    # return url_for('login3')
    # return url_for('login3', name='zhangsan', pwd="123")
    return url_for('login4')


if __name__ == '__main__':
    app.run(debug=True)
