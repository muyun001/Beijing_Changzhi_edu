import datetime


def get_date():
    """获取当前的年月日"""
    # 获取当地时间
    now = datetime.datetime.now()
    return now.year, now.month, now.day


def lesson_judge():
    """ 判断此时是第几节课 """
    # 每节课的时间段
    lessons = [
        ["08:15:00", "08:55:00"],  # 第1节课
        ["09:10:00", "09:50:00"],  # 第2节课
        ["10:25:00", "11:05:00"],  # 第3节课
        ["11:20:00", "12:00:00"],  # 第4节课

        ["13:30:00", "14:10:00"],  # 第5节课
        ["14:25:00", "15:05:00"],  # 第6节课
        ["15:25:00", "16:05:00"],  # 第7节课
    ]
    now = datetime.datetime.now()
    today = str(datetime.date.today())

    # 判断此时是第几节课
    index = 0
    for time_zone in lessons:
        index += 1
        start_time = datetime.datetime.strptime(f"{today} {time_zone[0]}", "%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.strptime(f"{today} {time_zone[1]}", "%Y-%m-%d %H:%M:%S")

        # todo 需要完善
        if start_time < now < end_time:
            return index
    else:
        print("现在好像是课余时间")
