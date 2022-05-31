from flask import Flask

# 创建一个web应用的对象
app = Flask(__name__)


# 定义路由规则，以及对应的处理函数
# @app.route('/')
# def hello():
#     return "hello!"


# @app.route('/hello')
@app.route('/hello/')
def hello2():
    return "hello python!"


@app.route('/hello/<name>/')
def hello3(name):
    return f"hello {name}!"


@app.route('/user/<int:uid>/')
def get_user(uid):
    return f"user_id: {uid}!"

# 一个函数可以设置多个路由规则
# @app.route('/')
# @app.route('/hello/')
# @app.route('/hello/<name>/s')
# def hello(name=None):
#     if not name:
#         return "hello!"
#     return f"hello {name}"


if __name__ == '__main__':
    # 启动web服务器
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=8777, debug=True)
