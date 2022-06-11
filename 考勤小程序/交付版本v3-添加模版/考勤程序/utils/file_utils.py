import shutil
import os
import os.path
import re

SETTING_PATH = "0-说明文档和配置文档/配置文档.txt"
SAVE_FILE = "考勤总表.xlsx"


def read_settings(path):
    """读取配置文件"""
    f = open(path, "r", encoding="utf-8")
    text = f.read()
    f.close()
    # 正则表达式：re
    # 读取"是否需要开启程序语音"
    is_open_voice = re.findall(".*语音播报.*?【(\d)】", text, re.S)
    read_folder = re.findall("需要考勤的目录名：【(.*?)】", text, re.S)
    save_folder = re.findall("生成考勤结果的目录名：【(.*?)】", text, re.S)
    kq_situations = re.findall("""考勤的所有情形：\n(.*?)\n注意""", text, re.S)
    lesson = re.findall("需要考勤的课程：\n(.*?)\n注意", text, re.S)
    if not is_open_voice:
        is_open_voice = ["0"]
        # raise Exception("是否需要语音播报？需要您在【配置文件.txt】中进行配置。")
    if not read_folder:
        read_folder = ["1-学生名单表"]
    if not save_folder:
        save_folder = ["2-考勤结果"]

    return {
        # "is_open_voice": int(is_open_voice[0]),
        "read_folder": read_folder[0],
        "save_folder": save_folder[0],
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
