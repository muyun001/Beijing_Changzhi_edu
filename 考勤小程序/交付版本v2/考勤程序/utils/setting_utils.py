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
    is_open_voice = re.search(".*语音播报.*?【(\d)】", text, re.S)
    read_folder = re.search("需要考勤的目录名：【(.*?)】", text, re.S)
    save_folder = re.search("生成考勤结果的目录名：【(.*?)】", text, re.S)
    kq_abnormal = re.search("""考勤异常情况：(.*?)注意: .*【考勤异常】""", text, re.S)
    lesson = re.search("上课情况：\n(.*?)\n注意：如果您有其他上课需求", text, re.S)
    if not is_open_voice:
        raise Exception("是否需要语音播报？需要您在【配置文件.txt】中进行配置。")
    if not read_folder.group(1):
        raise Exception("考勤的目录名，需要您在【配置文件.txt】中进行配置。")
    if not save_folder.group(1):
        raise Exception("保存考勤结果的目录名，需要您在【配置文件.txt】中进行配置。")

    return {
        "is_open_voice": int(is_open_voice.group(1)),
        "read_folder": read_folder.group(1),
        "save_folder": save_folder.group(1),
        "kq_abnormal": kq_abnormal.group(1),
        "lessons": lesson.group(1)
    }


if __name__ == '__main__':
    path = os.path.abspath('../..') + "/0-说明文档和配置文档/配置文档.txt"
    print(read_settings(path))
