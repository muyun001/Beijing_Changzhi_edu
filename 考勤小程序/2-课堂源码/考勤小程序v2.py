import time
import pyttsx3 as pt
import pandas as pd

"""
考勤小程序v1
流程：
1。读取数据
2。遍历所有学生，判断考勤情况
3。将考勤情况保存到excel文件
    - 获取日期
"""

FILE_PATH = "../files/联想未来班名单测试版.xlsx"


def read_excel():
    """读取数据"""
    # 从excel读取数据
    data = pd.read_excel(FILE_PATH)  # DataFrame数据类型-二维
    return data


def voice_read():
    """声音"""
    engine = pt.init()
    engine.setProperty('rate', 170)  # 获取默认的语速
    # engine.setProperty('voice', voices[0].id)  # 设置为男声
    # engine.setProperty('voice', voices[1].id)  # 设置为女声
    return engine


def kaoqin(students):
    """判断考勤是否异常"""
    kaoqin = []  # 考勤
    shuoming = []  # 说明
    engine = voice_read()

    for name in students:
        print(f"1-请假，2-参加活动，3-迟到，4-旷课，考勤正常请直接回车。")
        engine.say(f"{name} 到了没？")
        engine.runAndWait()

        input_num = input()
        if not input_num:
            # 考勤正常
            kaoqin.append("考勤正常")
            shuoming.append("")
            continue

        # 考勤异常
        kaoqin.append("考勤异常")
        if input_num == "1":
            shuoming.append("请假")
        elif input_num == "2":
            shuoming.append("参加活动")
        elif input_num == "3":
            shuoming.append("迟到")
        elif input_num == "4":
            shuoming.append("旷课")
        else:
            print("输入有误！")

    return kaoqin, shuoming


def get_date():
    """获取当前日期"""
    # 获取当地时间
    time_local = time.localtime()
    # 获取年份
    year = time_local.tm_year
    # 获取月份
    month = time_local.tm_mon
    # 获取日子
    day = time_local.tm_mday
    return year, month, day


def save_excel(data):
    """保存数据到excel文件"""
    year, month, day = get_date()
    # 将数据保存到excel, index=False是去掉第一列的索引
    data.to_excel(f"../files/{year}年{month}月{day}日联想未来班考勤表测试版.xlsx", index=False)


def main():
    data = read_excel()
    students = data["名单"]

    kaoqin_list, shuoming_list = kaoqin(students)
    data["考勤"] = kaoqin_list
    data["说明"] = shuoming_list

    save_excel(data)


if __name__ == '__main__':
    main()
