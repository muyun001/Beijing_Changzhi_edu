from flask import Flask, render_template,request, redirect

# 实例化
app = Flask(__name__, static_folder="static")

#定义首页路由地址
@app.route('/')
def index():
    return render_template('index.html')

#form表单的提交处理,默认路由只支持get提交
@app.route('/login/',methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template('hello2.html')
    else:
        # 获取form表单提交的内容
        user_name = request.form.get('user_name')
        pwd = request.form.get('pwd')
        if user_name == 'root' and pwd == '123456':
            return redirect(f'/?username={user_name}')
        else:
            return redirect('/login/?error=1')
            # 使用加载模板会出现刷新页面，重新提交之前form表的的数据
            #return render_template('hello2.html')


# 只执行当前文件时启用 flask服务
if __name__ == '__main__':
    app.run('127.0.0.1', 80, debug=True)