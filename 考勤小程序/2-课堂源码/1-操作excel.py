import pandas as pd

# 从excel读取数据
data = pd.read_excel("../files/5楼学生名单.xlsx")  # DataFrame数据类型-二维
students = data['名单']
# print(students)

# 添加数据
# data["考勤"] = ["考勤正常", "考勤异常", "考勤异常"]
# data["说明"] = ["", "参加活动", "请假"]

# kaoqin = []  # 考勤
# shuoming = []  # 说明
# for name in students:
#     print(name)
#     num = input("是否考勤正常？1-请假，2-参加活动，3-旷课，4-迟到， 考勤正常请直接回车。")
#     if num == "":
#         kaoqin.append("考勤正常")
#         shuoming.append("")
#     else:
#         kaoqin.append("考勤异常")
#         if num == "1":
#             shuoming.append("请假")
#         elif num == "2":
#             shuoming.append("参加活动")
#         elif num == "3":
#             shuoming.append("旷课")
#         elif num == "4":
#             shuoming.append("迟到")
#         else:
#             print("您的输入有误！")
#
# data["考勤"] = kaoqin
# data["说明"] = shuoming
#
# # 将数据保存到excel, index=False是去掉第一列的索引
# data.to_excel("联想未来班考勤表测试版-4.xlsx", index=False)


# 添加数据


# 考勤
kaoqin = []
# 说明
shuoming = []

for name in students:
    print(name)
    input_num = input("1-请假，2-参加活动，3-迟到，4-旷课，考勤正常请直接回车。")
    print(input_num)

    # 判断是否为空
    # if input_num == "":
    if not input_num:
        # 考勤正常
        kaoqin.append("考勤正常")
        shuoming.append("")
    else:
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

data["考勤"] = kaoqin
data["说明"] = shuoming
# # # 将数据保存到excel, index=False是去掉第一列的索引
data.to_excel("联想未来班考勤表测试版-5.xlsx", index=False)
