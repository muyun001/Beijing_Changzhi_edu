from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route("/hello/<name>/")
def hello(name=None):
    # return f"hello {name}"
    return render_template("hello.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)
