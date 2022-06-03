from flask import Flask, redirect, request, render_template, url_for
import service
from utils import setting_utils

app = Flask(__name__)
# 解决flask接口中文数据编码问题
app.config['JSON_AS_ASCII'] = False

# 读取配置信息
settings = setting_utils.read_settings()


@app.route('/')
def hello():
    return redirect(url_for("kaoqin"))


@app.route('/kaoqin/')
def kaoqin():
    cs_info = service.read_cs()  # 班级和学生信息
    if not cs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    courses = list(cs_info.keys())  # 课程：如政治、语文
    course = request.args.get("course")  # get请求传递过来的课程
    if not course:
        course = courses[0]

    data = {
        "courses": courses,  # 所有课程
        "course": course,  # 当前请求对课程
        "cs_info": cs_info[course],  # 班级和学生信息
        "kaoqin": service.all_situation()  # 考勤的所有情况
    }
    return render_template('kaoqin.html', data=data)


@app.route('/submit_kq/<course>/', methods=['GET', "POST"])
def submit_kq(course):
    if request.method == "POST":
        # todo
        return request.form
    return "get请求"
