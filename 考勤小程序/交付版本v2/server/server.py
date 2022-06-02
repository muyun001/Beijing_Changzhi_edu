import json
import sys

from flask import Flask, redirect, request, render_template, url_for
import traceback
import os
from utils import excel_utils, setting_utils, file_utils, others

# try:
#     from utils import excel_utils, setting_utils, file_utils
# except ModuleNotFoundError:
#     from sys import path
#     sys.path.append('../utils/')
#     from ..utils import excel_utils, setting_utils, file_utils

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
    files = file_utils.get_files(set['read_folder'])
    for f in files:
        if "~" not in f and "xlsx" in f:
            path = os.path.abspath(set['read_folder']) + "/" + f
            data = excel_utils.read_excel_cs(path)
            return render_template('kaoqin.html', data=data, kq_ab=others.all_situation())
    return "目录中没有可读取文件，或者不是'xlsx'文件，请练习联想班学员 ^_^"


@app.route('/submit_kq/', methods=['GET', "POST"])
def submit_kq():
    if request.method == "POST":
        return request.form
    return "get请求"


if __name__ == '__main__':
    app.run(debug=True)
