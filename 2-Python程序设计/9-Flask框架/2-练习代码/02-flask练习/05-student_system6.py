from flask import Flask, url_for, redirect, request
import settings
import pymysql

app = Flask(__name__)

conn = pymysql.connect(**settings.MYSQL_CONFIG)
cursor = conn.cursor()



@app.route('/')
def hello():
    return redirect(url_for('user_list'))


@app.route('/user/')
def user_list():
    # 从数据库获取所有数据
    sql = f"select * from {settings.TABLE_NAME};"
    cursor.execute(sql)
    res = cursor.fetchall()
    # 展示数据
    return f"{res}"


@app.route('/add', methods=["POST"])
def add():
    info = request.form
    name = info.get('name')
    gender = info.get('gender')
    group_id = info.get('group_id')

    sql = f"""
    insert into {settings.TABLE_NAME} 
        (name, gender, group_id)
    values 
        ("%s", %s, %s)
    """ % (name, gender, group_id)
    cursor.execute(sql)
    return redirect(url_for('user_list'))




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
