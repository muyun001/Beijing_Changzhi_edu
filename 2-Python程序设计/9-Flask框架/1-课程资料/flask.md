# Flask

中文官网：http://docs.jinkan.org/docs/flask/quickstart.html#context-locals

## 一、Hello World

项目开发中，经常要写一些小系统来辅助，比如监控系统，配置系统等等。用传统的Java写，太笨重了，连PHP都嫌麻烦。一直在寻找一个轻量级的后台框架，学习成本低，维护简单。发现Flask后，我立马被它的轻巧所吸引，它充分发挥了Python语言的优雅和轻便，连Django这样强大的框架在它面前都觉得繁琐。可以说简单就是美。这里我们不讨论到底哪个框架语言更好，只是从简单这个角度出发，Flask绝对是佼佼者。这一系列文章就会给大家展示Flask的轻巧之美。

1. Flask入门系列(一)-Hello World
2. Flask入门系列(二)-路由
3. Flask入门系列(三)-模板
4. Flask入门系列(四)-请求，响应及会话
5. Flask入门系列(五)-错误处理及消息闪现
6. Flask入门系列(六)-数据库集成

### **Hello World**

程序员的经典学习方法，从Hello World开始。不要忘了，先安装`python, pip`，然后运行`pip install Flask`，环境就装好了。当然本人还是强烈建议使用virtualenv来安装环境。细节就不多说了，让我们写个`Hello World`吧：

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run()
```

一个Web应用的代码就写完了，对，就是这么简单！保存为”hello.py”，打开控制台，到该文件目录下，运行

```python
$ python hello.py
```

如果看到

```python
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

字样后，就说明服务器启动完成。打开你的浏览器，访问`http://127.0.0.1:5000/`，一个硕大的”Hello World”映入眼帘:-)

### **简单解释下这段代码**

- 首先引入了Flask包，并创建一个Web应用的实例”app”

  ```python
  from flask import Flask
  app = Flask(__name__)
  ```

  这里给的实例名称就是这个python模块名。

- 定义路由规则

  ```py
  @app.route('/')
  ```

  这个函数级别的注解指明了当地址是根路径时，就调用下面的函数。可以定义多个路由规则，会在后续教程里详细介绍。说的高大上些，这里就是MVC中的Contoller。

- 处理请求

  ```py
  def index():
      return '<h1>Hello World</h1>'
  ```

  当请求的地址符合路由规则时，就会进入该函数。可以说，这里是MVC的Model层。你可以在里面获取请求的request对象，返回的内容就是response。本例中的response就是大标题”Hello World”。

- 启动Web服务器

  ```py
  if __name__ == '__main__':
      app.run()
  ```

  当本文件为程序入口（也就是用python命令直接执行本文件）时，就会通过`app.run()`启动Web服务器。如果不是程序入口，那么该文件就是一个模块。Web服务器会默认监听本地的5000端口，但不支持远程访问。如果你想支持远程，需要在`run()`方法传入`host=0.0.0.0`，想改变监听端口的话，传入`port=端口号`，你还可以设置调试模式。具体例子如下：

  ```python
  if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8888, debug=True)
  ```

  注意，Flask自带的Web服务器主要还是给开发人员调试用的，在生产环境中，你最好是通过WSGI将Flask工程部署到类似Apache或Nginx的服务器上。
  
  ```python
  # 开启debug ：激活自动重载 并 可以帮助我们查找代码里面的错误
  ```
  
  **运行时常见错误：**
  
  错误一：
  
  ![image-20220520174557244](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0hyjnrej20y802u75b.jpg)

​		错误原因：在控制面板中将电脑名字改为英文名字，运行就ok

​	错误2：

![image-20220520174635038](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0ikdspfj20y4038mxz.jpg)	错误原因：浏览器访问时使用：https ，将https修改为http



### 完整代码

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
```

## 二、路由

现代 web 应用都使用有意义的 URL ，这样有助于用户记忆，网页会更得到用户的青睐， 提高回头率。

使用 route() 装饰器来把函数绑定到 URL:

```python
@app.route('/') 
def index(): 
  return 'Index Page' 

@app.route('/hello') 
def hello(): 
  return 'Hello, World'
```

浏览器的地址栏中输入:http://127.0.0.1:5000/

![image-20220520174939380](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0lroqchj20qw08w3zj.jpg)

浏览器的地址栏中输入:`http://127.0.0.1:5000/hello

![image-20220520174956426](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0m2h4x0j20r8088gmg.jpg)

但是能做的不仅仅是这些！你可以动态变化 URL 的某些部分， 还可以为一个函数指定多个规则。通过把 URL 的一部分标记为 <variable_name> 就可以在 URL 中添加变量。标记的 部分会作为关键字参数传递给函数。通过使用 <converter:variable_name> ，可以选择性的加上一个转换器，为变量指定规则。请看下面的例子:

```python
from flask import Flask, escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示该用户的用户配置文件 , escape用来转义
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示具有给定id的帖子，id为整数
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 显示在/path之后的子路径
    return 'Subpath %s' % escape(subpath)


if __name__ == '__main__':
    app.run(debug=True)

```

**escape()**是用来转义的,需要引入 from flask import escape

当你在浏览器的地址栏中输入 http://localhost:5000/user/xiaopang ，你将在页面上看到"User xiaopang”的字样。URL路径中/user/后面的参数被作为show_user_profile() 函数的username参数传了进来。

![image-20220520175539574](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0s0b4zuj20u6078t9f.jpg)

试下访问 http://localhost:5000/post/xiaopang ，你会看到Not Found错误。但是试下http://localhost:5000/post/123 ，页面上就会有”Post 123”显示出来。参数类型转换器 int:帮你控制好了传入参数的类型只能是整形。

![image-20220520175724136](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0ttyxygj20sm05odgj.jpg)



试下访问 http://localhost:5000/path/article/show.html ，你将在页面上看到”Subpatharticle/show.html”的字样,会将path之后的路径地址全部作为show_subpath()函数的subpath参数值传递进去

![image-20220520175746362](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0u7iiofj20ve066q40.jpg)

目前支持的参数类型转换器有：

| 类型转换器   | 作用                 |
| ------------ | -------------------- |
| 默认（缺省） | 字符型，但不能有斜杠 |
| int:         | 整型                 |
| float:       | 浮点型               |
| path:        | 字符型，可有斜杠     |

另外，大家有没有注意到，Flask自带的Web服务器支持热部署。当你修改好文件并保存后，Web服务器自动部署完毕，你无需重新运行程序。

### 多URL的路由

一个函数上可以设置多个URL路由规则

```python
@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = 'World'
    return 'Hello %s' % name
```

这个例子接受三种URL规则，`/`和`/hello`都不带参数，函数参数`name`值将为空，页面显示”Hello World”；`/hello/<name>`带参数，页面会显示参数`name`的值，效果与上面第一个例子相同。

### HTTP请求方法设置

HTTP请求方法常用的有Get, Post, Put, Delete。Flask路由规则也可以设置请求方法。

```python
from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'
```

当你请求地址`http://localhost:5000/login`，”GET”和”POST”请求会返回不同的内容。

- 通过浏览器访问 http://localhost:5000/login/ ，你将在页面上看到 这是一个 GET 请求

- 可借助第三方测试软件(如postman、apipost、apifox等)

  ![image-20220520180157667](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0ykhto3j21he0s2dkg.jpg)

  ![image-20220520180256607](https://tva1.sinaimg.cn/large/e6c9d24ely1h2f0zlf0hfj21gc0p8aej.jpg)

### 唯一的URL /重定向行为

以下两条规则的不同之处在于是否使用尾部的斜杠: 

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

projects 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文件夹。 访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。

```
当浏览器上输入:http://127.0.0.1:5000/projects Flask会自动将http://127.0.0.1:5000/projects重定向到 http://127.0.0.1:5000/projects/
```

about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。

### URL构建方法

Flask提供了`url_for()`方法来快速获取及构建URL，方法的第一个参数指向函数名（加过`@app.route`注解的函数），后续的参数对应于要构建的URL变量。下面是几个例子：

```python
url_for('login')    # 返回/login
url_for('login', id='1')    # 将id作为URL参数，返回/login?id=1
url_for('hello', name='man')    # 适配hello函数的name参数，返回/hello/man
url_for('static', filename='style.css')    # 静态文件地址，返回/static/style.css
```

```
为什么不在把 URL 写死在模板中，而要使用反转函数 url_for() 动态构建？
1. 反转通常比硬编码 URL 的描述性更好。
2. 你可以只在一个地方改变 URL ，而不用到处乱找。
3. URL 创建会为你处理特殊字符的转义和 Unicode 数据，比较直观。
4. 生产的路径总是绝对路径，可以避免相对路径产生副作用。
5. 如果你的应用是放在 URL 根路径之外的地方（如在 /myapplication 中，不在 / 中），url_for() 会为你妥善处理。
```

### 静态文件位置

一个Web应用的静态文件包括了JS, CSS, 图片等，Flask的风格是将所有静态文件放在”static”子目录下。并且在代码或模板（[下篇](http://www.bjhee.com/flask-3.html)会介绍）中，使用`url_for('static')`来获取静态文件目录。上小节中第四个的例子就是通过`url_for()`函数获取”static”目录下的指定文件。如果你想改变这个静态目录的位置，你可以在创建应用时，指定`static_folder`参数。

```python
app = Flask(__name__, static_folder='static')
```

### 完整代码

```python
from flask import Flask
from flask import request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = 'World'
    return 'Hello %s' % name

@app.route('/user/<int:user_id>')
def get_user(user_id):
    return 'User ID: %d' % user_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'

@app.route('/path')
def path():
    #return url_for('login')
    #return url_for('login', id='1')
    #return url_for('hello', name='man')
    return url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

# 三、模板

在 Python 内部生成 HTML 不好玩，且相当笨拙。因为你必须自己负责 HTML 转义， 以确保应用的安全。因此， Flask 自动为你配置 [Jinja2 模板引擎](http://jinja.pocoo.org/)。

**render_template()**

使用 render_template() 方法可以渲染模板，你只要提供模板名称和需要 作为参数传递给模板的变量就行了。下面是一个简单的模板渲染例子:

```python
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

Flask 会在 `templates` 文件夹内寻找模板，文件路径如下：

```
/main.py 
/templates 
	/hello.html
```

这段代码同上一篇的多URL路由的例子非常相似，区别就是`hello()`函数并不是直接返回字符串，而是调用了`render_template()`方法来渲染模板。方法的第一个参数`hello.html`指向你想渲染的模板名称，第二个参数`name`是你要传到模板去的变量，变量可以传多个。

那么这个模板`hello.html`在哪儿呢，变量参数又该怎么用呢？别急，接下来我们创建模板文件。在当前目录下，创建一个子目录”templates”（注意，一定要使用这个名字）。然后在”templates”目录下创建文件”hello.html”，内容如下：

```html
<!doctype html>
<title>Hello Sample</title>
{% if name %}
    <h1>Hello {{ name }}!</h1>
{% else %}
    <h1>Hello World!</h1>
{% endif %}
```

这段代码是不是很像HTML？接触过其他模板引擎的朋友们肯定立马秒懂了这段代码。它就是一个HTML模板，根据`name`变量的值，显示不同的内容。变量或表达式由`{{ }}`修饰，而控制语句由`{% %}`修饰，其他的代码，就是我们常见的HTML。

让我们打开浏览器，输入`http://localhost:5000/hello/man`，页面上即显示大标题”Hello man!“。我们再看下页面源代码:

```html
<!doctype html>
<title>Hello from Flask</title>

    <h1>Hello man!</h1>
```

果然，模板代码进入了`Hello {{ name }}!`分支，而且变量`{{ name }}`被替换为了`man`。Jinja2的模板引擎还有更多强大的功能，包括for循环，过滤器等。模板里也可以直接访问内置对象如`request`,` session`等。

### flask之jinja2模板内置过滤器

过滤器是通过管道符号（|）使用的，比如`{{ age|abs }}`是返回`age`的绝对值。过滤器类似函数，将参数传递给过滤器，再由过滤器根据其相应的功能返回相应的值去渲染网页。jinja2有许多内置的过滤器，下面一 一进行介绍：

```python
abs(value)：返回value的绝对值 

default(value,default_value)：设置默认值，如果value没有定义，则返回默认的 default_value值 

escape(value)/e(value)：将value中的<,>等符号转义为html符号 

safe(value)：如果全局开启了转义，用safe可以将value的转义关闭 

first(value)：获取value(序列)中的第一个值 

last(value)：获取value(序列)中的最后一个值 

length(value)：获取value的长度 

format(value,**args,**kwargs)：格式化value， 
{{ '%s and %s' | format(xxx,yyy) }} 

join(value,d=‘参数值’)：将序列value用d的参数值进行拼接，拼接成一个字符串

wordcount(value)：获取value中的词的个数（以空格为分隔符） 

trim(value)：截取value前后的空白字符 

int(value)：将value转化为整型

float(value)：将value转化为浮点型

string(value)：将value转化为字符串类型 

replace(value,old,new)：把value中的old替换成new，输出替换后的value 

truncate(value,length=x,killwords=False)：截取value长度为length的字符串； killwords为是否输出完整的单词 

upper(value)：将value转化为大写 

lower(value)：将value转化为小写
```

实例`demo.filter.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>常见内建filter</h1>

<em>hello</em>
<hr>

<p>{{ '<em>hello</em>' }}</p>
<hr>

{# 自动转义 #}
<p>{{ '<em>hello</em>'|safe }}</p>
<hr>

{# 变量首字母大写 #}
<p>{{ 'hello'|capitalize }}</p>
<hr>

{# 转化成大写 #}
<p>{{ 'hello'|upper }}</p>
<hr>

{# 转化成小写 #}
<p>{{ 'HELLO'|lower }}</p>
<hr>

{# 单词首字母大写 #}
<p>{{ 'ada addada fhfghf'|title }}</p>
<hr>

{# 格式化输出 #}
<p>{{ '%s is %d'| format('李傲',18) }}</p>
<hr>

{# 反转 #}
<p>{{ 'hello'|reverse }}</p>
<hr>

{# 渲染之前把所有html标签都去掉 #}
<p>{{ '<h1>hello</h1>'|striptags }}</p>
<hr>
<h1>列表操作</h1>

{# 取值 #}
<p>{{ [1,2,3,4 ]|first }}</p>
<p>{{ [1,2,3,4 ]|last }}</p>
<p>{{ [1,2,3,4 ]|length }}</p>

{# 求和 #}
<p>{{ [1,2,3,4 ]|sum }}</p>

{# 排序 #}
<p>{{ [1,2,3,4 ]|sort }}</p>
</body>
```

<img src="https://tva1.sinaimg.cn/large/e6c9d24ely1h2f1pzt8xdj20ho0ym3zh.jpg" alt="image-20220520182821268" style="zoom:50%;" />

<img src="https://tva1.sinaimg.cn/large/e6c9d24ely1h2f1q3w510j20960eqaa4.jpg" alt="image-20220520182828021" style="zoom:50%;" />

**jinja2模板`for`循环**

在 jinja2 中的 for 循环，跟 python 中的 for 循环基本上是一模一样的。也是 for...in... 的形式。并且也可以遍历所有的序列以及迭代器。但是唯一不同的是， jinja2 中的 for 循环没有 break 和 continue 语句。

```
并且jinja2中的for循环还包含以下变量，可以用来获取当前的遍历状态 

变量|描述 
loop.index 当前迭代的索引（从1开始） 
loop.index0 当前迭代的索引（从e开始） 
1oop.first 是否是第一次迭代，返回True或 False 
loop.last 是否是最后一次选代，返回True或 False 
1oop.length 序列的长度
```

`main.py`

```python
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index_for():
    context = {'users': ['崔昊元', '王浩羽', '张子豪'],
               'person':
                   {
                       'username': '张三',
                       'age': 18,
                       'country': 'china'
                   },
               'books': [
                   {'name': '三国演义', 'author': '罗贯中', 'price': 110},
                   {'name': '西游记', 'author': '吴承恩', 'price': 109},
                   {'name': '红楼梦', 'author': '曹雪芹', 'price': 120},
                   {'name': '水浒传', 'author': '施耐庵', 'price': 119}]
               }

    return render_template('index_for.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

```

`templates/index_for.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>for循环</title></head>
<body>
<ul>
    {% for user in users|reverse %}
        <li>{{ user }}</li>
    {% else %}
        <li>沒有任何值</li>
    {% endfor %}
</ul>
<hr>
<table>
    <thead>
    <tr>
        <th>用户名</th>
        <th>年龄</th>
        <th>国家</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        {% for v in person.values() %}
            <td>{{ v }}</td>
        {% endfor %}
    </tr>
    </tbody>
</table>
<hr>
<table>
    <thead>
    <tr>
        <th>序号</th>
        <th>书名</th>
        <th>作者</th>
        <th>价格</th>
        <th>总数</th>
    </tr>
    </thead>
    <tbody>
        {% for book in books %}
            {% if loop.first %}
                <tr style="background: red;">
            {% elif loop.last %}
                <tr style="background: pink;">
            {% endif %}
            {# 添加序号 #}
            <td>{{ loop.index0 }}</td>
            <td>{{ book.name }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.price }}</td>
            <td>{{ loop.length }}</td> </tr>
        {% endfor %}
    </tbody>
</table>
<hr>
<table border="1">
    <tbody>
        {% for x in range(1,10) %}
            <tr>
                {% for y in range(1,10) if y <= x %}
                    <td>{{ y }}*{{ x }}={{ x*y }}</td>
                {% endfor %} 
            </tr>
        {% endfor %}
    </tbody>
</table>
</body>
</html>
```

<img src="https://tva1.sinaimg.cn/large/e6c9d24ely1h2fvtik0a8j20u00utjv4.jpg" alt="image-20220521114939995" style="zoom:50%;" />

### 常见错误

1.templates模板文件夹创建错误，或文件不存在 都会报一下错误

![image-20220521170221382](https://tva1.sinaimg.cn/large/e6c9d24ely1h2g4uuybzzj20vo094dhh.jpg)

### 模板继承

一般我们的网站虽然页面多，但是很多部分是重用的，比如页首，页脚，导航栏之类的。对于每个页面，都要写这些代码，很麻烦。Flask的Jinja2模板支持模板继承功能，省去了这些重复代码。让我们基于上面的例子，在`templates`目录下，创建一个名为`layout.html`的模板：

```html
<!doctype html>
<title>Hello Sample</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<div class="page">
    {% block body %}
    {% endblock %}
</div>
```

再修改之前的`hello.html`，把原来的代码定义在`{% block body %}`中，并在代码一开始”继承”上面的`layout.html`：

```html
{% extends "layout.html" %}
{% block body %}
{% if name %}
    <h1>Hello {{ name }}!</h1>
{% else %}
    <h1>Hello World!</h1>
{% endif %}
{% endblock %}
```

打开浏览器，再看下`http://localhost:5000/hello/man`页面的源码。

```html
<!doctype html>
<title>Hello Sample</title>
<link rel="stylesheet" type="text/css" href="/static/style.css">
<div class="page">

    <h1>Hello man!</h1>

</div>
```

你会发现，虽然`render_template()`加载了`hello.html`模板，但是`layout.html`的内容也一起被加载了。而且`hello.html`中的内容被放置在`layout.html`中`{% block body %}`的位置上。形象的说，就是`hello.html`继承了`layout.html`。

### HTML自动转义

我们看下下面的代码：

```python
@app.route('/')
def index():
    return '<div>Hello %s</div>' % '<em>Flask</em>'
```

打开页面，你会看到”Hello Flask”字样，而且”Flask”是斜体的，因为我们加了`<em>`标签。但有时我们并不想让这些HTML标签自动转义，特别是传递表单参数时，很容易导致HTML注入的漏洞。我们把上面的代码改下，引入”Markup”类：

```python
from flask import Flask, Markup

app = Flask(__name__)

@app.route('/')
def index():
    return Markup('<div>Hello %s</div>') % '<em>Flask</em>'
```

再次打开页面，`<em>`标签显示在页面上了。Markup还有很多方法，比如`escape()`呈现HTML标签, `striptags()`去除HTML标签。这里就不一一列举了。

### 完整代码

`flask3.py`

```python
from flask import Flask
from flask import render_template, Markup

app = Flask(__name__)

@app.route('/')
def index():
    return Markup('<div>Hello %s</div>') % '<em>Flask</em>'
    #return Markup.escape('<div>Hello Flask</div>')
    #return Markup('<h1>Hello Flask</h1>').striptags()

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

`templates/hello.html`

```html
{% extends "layout.html" %}
{% block body %}
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
{% endblock %}
```

`templates/layout.html`

```html
<!doctype html>
<title>Hello Sample</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<div class="page">
    {% block body %}
    {% endblock %}
</div>
```

## 四、请求，响应及会话

一个完整的HTTP请求，包括了客户端的请求Request、服务器端的响应Response、会话Session等。一个基本的Web框架一定会提供内建的对象来访问这些信息，Flask当然也不例外。我们来看看在Flask中该怎么使用这些内建对象。

### Flask内建对象

Flask提供的内建对象常用的有request、session、g，通过request，你还可以获取cookie对象。这些对象不但可以在请求函数中使用，在模板中也可以使用。

#### 请求对象request

来自客户端网页的数据作为全局请求对象发送到服务器。为了处理请求数据，应该从Flask模块导入。Request对象的重要属性如下所列：

| 属性    | 解释                                                  |
| ------- | ----------------------------------------------------- |
| Form    | 它是一个字典对象，包含表单参数及其值的键和值对        |
| args    | 解析查询字符串的内容，它是问号（？）之后的URL的一部分 |
| Cookies | 保存Cookie名称和值的字典对象                          |
| files   | 与上传文件有关的数据                                  |
| method  | 当前请求方法                                          |

**获取`get`方式提交的数据**

实例：

`main.py`

```python
from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    title = request.args.get('title', 'Default')
    return render_template('hello2.html', title=title)
```

模版：`news_list.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title></title>
    <style>
        ul li {
            list-style: none;
        }
    </style>
</head>
<body>
<table border="1">
    <tr>
        <th>编号</th>
        <th>姓名</th>
        <th>年龄</th>
        <th>查看爱好</th>
    </tr>
    <!---- 循环展示学生信息----->
    {% for user in user_info %}
        <tr>
            <td>{{ user.get('id', '') }}</td>
            <td>{{ user.get('name', '') }}</td>
            <td>{{ user['age'] }}</td>
            <td>
                <a target="_blank"
                   href="/user/detail.html?uid={{ user['id'] }}">
                    查看--/user/detail.html?uid={{ user['id'] }}
                </a>
            </td>
        </tr>
    {% endfor %}
</table>
</body>

```

页面:`user_detail.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>联想班学生-{{ res['name'] }}爱好页面</title>
</head>
<body>
    <h1>"{{ res['name'] }}"学生的爱好</h1>
    <p>
        <h3>学生:{{ res['name'] }} ,年龄:{{ res.get('age') }}</h3>
        <span style="color: red;">
            爱好
        </span>:{{ res.get('other') }}
    </p>
</body>
</html>
```

**获取post方式提交的数据**

引入flask包中的request对象，就可以直接在请求函数中直接使用该对象了。让我们改进下 login() 方法：

```python
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        pwd = request.form.get("pwd")
        if user_name == "admin" and pwd == "123456":
            return '<h1>登陆成功</h1>'
        else:
            return render_template('login.html', **{"error": "账号或密码错误！"})

    # get请求
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

```

在`templates`目录下，添加`login.html`文件：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"> <!--引入公共样式文件style.css和登录样式login.css-->
    <title>登录页面</title>
</head>
<body>
<div class="main">
    <!-- action为提交地址，method为提交方式 -->
    <form action="/login/" method="post">
        <ul>
            <h1>欢迎登录</h1>
            <li>
                <label>账 号：<input type="text" autocomplete="off" name="user_name" required></label>
            </li>
            <li>
                <label>密 码：<input type="password" name="pwd" required></label>
            </li>
            <button>登录</button>

            <!-- 用户登录失败时 提示错误信息-->
            {% if error %}
                <span style="color: red">
                    {{ error }}
                </span>
            {% endif %}
        </ul>
    </form>
</div>
</body>
```

执行上面的例子，结果就不多描述了。简单解释下，`request`中`method`变量可以获取当前请求的方法，即”GET”, “POST”, “DELETE”, “PUT”等；`form`变量是一个字典，可以获取”Post”请求表单中的内容，在上例中，如果提交的表单中不存在`user`项，则会返回一个`KeyError`，你可以不捕获，页面会返回400错误（想避免抛出这`KeyError`，你可以用`request.form.get('user')`来替代）。而`request.args.get()`方法则可以获取”Get”请求URL中的参数，该函数的第二个参数是默认值，当URL参数不存在时，则返回默认值。`request`的详细使用可参阅Flask的[官方API文档](http://flask.pocoo.org/docs/0.10/api/#flask.request)。

#### 会话对象session

会话可以用来保存当前请求的一些状态，以便于在请求之前共享信息。

实例：

```python
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# 使用session，需要设置密钥
# # 密钥要尽量复杂，最好使用一个随机数
app.secret_key = 'a1s@i34!3-&d'

@app.route('/')
def index():
    # 判断'user'是否存在与session中
    if 'user' in session:
        return render_template('admin_index.html')
    # 如果不存在，返回特定信息
    return 'session中无用户信息！！'

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        pwd = request.form.get("pwd")
        if user_name == "admin" and pwd == "123456":
            # 登陆成功后，将user信息保存下来
            session['user'] = user_name
            return redirect(url_for('index'))
        else:
            return render_template('login.html', **{"error": "账号或密码错误！"})

    # get请求
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
```

`templates/admin_index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后台首页</title>
</head>
<body>
{# 判断'user'是否在session中，存在则显示session中保存的用户信息 #}
<h1>
    欢迎
    {% if 'user' in session %}
        {{ session['user'] }}
    {% endif %}

</h1>
</body>
</html>
```

如果不设置密钥会报错：

![image-20220521221100428](https://tva1.sinaimg.cn/large/e6c9d24ely1h2gds0bp5lj21r40byjte.jpg)

再写个“退出登陆”的方法，就是清除字典里的键值：

```python
from flask import request, session, redirect, url_for

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
```

`admin_index.html`中添加“退出”按钮：

```
```



#### 构建响应

在之前的例子中，请求的响应我们都是直接返回字符串内容，或者通过模板来构建响应内容然后返回。其实我们也可以先构建响应对象，设置一些参数（比如响应头）后，再将其返回。修改下上例中的”Get”请求部分：

```python
from flask import request, session, make_response

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        pass
    if 'user' in session:
        pass
    else:
        title = request.args.get('title', 'Default')
        response = make_response(render_template('hello2.html', title=title), 200)
        response.headers['key'] = 'value'
        return response
```

打开浏览器调试，在”Get”请求用户未登录状态下，你会看到响应头中有一个`key`项。`make_response`方法就是用来构建`response`对象的，第二个参数代表响应状态码，缺省就是”200”。`response`对象的详细使用可参阅Flask的[官方API文档](http://flask.pocoo.org/docs/0.10/api/#response-objects)。

#### Cookie的使用

提到了Session，当然也要介绍Cookie，毕竟没有Cookie，Session就根本没法用。Flask中使用Cookie也很简单：

```python
from flask import request, session, make_response
import time

@app.route('/login', methods=['POST', 'GET'])
def login():
    response = None
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))
        ...
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        ...

    return response
```

例子越来越长了，这次我们引入了`time`模块来获取当前系统时间。我们在返回响应时，通过`response.set_cookie()`函数，来设置Cookie项，之后这个项值会被保存在浏览器中。这个函数的第三个参数`max_age`可以设置该Cookie项的有效期，单位是秒，不设的话，在浏览器关闭后，该Cookie项即失效。

在请求中，`request.cookies`对象就是一个保存了浏览器Cookie的字典，使用其`get()`函数就可以获取相应的键值。

#### 全局对象g

`flask.g`是Flask一个全局对象，这里有点容易让人误解，其实`g`的作用范围，就在一个请求（也就是一个线程）里，它不能在多个请求间共享。你可以在`g`对象里保存任何你想保存的内容。一个最常用的例子，就是在进入请求前，保存数据库连接。这个我们会在介绍【数据库集成】时讲到。

### 完整代码

`flask4.py`

```python
from flask import Flask
from flask import render_template, redirect, url_for, request, session, make_response, g
import time

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    response = None
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            response = make_response('No such user!')
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        else:
            title = request.args.get('title', 'Default')
            response = make_response(render_template('hello2.html', title=title), 200)

    return response


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


app.secret_key = '123456'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

`templates/layout.html`

```html
<!doctype html>
<title>Hello Sample</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<div class="page">
    {% block body %}
    {% endblock %}
</div>
```

`templates/layout.html`

```html
{% extends "layout.html" %}
{% block body %}
<form name="login" action="/login" method="post">
    Hello {{ title }}, please login by:
    <input type="text" name="user" />
</form>
{% endblock %}
```

## 五、错误处理及消息闪现

本篇将补充一些Flask的基本功能，包括错误处理，URL重定向，日志功能，还有一个很有趣的消息闪现功能。

### 错误处理

使用`abort()`函数可以直接退出请求，返回错误代码：

```python
from flask import abort

@app.route('/error')
def error():
    abort(404)
```

上例会显示浏览器的404错误页面。有时候，我们想要在遇到特定错误代码时做些事情，或者重写错误页面，可以用下面的方法：

```python
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
```

此时，当再次遇到404错误时，即会调用`page_not_found()`函数，其返回”404.html”的模板页。第二个参数代表错误代码。

不过，在实际开发过程中，我们并不会经常使用`abort()`来退出，常用的错误处理方法一般都是异常的抛出或捕获。装饰器`@app.errorhandler()`除了可以注册错误代码外，还可以注册指定的异常类型。让我们来自定义一个异常：

```python
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response
```

我们在上面的代码中定义了一个异常`InvalidUsage`，同时我们通过装饰器`@app.errorhandler()`修饰了函数`invalid_usage()`，装饰器中注册了我们刚定义的异常类。这也就意味着，一但遇到`InvalidUsage`异常被抛出，这个`invalid_usage()`函数就会被调用。写个路由试一试吧。

```python
@app.route('/exception')
def exception():
    raise InvalidUsage('No privilege to access the resource', status_code=403)
```

### URL重定向

重定向`redirect()`函数的使用在[上一篇](http://www.bjhee.com/flask-4.html)`logout`的例子中已有出现。作用就是当客户端浏览某个网址时，将其导向到另一个网址。常见的例子，比如用户在未登录时浏览某个需授权的页面，我们将其重定向到登录页要求其登录先。

```python
from flask import session, redirect

@app.route('/')
def index():
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        return redirect(url_for('login'), 302)
```

`redirect()`的第二个参数时HTTP状态码，可取的值有301, 302, 303, 305和307，默认即302（为什么没有304？留给大家去思考）。

### 日志

提到错误处理，那一定要说到日志。Flask提供`logger`对象，其是一个标准的`Python Logger`类。修改上例中的`exception()`函数：

```python
@app.route('/exception')
def exception():
    app.logger.debug('Enter exception method')
    app.logger.error('403 error happened')
    raise InvalidUsage('No privilege to access the resource', status_code=403)
```

执行后，你会在控制台看到日志信息。在debug模式下，日志会默认输出到标准错误stderr中。你可以添加`FileHandler`来使其输出到日志文件中去，也可以修改日志的记录格式，下面演示一个简单的日志配置代码：

```python
server_log = TimedRotatingFileHandler('server.log','D')
server_log.setLevel(logging.DEBUG)
server_log.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

error_log = TimedRotatingFileHandler('error.log', 'D')
error_log.setLevel(logging.ERROR)
error_log.setFormatter(logging.Formatter('%(asctime)s: %(message)s [in %(pathname)s:%(lineno)d]'))

app.logger.addHandler(server_log)
app.logger.addHandler(error_log)
```

上例中，我们在本地目录下创建了两个日志文件，分别是”server.log”记录所有级别日志；”error.log”只记录错误日志。我们分别给两个文件不同的内容格式。另外，我们使用了`TimedRotatingFileHandler`并给了参数`D`，这样日志每天会创建一个新的文件，并将旧文件加日期后缀来归档。

你还可以将错误信息发送邮件。更详细的日志使用可参阅[Python logging官方文档](https://docs.python.org/2/library/logging.html)。

### 消息闪现

“Flask Message”是一个很有意思的功能，一般一个操作完成后，我们都希望在页面上闪出一个消息，告诉用户操作的结果。用户看完后，这个消息就不复存在了。Flask提供的`flash`功能就是为了这个。我们还是拿用户登录来举例子：

```python
from flask import render_template, request, session, url_for, redirect, flash

@app.route('/')
def index():
    if 'user' in session:
        return render_template('hello.html', name=session['user'])
    else:
        return redirect(url_for('login'), 302)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        flash('Login successfully!')
        return redirect(url_for('index'))
    else:
        return '''

        '''
```

上例中，当用户登录成功后，就用`flash()`函数闪出一个消息。让我们找回[第三篇](http://www.bjhee.com/flask-3.html)中的模板代码，在”layout.html”加上消息显示的部分：

```html
<!doctype html>
<title>Hello Sample</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class="flash">
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
<div class="page">
    {% block body %}
    {% endblock %}
</div>
```

上例中`get_flashed_messages()`函数就会获取我们在`login()`中通过`flash()`闪出的消息。从代码中我们可以看出，闪出的消息可以有多个。模板”hello.html”不用改。运行下试试。登录成功后，是不是出现了一条”Login successfully”文字？再刷新下页面，你会发现文字消失了。你可以通过CSS来控制这个消息的显示方式。

`flash()`方法的第二个参数是消息类型，可选择的有”message”, “info”, “warning”, “error”。你可以在获取消息时，同时获取消息类型，还可以过滤特定的消息类型。只需设置`get_flashed_messages()`方法的`with_categories`和`category_filter`参数即可。比如，Python部分可改为：

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        flash('Login successfully!', 'message')
        flash('Login as user: %s.' % request.form['user'], 'info')
        return redirect(url_for('index'))
    ...
```

layout模板部分可改为：

```html
...
{% with messages = get_flashed_messages(with_categories=true, category_filter=["message","error"]) %}
  {% if messages %}
    <ul class="flash">
    {% for category, message in messages %}
        <li class="{{ category }}">{{ category }}: {{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
...
```

### 完整代码

`flask5.py`

```python
from flask import Flask
from flask import render_template, request, session, url_for, make_response
from flask import abort, redirect, flash, g
from logging.handlers import TimedRotatingFileHandler
import logging

app = Flask(__name__)

server_log = TimedRotatingFileHandler('server.log','D')
server_log.setLevel(logging.DEBUG)
server_log.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s'
))

error_log = TimedRotatingFileHandler('error.log', 'D')
error_log.setLevel(logging.DEBUG)
error_log.setFormatter(logging.Formatter(
    '%(asctime)s: %(message)s [in %(pathname)s:%(lineno)d]'
))

app.logger.addHandler(server_log)
app.logger.addHandler(error_log)

@app.route('/')
def index():
    if 'user' in session:
        return render_template('hello.html', name=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        flash('Login successfully!', 'message')
        flash('Login as user: %s.' % request.form['user'], 'info')
        return redirect(url_for('index'))
    else:
        return '''
        <form name="login" action="/login" method="post">
            Username: <input type="text" name="user" />
        </form>
        '''

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'), 302)

@app.route('/error')
def error():
    app.logger.debug('Enter error method')
    app.logger.error('404 error happened')
    abort(404)


@app.route('/exception')
def exception():
    app.logger.debug('Enter exception method')
    app.logger.error('403 error happened')
    raise InvalidUsage('No privilege to access the resource', status_code=403)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response

app.secret_key = '12345678'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

templates/404.html

```html
<h1>Error: Page not found!</h1>
```

templates/hello.html

```html
{% extends "layout.html" %}
{% block body %}
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
{% endblock %}

```



templates/layout.html

```html
<!doctype html>
<title>Hello Sample</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
{% with messages = get_flashed_messages(with_categories=true, category_filter=["message","error"]) %}
  {% if messages %}
    <ul class="flash">
    {% for category, message in messages %}
      <li class="{{ category }}">{{ category }}: {{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
<div class="page">
    {% block body %}
    {% endblock %}
</div>
```

