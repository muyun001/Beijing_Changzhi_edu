
# list 列表定义 变量名 = [元素,元素2,....]

# girls = ["迪丽热巴", "杨妮", "宋茜", "杨超越", 12, 12.5]
#
# # 取元素：变量名[索引]
# print("总类型：",type(girls))
# today_gf = girls[1]
# print(today_gf)
# print(type(girls[1])) #<class 'str'>
# print(type(girls[-1])) #<class 'float'>
# 切片：  变量名[start:end] 不包含end
# print(girls[:3]) ##['迪丽热巴', '杨妮', '宋茜']
# mm_gfs = girls[:3]
# print(mm_gfs)  # ['迪丽热巴', '杨妮', '宋茜']

# 修改
# girls = ["迪丽热巴", "杨妮", "宋茜", "杨超越", 12, 12.5]
# print(girls)
# print("girls的地址：",id(girls))
# print(girls[0])  # 迪丽热巴
# girls[0] = '古力娜扎'
# print(girls) # ['古力娜扎', '杨妮', '宋茜', '杨超越', 12, 12.5]
# print("girls修改后的地址：",id(girls))

# 添加
# girls = ['古力娜扎', '杨妮', '宋茜', '杨超越', 12, 12.5]
# print(girls)
# 贾玲  append:变量名.append(元素)
# girls.append("贾玲")
# print(girls) #['古力娜扎', '杨妮', '宋茜', '杨超越',  12, 12.5, '贾玲']
# girls.insert(0,"贾玲") # ['贾玲', '古力娜扎', '杨妮', '宋茜', '杨超越', 12, 12.5]
# print(girls)   # ['贾玲', '古力娜扎', '杨妮', '宋茜', '杨超越', 12, 12.5]
# 删除
girls = ['古力娜扎', '杨妮', '宋茜', '杨超越', '宋茜', '宋茜']
# del girls[4]
print(girls)
#girls = ['贾玲', '古力娜扎', '杨妮', '宋茜', '杨超越']
#del girls[2]
#print(girls) #['贾玲', '古力娜扎', '宋茜', '杨超越']
# 直接删除元素，通过元素直接删除 remove
girls.remove('杨超越')
print(girls)
girls.remove('宋茜')
print(girls)
# 取多个元素
# girls = ['贾玲', '古力娜扎', '杨妮', '宋茜', '杨超越']
# print(girls, ":", id(girls))
# mm_gf = girls[:2]
# print(mm_gf, ":", id(mm_gf))
# mm_gf.append("杨幂")
# print(girls)
# print(mm_gf)

# group1 = ["刘丹妮", 18, "苏园园", 15]
# group1 = [
#             ["刘丹妮", 18],
#             ["苏园园", 15],
#             12,
#             "王东丽"
#         ]
#
# group2 = [
#             ["刘丹妮", [18,"爱看书"]],  # [0][1][1]
#             ["苏园园", 15],
#             12,
#             "王东丽"
#         ]
#
# print("找出第一个元素",group1[0]) #找出第一个元素 ['刘丹妮', 18]
# print("找出第一次结果中的元素",group1[0][1]) #找出第一次结果中的元素 18
# group1[0][1] = 17
# print(group1)   # [['刘丹妮', 17], ['苏园园', 15], 12, '王东丽']
#print(group1[0])

# 判断是否存在  in
girls = ['贾玲', '古力娜扎', '杨妮', '宋茜', '杨超越']
print("贾玲" in girls) #True

group1 = [
            ["刘丹妮", 18],
            ["苏园园", 15],
            12,
            "王东丽"
        ]
print("刘丹妮" in group1) # False
print("王东丽" in group1) # True

print("刘丹妮" in group1[0]) # True