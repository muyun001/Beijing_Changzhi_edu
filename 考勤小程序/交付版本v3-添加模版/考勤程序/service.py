from utils import excel_utils, file_utils, others
import os


def get_settings():
    """ 读取配置数据 """
    # 读取配置信息
    try:
        sett_dict = file_utils.read_settings(os.getcwd() + "/0-说明文档和配置文档/配置文档.txt")
    except FileNotFoundError:
        sett_dict = file_utils.read_settings(os.path.abspath('..') + "/0-说明文档和配置文档/配置文档.txt")
    return sett_dict


def update_sett(sett_dict):
    """ 更新设置中key的值 """
    sett_dict["需要考勤的目录名"] = sett_dict.pop("read_folder")
    sett_dict["生成考勤结果的目录名"] = sett_dict.pop("save_folder")
    sett_dict["考勤的所有情形"] = sett_dict.pop("kq_situ")
    sett_dict["需要考勤的课程"] = sett_dict.pop("lessons")
    return sett_dict


def all_situation():
    """考勤的所有情形"""
    return others.str_to_dict(get_settings()['kq_situ'])


def get_read_file():
    """ 从【1-学生名单表】中获取文件名（包含文件路径） """
    files = file_utils.get_files(others.get_abspath(get_settings()['read_folder']))
    for f in files:
        if not others.is_excel(f):
            # 如果不是正常excel文件，就继续判断下一个文件
            continue
        read_file = f"{others.get_abspath(get_settings()['read_folder'])}/{f}"
        return read_file


def get_save_file():
    save_file = others.get_abspath(get_settings()['save_folder']) + "/" + file_utils.SAVE_FILE
    return save_file


def read_cs():
    """ 读取科目、班级和学生数据 """
    path = get_read_file()
    if not path:
        return
    data = excel_utils.read_excel_cs(path)
    return data


def convert_data(data):
    """
    将数据转成下面这种格式 :
    {
        "course":"语文",
        "lesson":"第一节课",
        "考勤情况": {
            "1班":{"崔昊元":"考勤正常", "张子豪":"迟到", "牛皓冬":"考勤正常"},
            "2班":{"杨梓琦":"考勤正常", "蒋文拓":"迟到", "吕铭":"考勤正常"}
        }
    }
    """
    result = {"course": data["course"], "lesson": data['lesson'], "考勤情况": {}}
    classes = []
    for k in data.keys():
        if "kq" in k:
            classes.append(k.split('-')[1])
    for c in list(set(classes)):
        result["考勤情况"][c] = {}

    for k, v in data.items():
        if "kq" in k:
            cls = k.split('-')[1]  # 班级
            s = k.split('-')[2]  # 学生
            result["考勤情况"][cls][s] = v
    return result


def get_lessons():
    """ 获取课程情况（有哪几节课） """
    return get_settings()['lessons'].split('\n')


def get_desc():
    """ 获取配置文件数据 """
    try:
        desc = file_utils.read_description(os.getcwd() + "/0-说明文档和配置文档/说明文档.txt")
    except FileNotFoundError:
        desc = file_utils.read_description(os.path.abspath('..') + "/0-说明文档和配置文档/说明文档.txt")
    return desc[1:]


def save_kaoqin_data(data):
    """ 将考勤数据保存到excel """
    data = convert_data(data)
    save_file = get_save_file()
    excel_utils.save_excel_openpyxl(data, save_file)


if __name__ == '__main__':
    print(get_desc())
