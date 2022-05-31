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
