import time
from dateutil.parser import parse
import datetime

"""
获取当前时间
"""
# # 之前讲过的方式
# # 获取当地时间
# time_local = time.localtime()
# # 获取年份
# year = time_local.tm_year
# # 获取月份
# month = time_local.tm_mon
# # 获取日子
# day = time_local.tm_mday

# 另一种方式
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

today = str(datetime.date.today())
print(today)

# 判断此时是否在某个时间段内
start_time = datetime.datetime.strptime(today + " 00:00:00", "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime(today + " 23:00:00", "%Y-%m-%d %H:%M:%S")
print(start_time)
print(end_time)
now_time = datetime.datetime.now()
print(start_time < now_time < end_time)


