from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# 使用session，需要设置密钥
# 密钥要尽可能复杂
app.secret_key = 'a1s@i34!3-&d'

@app.route('/')
def index():
    # 判断'user'是否存在与session中
    if 'user' in session:
        return render_template('admin_index.html')
    # 如果不存在，返回特定信息
    return 'session中无用户信息！！'


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        pwd = request.form.get("pwd")
        if user_name == "admin" and pwd == "123456":
            # 登陆成功后，将user信息保存下来
            session['user'] = user_name
            return redirect(url_for('index'))
        else:
            return render_template('login.html', **{"error": "账号或密码错误！"})

    # get请求
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
