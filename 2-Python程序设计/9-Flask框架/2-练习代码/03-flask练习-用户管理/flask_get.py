from flask import Flask, render_template, redirect

app = Flask(__name__)

user_list = [
    {"name": "崔昊元", "age": "18", "gender": "2", "phone": "110"},
    {"name": "王孝天", "age": "18", "gender": "1", "phone": "111"},
    {"name": "赵鑫博", "age": "18", "gender": "1", "phone": "112"},
    {"name": "吴俊岳", "age": "18", "gender": "1", "phone": "113"},
    {"name": "张子豪", "age": "18", "gender": "1", "phone": "114"},
]


@app.route('/')
def index():
    # return "欢迎来到用户管理系统"
    return redirect('user_list')


@app.route('/user_list/')
def user_list():
    return render_template('user_list.html', user_list=user_list)


@app.route('/add/', methods=["GET", "POST"])
def add():
    pass


@app.route('/delete/')
def delete():
    pass


@app.route('/edit/')
def edit():
    pass


if __name__ == '__main__':
    app.run(debug=True)
