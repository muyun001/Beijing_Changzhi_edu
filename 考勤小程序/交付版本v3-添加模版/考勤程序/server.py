from flask import Flask, redirect, request, render_template, url_for
import service

app = Flask(__name__)
# 解决flask接口中文数据编码问题
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello():
    return redirect(url_for("home"))


@app.route('/get_courses/')
def get_courses():
    """ 获取科目 """
    ccs_info = service.read_cs()  # 班级和学生信息
    if not ccs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    return {"courses": list(ccs_info.keys())}  # 课程：如政治、语文


@app.route("/get_classes/<course>/")
def get_classes(course):
    """ 根据科目，获取它对应的哪些班级 """
    ccs_info = service.read_cs()  # 科目、班级和学生信息
    if not ccs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    cs_info = ccs_info.get(course)  # 班级、学生信息
    if not cs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    d = {"course": course, "classes": list(cs_info.keys())}
    return d


@app.route('/get_cls_students/<cls>/')
def get_cls_students(cls):
    """ 获取某班级的学生名单 """
    data = {"classes": cls, "students": []}  # 班级、学生名单
    ccs_info = service.read_cs()  # 科目、班级和学生信息
    if not ccs_info:
        return "目录中没有可读取文件，或者不是'xlsx'文件，请联系联想班学员帮您解决问题 ^_^"
    for course, cs_info in ccs_info.items():
        if cls in list(cs_info.keys()):
            data["students"] = cs_info[cls]
            return data
    return data


@app.route('/home/')
def home():
    """ 主页 """
    course = request.args.get("course")
    courses = get_courses().get('courses')  # 获取所有科目
    if not course:
        course = courses[0]

    data = {
        "courses": courses,  # 所有课程
        "course": course,  # 当前请求对课程
        "cs_info": service.read_cs()[course],  # 班级和学生信息
        "kaoqin": service.all_situation(),  # 考勤的所有情况
        "classes": get_classes(course)["classes"],
        "lessons": service.get_lessons(),
        "description": service.get_desc(),
        "settings": service.get_settings(),
        "cls_imgs": service.get_imgs()
    }
    return render_template('home.html', data=data)


@app.route('/kaoqin/')
def kaoqin():
    """ 科目的考勤 """
    course = request.args.get("course")
    courses = get_courses().get('courses')  # 获取所有科目
    if not course:
        course = courses[0]

    data = {
        "courses": courses,  # 所有课程
        "course": course,  # 当前请求的课程
        "cs_info": service.read_cs()[course],  # 班级和学生信息
        "kaoqin": service.all_situation(),  # 考勤的所有情况
        "classes": get_classes(course)["classes"],
        "lessons": service.get_lessons()
    }
    return render_template('kaoqin.html', data=data)


@app.route('/submit_kq/<course>/', methods=['GET', "POST"])
def submit_kq(course):
    """ 考勤数据的提交 """
    if request.method == "POST":
        kaoqin_info = request.form.to_dict()
        kaoqin_info['course'] = course
        # 将数据保存到excel
        service.save_kaoqin_data(kaoqin_info)
        return redirect(url_for('kaoqin'))
    return """<script>alert("现在是get请求，请求有误，请联系联想班学员处理。")</script>"""


@app.route("/settings/", methods=["POST"])
def submit_settings():
    """ 接收提交的配置信息，并保存到配置文件中 """
    old_sett = service.get_settings()  # 读取原配置，方便后面做对比
    if request.method == "POST":
        new_sett = request.form.to_dict()
        # 判断原设置数据和提交上来的配置数据是否相同
        # 如果不同，则按照提交配置进行更改
        for k, v in new_sett.items():
            # 如果配置相同，则无需更改，跳过
            if old_sett[k].replace('\n', "") == new_sett[k].replace('\r', "").replace('\n', ""):
                continue
            # 不同的数据，判断是哪些地方不同
            # 如果是考勤情形不同，则修改考勤内容
            # 如果是上课情形不同，则修改上课情形
            service.save_setting(old_sett[k], v)
    return redirect(url_for('hello'))


@app.route('/kq_analyse/')
def kq_analyse():
    """ 考勤分析 """

    return render_template('kq_analyse.html')
