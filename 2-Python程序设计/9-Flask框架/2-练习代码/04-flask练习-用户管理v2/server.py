from flask import Flask, url_for, redirect, request, render_template
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

    students = []
    for r in res:
        new_s = {"name": r[1], "age": r[2], "gender": r[3]}
        students.append(new_s)
    return render_template('user.html', students=students)


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
        ("%s", %s, %s);
    """ % (name, gender, group_id)
    cursor.execute(sql)
    return redirect(url_for('user_list'))


@app.route('/delete')
def delete():
    uid = request.args.get('uid')
    if not uid:
        return "uid不能为空"
    if not uid.isdigit():
        return "uid必须是整数类型"
    sql = f"""
    delete from {settings.TABLE_NAME} where id = %s;
    """ % uid
    cursor.execute(sql)
    return redirect(url_for('user_list'))


@app.route('/edit')
def edit():
    uid = request.args.get('uid')
    age = request.args.get('age')
    if not uid:
        return "uid不能为空"
    if not uid.isdigit() or not age.isdigit():
        return "uid和age必须是整数类型"
    sql = f"""
        update {settings.TABLE_NAME} set age = %s where id = %s;
        """ % (age, uid)
    cursor.execute(sql)
    return redirect(url_for('user_list'))


@app.route('/query')
def query():
    uid = request.args.get('uid')
    if not uid:
        return "uid不能为空"
    if not uid.isdigit():
        return "uid必须是证书类型"
    sql = f"""
        select * from {settings.TABLE_NAME} where id = %s;
        """ % uid
    cursor.execute(sql)
    res = cursor.fetchall()
    if not res:
        return f"没有找到uid为{uid}的人"
    return str(res)


if __name__ == '__main__':
    app.run(debug=True)
