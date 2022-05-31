import traceback

import utils

# 读取配置信息
IS_OPEN_VOICE, READ_FOLDER, SAVE_FOLDER, KQ_ABNORMAL = utils.read_settings()


def all_situation():
    """考勤异常的所有情形"""
    return utils.str_to_dict(KQ_ABNORMAL)


def kaoqin(students, is_evening_study=False):
    """考勤"""
    print("-------------- 开始考勤 ---------------")

    if students.empty:
        raise Exception("您需要考勤的名单为空，请您验证excel文件。")

    kaoqin, shuoming = [], []  # 考勤、说明
    engine = utils.voice_read()  # 语音的播报引擎
    sits = all_situation()  # 所有考勤异常的情形

    # 如果是晚自习，就加入"走读"选项
    if is_evening_study:
        sits["7"] = "走读"
        sits["8"] = "其他情况"

    for name in students:
        # 根据配置，判断是否启动语音
        if IS_OPEN_VOICE:
            engine.say(name)
            engine.runAndWait()

        input_num = input(f"{name}：【{utils.dict_to_str(sits)}】，考勤正常请直接回车：")

        # 考勤正常
        if not input_num:
            kaoqin.append("考勤正常")
            shuoming.append("")
            continue

        # 如果输错的话（不是数字），再提供一次输入的机会
        if not input_num.isdigit():
            input_num = input(f"{name}：【{utils.dict_to_str(sits)}】，请您【输入数字】，如果考勤正常请【直接回车】：")

        # 考勤异常
        kaoqin.append("考勤异常")
        for k, v in sits.items():
            if input_num == k:
                shuoming.append(v)
                break
        else:
            print('您的输入有误！自动添加为"其他情况".')
            shuoming.append("其他情况")

    print("-------------- 考勤结束 ---------------")
    engine.stop()
    return kaoqin, shuoming


def choose_file(files):
    """选择考勤名单"""
    if not files:
        raise Exception(f"在您的【{READ_FOLDER}】目录中没有发现需要考勤的人员名单。")

    # 如果只有1个文件，则无需选择
    if len(files) == 1:
        return files[0]

    print(f"----- 有以下{len(files)}个考勤名单 -----")

    # 循环输出
    for f in range(1, len(files) + 1):
        print(f"第{f}个：{files[f - 1]}")
    print("--------------------------")

    # 选择考勤名单
    num = input("您需要对第几个名单进行考勤？【请输入数字】：")
    if not num.isdigit():
        num = input("请问您选择第几个？【只需要输入数字即可（比如1）】：")
        if not num.isdigit():
            raise Exception("没有输入数字，程序退出。")

    return files[int(num) - 1]


def main():
    files = utils.get_files(READ_FOLDER)  # 获取所有考勤名单
    read_file = choose_file(files)
    # print("您现在的考勤名单是：", read_file)
    lesson_num = input("您现在是第几节课？（请直接写【数字】，若是晨读请写【-1】，晚自习请写【-2】）：")

    # 获取考勤数据
    data = utils.read_excel(rf"{READ_FOLDER}/{read_file}")
    # 如果是晚自习，就加入"走读"选项
    if lesson_num == "-2":
        data["考勤"], data["说明"] = kaoqin(data["名单"], True)
    else:
        data["考勤"], data["说明"] = kaoqin(data["名单"])

    # 拼接文件名
    year, month, day = utils.get_date()
    _path = f"{SAVE_FOLDER}/{year}年{month}月{day}日{utils.key_info(read_file)}"
    if lesson_num == "-1":
        path = _path + "晨读考勤表.xlsx"
    elif lesson_num == "-2":
        path = _path + "晚自习考勤表.xlsx"
    else:
        path = _path + f"第{lesson_num}节课考勤表.xlsx"

    # 保存数据
    utils.save_excel(data, path)


if __name__ == '__main__':
    try:
        main()
    except:
        traceback.print_exc()
