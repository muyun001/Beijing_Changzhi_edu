from flask import Flask, redirect, request, render_template, url_for
import service

app = Flask(__name__)
# 解决flask接口中文数据编码问题
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello():
    return redirect(url_for("kaoqin"))


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


@app.route('/kaoqin/')
def kaoqin():
    """ 科目的考勤 """
    course = request.args.get("course")
    courses = get_courses().get('courses')  # 获取所有科目
    if not course:
        course = courses[0]

    data = {
        "courses": courses,  # 所有课程
        "course": course,  # 当前请求对课程
        "cs_info": service.read_cs()[course],  # 班级和学生信息
        "kaoqin": service.all_situation(),  # 考勤的所有情况
        "classes": get_classes(course)["classes"]
    }
    return render_template('kaoqin.html', data=data)


@app.route('/submit_kq/<course>/', methods=['GET', "POST"])
def submit_kq(course):
    if request.method == "POST":
        kaoqin_info = request.form.to_dict()
        kaoqin_info['course'] = course
        # 将数据保存到excel
        service.save_kaoqin_data(kaoqin_info)

        return "<h1>考勤结果保存成功，<a href='/'>点击此处</a>重新进行考勤。</h1>"
    return "现在是get请求，请求有误，请联系联想班学院处理。"
