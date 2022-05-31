from flask import Flask,render_template
import utils

# 创建一个web应用的对象
app = Flask(__name__)


@app.route('/home/')
def home():
    """主页"""
    # return "欢迎来到主页"
    return "<h1>欢迎来到主页</h1>"


@app.route('/baidu/')
def baidu():
    # return "https://www.baidu.com"
    return "<a href='https://www.baidu.com'>百度</a>"


@app.route('/read/')
def read_file():
    text = utils.read_file()
    return text


@app.route('/write/<text>/')
def write_file(text=None):
    try:
        utils.write_file(text)
        return "写数据成功"
    except:
        return "写数据失败"


@app.route('/create/table/')
def create_table():
    try:
        utils.create_table()
        return ""
    except:
        return ""

@app.route('/table/')
def a():
    return render_template('area-stack.html')


if __name__ == '__main__':
    # 启动web服务器
    app.run(debug=True)
