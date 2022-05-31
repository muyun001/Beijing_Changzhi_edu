from flask import Flask, render_template, request

# app类 ,对flask实例
app = Flask(__name__)


@app.route('/')
def index():
    #return "首页 <a href='/news_list/'>新闻列表页{name}</a>".format(name=1212)
    return render_template('index.html')


# @app.route('/news_list/')
# def news_list():
#     return "<a href='/'>首页</a><-新闻列表页-><a href='/news_list/detail.html'>跳转详细页</a>"


@app.route('/gm02/news_list/')
def news_list():
    # content = ''
    # with(open('./templates/news_list.html','r',encoding='utf-8')) as f:
    #     content = f.read()
    # return content.format(my_name="2班学生")
    my_name = "2班学生"
    news_list = [i for i in range(1, 11)]
    users = ["苏圆圆","林泽棕","观景风","吴武强"]
    user_info = [
        {'id':1,"name": "苏圆圆", 'age': 18,'other': "她喜欢吃吃吃..........各种吃，就是不胖，就是玩！"},
        {'id':2,"name": "林泽棕", 'age': 19,'other': "喜欢按摩,各种按，全方位的按,不怕花钱，就是玩！"},
        {'id':3,"name": "观景风", 'age': 20,'other': "喜欢上课，各种课，学习无止境，别人都以为我在学习，我也不解释"},
        {'id':4,"name": "吴武强", 'age': 12,'other': "刷B站，各种刷，网罗全网各色小姐姐."},
    ]
    # locals()以字典形式保存 函数中的所有局部变量
    #print(locals())
    return render_template('news_list.html', **locals())


@app.route('/user/detail.html')
def user_detail():
    #地址:127.0.0.1/user/detail.html?id=10&name=aaaaa
    # 参数id   值为10
    # 参数name   值为aaaaa
    # 取得get方式提交的参数 使用request.args.get() # 参数值都为字符串
    uid = int(request.args.get('uid'))
    users_info = [
        {'id': 1, "name": "苏圆圆", 'age': 18, 'other': "她喜欢吃吃吃..........各种吃，就是不胖，就是玩！"},
        {'id': 2, "name": "林泽棕", 'age': 19, 'other': "喜欢按摩,各种按，全方位的按,不怕花钱，就是玩！"},
        {'id': 3, "name": "观景风", 'age': 20, 'other': "喜欢上课，各种课，学习无止境，别人都以为我在学习，我也不解释"},
        {'id': 4, "name": "吴武强", 'age': 12, 'other': "刷B站，各种刷，网罗全网各色小姐姐."},
    ]
    res = {}
    # 循环判断参数uid和用户id是否相等。取出正确内容
    for user in users_info:
        if uid == user['id']:
            res = user
            break
    return render_template('user_detail.html', res=res)



@app.route('/news_list/detail_<int:nid>.html')
def news_detail(nid):
    #return f"新闻详细页-{nid}"
    #return render_template('news_detail.html', t_nid=nid, title="大数据2班")
    return render_template('news_detail.html', **{'t_nid': nid, 'title': "--大数据2班--"})


if __name__ == '__main__':
    app.run('127.0.0.1', 80, debug=True)
