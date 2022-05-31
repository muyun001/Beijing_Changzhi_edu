import json
import settings
import pymysql

from flask import Flask, url_for, redirect, request

app = Flask(__name__)

conn = pymysql.connect(**settings.MYSQL_CONFIG)
cursor = conn.cursor()

person = {
    "student": [
        {"name": "张阔", "age": 18},
        {"name": "叶平", "age": 18},
    ]
}


@app.route('/user/')
def user():
    sql = f"""
        select * from {settings.TABLE_NAME}
        """
    cursor.execute(sql)
    conn.commit()  # 提交
    res = cursor.fetchall()
    return


@app.route('/add', methods=["GET", "POST"])
def add():
    """ 添加数据 """
    if request.method == "GET":
        # get请求
        # name
        info = request.args
    else:
        # post请求
        info = request.form

    name = info.get('name')
    group_id = info.get('group_id')
    # {"name": "叶平", "age": 18},
    # new_student = {"name": name, "age": age}
    # person['student'].append(new_student)
    # print(person)

    sql = f"""
        insert into {settings.TABLE_NAME}
            (name, group_id)
        values 
            ("%s", %s);
    """ % (name, group_id)
    cursor.execute(sql)
    conn.commit()  # 提交
    return redirect(url_for('user'))


@app.route('/delete')
def delete():
    pass


@app.route('/edit')
def edit():
    pass


@app.route('/query')
def query():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    # request.args = {"name": "zhangsan", "age": 18}
    # # name = d['name']
    # name = request.args.get('name')
    # print(name)
