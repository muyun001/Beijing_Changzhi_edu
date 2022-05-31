import datetime


"""
1、获取当前的时间
注意格式：时间格式
"""
# 获取当前的时间：datetime类型
now = datetime.datetime.now()
# 获取当前时间的年月日时分秒：int类型
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
# 获取当前的日期：date类型
now_day = datetime.date.today()

"""
2、将时间（datetime类型）转化为字符串类型： strftime
"""
# 获取当前时间的时分秒,并拼接成不同的样式
now = datetime.datetime.now()
now_time1 = now.strftime("%Y-%m-%d %H:%M:%S")
now_time2 = now.strftime("%Y年%m月%d日 %H点%M分%S秒")
# 获取当前日期，具体到日期
now_time3 = now.strftime("%Y-%m-%d 00:00:00")
# 获取当前时间，具体到小时
now_time4 = now.strftime("%Y-%m-%d %H:00:00")
# 获取当前时间，具体到分钟
now_time5 = now.strftime("%Y-%m-%d %H:%M:00")

"""
3、将字符串格式转化为时间格式： strptime
"""
my_datetime1 = datetime.datetime.strptime("2021年10月11日 14:17:32", "%Y年%m月%d日 %H:%M:%S")  # 2021-10-11 14:17:32
my_datetime2 = datetime.datetime.strptime("2021-10-11", "%Y-%m-%d")  # 2021-10-11 00:00:00

"""
4、时间推移：timedelta
"""
# 往前推移30天
before_30days = datetime.datetime.now() - datetime.timedelta(days=30)
print("往前推移30天的日期：", before_30days.strftime("%Y-%m-%d %H:%M:%S"))
# 往前推移12小时
before_12hours = datetime.datetime.now() - datetime.timedelta(hours=12)
print("往前推移12小时：", before_12hours.strftime("%Y-%m-%d %H:%M:%S"))
# 往前推移60分钟
before_60mins = datetime.datetime.now() - datetime.timedelta(minutes=60)
print("往前推移60分钟：", before_60mins.strftime("%Y-%m-%d %H:%M:%S"))
# 往后推移30天
after_30days = datetime.datetime.now() + datetime.timedelta(days=30)
print("往后推移30天的日期：", after_30days.strftime("%Y-%m-%d %H:%M:%S"))

"""
5、小案例
"""
# 1、设置一个开始时间和结束时间：从现在开始，10分钟后结束
start_datetime = datetime.datetime.now()
end_datetime = datetime.datetime.now() + datetime.timedelta(minutes=10)
print("开始时间:", start_datetime, "结束时间:", end_datetime)

# 2、设置一个开始时间和结束时间，判断此时是不是在这个时间段内
start_time = datetime.datetime.strptime("2022-5-1", "%Y-%m-%d")
end_time = datetime.datetime.strptime("2022-6-1", "%Y-%m-%d")
NOW = datetime.datetime.now()
print(start_time < NOW < end_time)

# 3、判断此时是否在某个时间段内（日期是今天）
today = str(datetime.datetime.today())

start_time = datetime.datetime.strptime(today + " 00:00:00", "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime(today + " 23:00:00", "%Y-%m-%d %H:%M:%S")
print(start_time)
print(end_time)

now_time = datetime.datetime.now()
print(start_time < now_time < end_time)
