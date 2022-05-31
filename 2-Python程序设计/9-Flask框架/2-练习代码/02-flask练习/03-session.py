"""
首先大家知道，http协议是无状态的，即你连续访问某个网页100次和访问1次对服务器来说是没有区别对待的，因为它记不住你。
那么，在一些场合，确实需要服务器记住当前用户怎么办？
比如用户登录邮箱后，接下来要收邮件、写邮件，总不能每次操作都让用户输入用户名和密码吧，
为了解决这个问题，session的方案就被提了出来，
事实上它并不是什么新技术，而且也不能脱离http协议以及任何现有的web技术。

原理很简单，假设你访问网页时就像进游泳馆，第一次进去你是没有钥匙的，
这个时候你交了钱服务台就分配一把钥匙给你，你走到哪里都要带上，因为这是你身份的唯一标识，
接下来你用这把钥匙可以去打开一个专有的储物柜存储你的衣物，游完泳，你再用钥匙去打开柜子拿出衣物，
最后离开游泳池时，把钥匙归还，你的这次游泳的过程就是一次session，或者叫做会话，
在这个例子中，钥匙就是session的key，而储物柜可以理解为存储用户会话信息的介质。
那么在web server中如何实现session呢？想必看了上面的例子你会很容易理解，主要是解决两个问题，
一个是钥匙的问题，一个是存储用户信息的问题。
对于第一个问题，即什么东西可以让你每次请求都会自动带到服务器呢？
如果你比较了解http协议，那么答案一目了然，就是cookie，如果你想为用户建立一次会话，
可以在用户授权成功时给他一个cookie，叫做会话id，它当然是唯一的，
比如PHP就会为建立会话的用户默认set一个名为phpsessid，值看起来为一个随机字符串的cookie，
如果下次发现用户带了这个cookie，服务器就知道，哎呀，刚刚这位顾客来了。
"""
"""
    没有设置session时，获取session就是None
"""

from flask import Flask, session

app = Flask(__name__)

"""
    在flask当中使用 session 时，必须要做一个配置、
    即 flask的session中需要用到的秘钥字符串，可以是任意值
    flask默认把数据存放到了cookie中
"""

app.config["SECRET_KEY"] = "abcdefghijk"


@app.route("/login")
def login():
    """设置session的数据"""
    session["name"] = "python"
    session["mobile"] = "18612345678"
    return "login success"


@app.route("/index")
def index():
    """获取session的数据"""
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)
