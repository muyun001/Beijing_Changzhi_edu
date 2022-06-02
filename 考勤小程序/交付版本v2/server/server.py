import json
import sys

from flask import Flask, redirect, request, render_template, url_for
import traceback
import os
from utils import excel_utils, setting_utils, file_utils, others

app = Flask(__name__)
# 解决flask接口中文数据编码问题
app.config['JSON_AS_ASCII'] = False

# 读取配置信息
set = setting_utils.read_settings()


@app.route('/')
def hello():
    return redirect(url_for("kaoqin"))


@app.route('/kaoqin/')
def kaoqin():
    course = request.args.get("course")
    files = file_utils.get_files(set['read_folder'])
    for f in files:
        if not others.is_excel(f):
            # 如果不是正常excel文件，就继续判断下一个文件
            continue
        path = f"{os.path.abspath(set['read_folder'])}/{f}"
        data = excel_utils.read_excel_cs(path)
        courses = list(data.keys())
        if not course:
            course = courses[0]
        return render_template('kaoqin.html', courses=courses, data=data[course], kq_ab=others.all_situation())
    return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员 ^_^"


@app.route('/submit_kq/', methods=['GET', "POST"])
def submit_kq():
    if request.method == "POST":
        return request.form
    return "get请求"


if __name__ == '__main__':
    app.run(debug=True)
