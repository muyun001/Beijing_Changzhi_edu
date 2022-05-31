import utils

"""
考勤小程序v1
流程：
1。读取数据
2。遍历所有学生，判断考勤情况
3。将考勤情况保存到excel文件
    - 获取日期
"""


def kaoqin(students):
    """判断考勤是否异常"""
    kaoqin = []  # 考勤
    shuoming = []  # 说明
    # engine = utils.voice_read()

    for name in students:
        input_num = input(f"{name}：1-请假，2-参加活动，3-迟到，4-旷课，考勤正常请直接回车。")
        # engine.say(f"{name} 到了没？")
        # engine.runAndWait()
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
    # engine.stop()
    return kaoqin, shuoming


def main():
    FILE_PATH = "{}名单.xlsx"
    num = input("您现在是在几楼上课？【请填入数字】：")
    lesson_num = input("请问现在是第几节课？【请填入数字：】(如果是晨读请填写-1、晚自习填写-2)")
    if num == "5":
        _class = "5楼学生"
    else:
        _class = "2楼学生"
    FILE_PATH = FILE_PATH.format(_class)

    data = utils.read_excel(FILE_PATH)
    data["考勤"], data["说明"] = kaoqin(data["名单"])

    year, month, day = utils.get_date()
    if lesson_num == "-1":
        path = f"{year}年{month}月{day}日{_class}晨读考勤表.xlsx"
    elif lesson_num == "-2":
        path = f"{year}年{month}月{day}日{_class}晚自习考勤表.xlsx"
    else:
        path = f"{year}年{month}月{day}日{_class}第{lesson_num}节课考勤表.xlsx"

    utils.save_excel(data, path)


if __name__ == '__main__':
    main()
