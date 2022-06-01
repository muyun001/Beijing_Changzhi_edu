import json
import sys

from flask import Flask, redirect, request, render_template, url_for
import traceback
import os
from utils import excel_utils, setting_utils, file_utils

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
IS_OPEN_VOICE, READ_FOLDER, SAVE_FOLDER, KQ_ABNORMAL = setting_utils.read_settings()


@app.route('/')
def hello():
    return redirect(url_for("kaoqin"))


@app.route('/kaoqin/')
def kaoqin():
    files = file_utils.get_files(READ_FOLDER)
    for f in files:
        if "~" not in f and "xlsx" in f:
            path = os.path.abspath(READ_FOLDER) + "/" + f
            data = excel_utils.read_excel_cs(path)
            return data
    return "目录中没有可读取文件，或者不是'xlsx'文件，请练习联想班学员 ^_^"


if __name__ == '__main__':
    app.run(debug=True)
