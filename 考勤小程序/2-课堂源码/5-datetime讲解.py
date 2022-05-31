import time
import datetime  # 时间

# 获取年月日
local_time = time.localtime()
year = local_time.tm_year
month = local_time.tm_mon
day = local_time.tm_mday
print(year, month, day)

now = datetime.datetime.now()
print(now)
print(type(now))  # datetime

# 时间格式化：datetime类型转成str类型：strftime
# 2022-05-09 08:47:38.029367
# 2022年05月09日 08时47分38秒
"""
年:year      %Y
月:month     %m
日:day       %d
时:hour      %H
分:minute    %M
秒:second    %S
"""
# 2022年05月09日 08时47分38秒
time1 = now.strftime("%Y年%m月%d日 %H时%M分%S秒")  # 2022年05月09日 08时52分15秒
# 2022-05-09 08:47:38
time2 = now.strftime("%Y-%m-%d %H:%M:%S")  # 2022-05-09 08:55:14
# 2022-05-09
time3 = now.strftime("%Y-%m-%d")  # 2022-05-09
# 08:55:14
time4 = now.strftime("%H:%M:%S")  # 08:56:21

# 2022-05-09 08:00:00
time5 = now.strftime("%Y-%m-%d %H:00:00")  # 2022-05-09 08:00:00
# 2022-05-09 08:57:00
time6 = now.strftime("%Y-%m-%d %H:%M:00")  # 2022-05-09 08:57:00
print(time1)
print(time2)
print(time3)
print(time4)
print(time5)
print(time6)

# 将str类型转成datetime类型
# 2022-05-09 08:57:00
now = datetime.datetime.now()
time7 = now.strptime("2022-05-05 08:57:00", "%Y-%m-%d %H:%M:%S")
time8 = now.strptime("2022年05月09日 08时57分00秒", "%Y年%m月%d日 %H时%M分%S秒")  # 2022-05-09 08:57:00
print(time7)
print(time8)
print(type(time7))

# 把str类型转成datetime类型：strptime
time9 = datetime.datetime.strptime("2022-05-05 08:57:00", "%Y-%m-%d %H:%M:%S")  # 2022-05-05 08:57:00
print(time9)

# 时间的推移
# timedelta
now = datetime.datetime.now()
time10 = now - datetime.timedelta(days=3)  # 向前推移3天
time11 = now + datetime.timedelta(days=3)  # 向后推迟3天
# print(time10)
# print(time11)
time12 = now - datetime.timedelta(hours=3)  # 向前推移3小时
time13 = now + datetime.timedelta(hours=3)  # 向后推迟3小时
# print(time12)
# print(time13)
time14 = now - datetime.timedelta(minutes=3)  # 向前推移3分钟
time15 = now + datetime.timedelta(minutes=3)  # 向后推迟3分钟
# print(time14)
# print(time15)

# 开始时间、结束时间
start_time = datetime.datetime.now()  # 此时
end_time = datetime.datetime.now() + datetime.timedelta(minutes=10)  # 十分钟之后
# print(start_time, end_time)

# 判断某个时间点是否位于start_time~end_time之间的前提是：必须是datetime类型
# 开始时间：10分钟之前
now = datetime.datetime.now()
start_time = now - datetime.timedelta(minutes=10)
# 结束时间：10分钟之后
end_time = now + datetime.timedelta(minutes=10)
print(start_time < now < end_time)

# 今天是否是2022年5月5号～2022年5月15号之间？
# 需要把"2022-5-5" 转成 datetime类型
# 需要把"2022-5-15" 转成 datetime类型
now = datetime.datetime.now()
start_time = datetime.datetime.strptime("2022-5-5", "%Y-%m-%d")
end_time = datetime.datetime.strptime("2022-5-15", "%Y-%m-%d")
# print(start_time, end_time)

print(start_time < now < end_time)

datetime.datetime.today()
datetime.date.today()

"""
需求：
1、判断此时此刻是否在 '2022年5月9日10:00~2022年5月9日12:00' 这个时间段内.
2、不将日期写死，即判断时间是否在【当天】的10:00~12:00之间
"""
# 1、判断此时此刻是否在 '2022年5月9日10:00~2022年5月9日12:00' 这个时间段内.
now = datetime.datetime.now()
start_time = datetime.datetime.strptime("2022-5-9 10:00", "%Y-%m-%d %H:%M")
end_time = datetime.datetime.strptime("2022-5-9 11:00", "%Y-%m-%d %H:%M")
print(start_time < now < end_time)

# 2、不将日期写死，即判断时间是否在【当天】的10:00~12:00之间
now = datetime.datetime.now()
today = datetime.date.today()  # 2022-5-9
today_str = str(datetime.date.today())  # 2022-5-9
print(type(today_str))
print(today_str)
start_time = datetime.datetime.strptime(today_str + " 10:00", "%Y-%m-%d %H:%M")
end_time = datetime.datetime.strptime(today_str + " 11:00", "%Y-%m-%d %H:%M")
print(start_time < now < end_time)

"""
需求：
如果给到每节课的时间段，能否判断此时是第几节课
如果在某个时间段内，就输出是第几节课。否则输出是"此时是课余时间"
"""
"""
# start_time < now < end_time
["15:25:00", "16:05:00"]
# datetime类型
2022-5-9 15:25:00       2022-5-9 16:05:00
# str类型
2022-5-9 15:25:00       2022-5-9 16:05:00
# 15:25:00      16:05:00已经给出，那么就需要我们去获取今天的日期
today_str = str(datetime.date.today())
"""

lessons = [["08:15:00", "08:55:00"],  # 第1节课
           ["09:10:00", "09:50:00"],  # 第2节课
           ["10:25:00", "11:05:00"],  # 第3节课
           ["11:20:00", "12:00:00"],  # 第4节课

           ["13:30:00", "14:10:00"],  # 第5节课
           ["14:25:00", "15:05:00"],  # 第6节课
           ["15:25:00", "16:05:00"],  # 第7节课
           ]

now = datetime.datetime.now()
today_str = str(datetime.date.today())
lesson_num = 0
for l in lessons:
    lesson_num += 1
    start_time_str = today_str + " " + l[0]
    end_time_str = today_str + " " + l[1]

    start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    if start_time < now < end_time:
        print(f"此时是第{lesson_num}节课")
        break

    if lesson_num == len(lessons):
        print("此时是课余时间")
