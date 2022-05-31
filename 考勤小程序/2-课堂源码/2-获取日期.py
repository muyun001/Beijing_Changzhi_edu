import time

# 获取当地时间
time_local = time.localtime()

# 获取年份
year = time_local.tm_year
# 获取月份
month = time_local.tm_mon
# 获取日子
day = time_local.tm_mday

print(f"{year}年{month}月{day}日联想未来班考勤表.xlsx")



