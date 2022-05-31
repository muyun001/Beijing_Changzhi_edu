import utils
import pyttsx3

"""
考勤小程序v2
流程：
1。读取数据
2。遍历所有学生，判断考勤情况
    - 需要语音将学生的名字读出来
3。将考勤情况保存到excel文件
    - 获取日期

要求：使用分模块的方式完成。
"""
FILE_PATH = "联想未来班名单测试版.xlsx"


def kaoqin(students):
    # 发音
    engine = utils.voice_read()

    kaoq = []
    shuom = []
    for name in students:
        print(name)

        engine.say(name + "到了没？")
        engine.runAndWait()

        input_num = input(f"正常的话就直接回车。1-迟到，2-旷课，3-参加活动")
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
    engine.stop()

    return kaoq, shuom


def main():
    data = utils.read_excel(FILE_PATH)
    data["考勤"], data["说明"] = kaoqin(data["名单"])

    year, month, day = utils.get_date()
    save_path = f"{year}年{month}月{day}日联想未来班考勤表.xlsx"
    utils.save_excel(data, save_path)


if __name__ == '__main__':
    main()
