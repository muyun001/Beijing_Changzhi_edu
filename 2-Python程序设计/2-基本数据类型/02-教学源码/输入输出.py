
# name = input("请输入姓名:")
# print("刚才输入的内容是:",name)
# print("刚才输入的内容类型:",type(name))  # 输入的内容类型 都是字符串
# print("结束")
# #使用input输入正方形的边长，分别输出正方形的周长和面积
# 第一步，使用input让用户输入
# 第二步 ，使用变量接收输入的内容
# 第三步，计算 正方形的周长： 边长*4  面积：边长*边长
# 第四步:  输出结果
# bc = input("请输入正方形的边长>>>")
# print("正方形的周长", bc * 4, ";正方形的面积:", bc * bc)
# TypeError: can't multiply sequence by non-int of type 'str'

# bc = int(input("请输入正方形的边长>>>"))
# print("正方形的周长", bc * 4, ";正方形的面积:", bc * bc)

# 格式化输出
# girls = ['贾玲', '古力娜扎', '杨妮', '宋茜', '杨超越',"Lisa"]
# # 返回变量的长度  len(变量名)
# print("len返回长度：", len(girls))
# # 武老师认识5个明星,其中就有迪丽热巴
# content = "武老师认识"+ str(len(girls))+ "个明星,其中就有迪丽热巴"
# content_1 = "武老师认识%s个明星,其中就有迪丽热巴" % len(girls)
#
# content_2 = "武老师认识%s个明星,其中就有%s" % (len(girls),"迪丽热巴")
#
# print(content_2)
# mon = 1123.111111
# content_3 = "我钱包里有%.2f元"%mon
# print(content_3)

"""
现有一练习需求，问用户的姓名、年龄、工作、爱好 ，
然后打印成以下格式
"""

name = input("请输入姓名>>>")
age = input("请输入年龄>>>")
job = input("请输入职业>>>")
hobby = input("请输入爱好>>>")
# print("------------ info of tom -----------")
# print("Name:%s" % name)
# print("Age:%s" % age)
# print("Job:%s" % job)
# print("Hobby:%s" % hobby)
# print("------------ end -----------")
content = """
------------ info of tom -----------
Name  : %s
Age   : %s
job   : %s
Hobbie: %s
------------- end -----------------
"""%(name, age,job,hobby)
print(content)
