from utils import excel_utils, setting_utils, file_utils, others

# 读取配置信息
settings = setting_utils.read_settings()


def all_situation():
    """考勤异常的所有情形"""
    return others.str_to_dict(settings['kq_abnormal'])


def get_read_file():
    """ 从【1-学生名单表】中获取文件名（包含文件路径） """
    files = file_utils.get_files(others.get_abspath(settings['read_folder']))
    for f in files:
        if not others.is_excel(f):
            # 如果不是正常excel文件，就继续判断下一个文件
            continue
        read_file = f"{others.get_abspath(settings['read_folder'])}/{f}"
        return read_file


def read_cs():
    """ 读取科目、班级和学生数据 """
    path = get_read_file()
    if not path:
        return
    data = excel_utils.read_excel_cs(path)
    return data
