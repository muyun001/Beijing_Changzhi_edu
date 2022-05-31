import time
import utils

import pandas as pd

"""
所有人的考勤
流程：
1、读取excel文件，获得人员的名单
2、名单考勤
3、将考勤结果保存到excel
    - xx年xx月xx日联想未来班考勤表.xlsx
"""

FILE_PATH = "联想未来班名单测试版.xlsx"


def kaoqin(students):
    """对名单进行考勤"""
    kaoq = []
    shuom = []
    for name in students:
        print(name)
        input_num = input(f"{name}来了没？正常的话就直接回车。1-迟到，2-旷课，3-参加活动")
        if input_num == "":
            # 考勤正常
            kaoq.append("考勤正常")
            shuom.append("")
        else:
            # 考勤异常
            kaoq.append("考勤异常")
            if input_num == "1":
                shuom.append("迟到")
            elif input_num == "2":
                shuom.append("旷课")
            elif input_num == "3":
                shuom.append("参加活动")
            else:
                print("您的输入有误！")

    return kaoq, shuom


def main():
    # 1、获取所有学生名单
    data = utils.read_excel(FILE_PATH)

    # 2、考勤
    data["考勤"], data["说明"] = kaoqin(data["名单"])

    # 3、将考勤数据保存到excel
    year, month, day = utils.get_date()
    file_path = f"{year}年{month}月{day}日联想未来班考勤表.xlsx"
    utils.save_excel(data, file_path)


# 程序的主要入口
if __name__ == '__main__':
    main()
