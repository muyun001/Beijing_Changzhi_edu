from flask import Flask, render_template
import pymysql
import utils

# 需要创建一个web对象
app = Flask(__name__)

# 1、连接数据库
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="cz_students",
    charset="utf8"
)

# 2、创建游标,可以传递参数
cursor = conn.cursor()


@app.route("/")
def hello():
    return "hello"


# @app.route('/hello1/')
# def hello1():
#     return "hello python1"
#
#
# @app.route('/add/')
# def add():
#     result = 1 + 2
#     return f"{result}"
#
#
# # @app.route('/hello/<name>/')
# # def hello2(name):
# #     print(name)
# #     # with open("", "w", encoding="utf-8") as f:
# #     #     return f.write(name)
# #     return f"早上好 {name}"
#
#
# @app.route('/hello/')
# @app.route('/hello/<name>/')
# def hello3(name=None):
#     print(name)
#     if not name:
#         return "hello"
#     return f"hello {name}"
#
#
# @app.route('/hello4/')
# def hello4():
#     return "<h1> hello </h1>"
#     # return "<h2> hello </h2>"
#
#
# @app.route('/page/')
# def page():
#     return render_template('hello.html')
#
#
# @app.route('/form_demo/')
# def form_demo():
#     return render_template('form_demo.html')
#
#
# @app.route('/area/')
# def echarts():
#     return render_template('area-stack.html')
#
#
# @app.route('/read/')
# def read():
#     with open("files/hello.txt", "r", encoding="utf-8") as f:
#         return f.read()
#
#
# @app.route('/read_from_mysql/')
# def read_from_mysql():
#     return f"{utils.read_from_mysql()}"
#
#
# @app.route('/write_to_mysql/<name>/')
# def write_to_mysql(name=None):
#     sql = """
#     insert into cz_s2(name)values (%s)
#     """
#     try:
#         cursor.execute(sql, name)
#         return "写入数据库成功！"
#     except:
#         return "写入数据库失败"

# @app.route('/user/<name>/')
# @app.route('/user/<int:id>')
# def hello6(id):
#     return f"hello {id}"

# @app.route('/score/<float:score>')
# def hello7(score):
#     return f"your score is {score}"
#
# @app.route('/path/<path:p>')
# def path(p):
#     return f"路径是{p}"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello1(name=None):
    print(name)
    return render_template('hello.html', name=name)


# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello2(name=None):
#     return render_template('hello2.html', name=name)

@app.route('/temp')
def temp_test():
    return render_template('temp_test.html')

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)
