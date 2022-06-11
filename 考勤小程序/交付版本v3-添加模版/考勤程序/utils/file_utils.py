import shutil
import os
import re

SETTING_PATH = "0-说明文档和配置文档/配置文档.txt"
READ_FILE = "1-学生名单表/学生名单.xlsx"
SAVE_FILE = "2-考勤结果/考勤总表.xlsx"


def read_settings(path):
    """读取配置文件"""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    kq_situations = re.findall("""考勤的所有情形：\n(.*?)\n注意""", text, re.S)
    lesson = re.findall("需要考勤的课程：\n(.*?)\n注意", text, re.S)
    return {
        "kq_situ": kq_situations[0],
        "lessons": lesson[0]
    }


def read_description(path):
    """ 读取说明文档 """
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def get_files(folder_path):
    """获取文件夹下的所有文件"""
    return os.listdir(folder_path)


def is_file_exist(file):
    """ 判断文件是否存在 """
    return os.path.exists(file)


def copy_file(source_file, to_file):
    """ 复制文件 """
    shutil.copy(source_file, to_file)


if __name__ == '__main__':
    path = "../../0-说明文档和配置文档/说明文档.txt"
    # print(get_files(path))
    # r = read_description(path)
    # print(r)
    path = "../../0-说明文档和配置文档/配置文档.txt"
    r = read_settings(path)
    print(r)
