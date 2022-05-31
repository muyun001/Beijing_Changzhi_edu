from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        pwd = request.form.get("pwd")
        if user_name == "admin" and pwd == "123456":
            return '<h1>登陆成功</h1>'
        else:
            return render_template('login.html', **{"error": "账号或密码错误！"})

    # get请求
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
