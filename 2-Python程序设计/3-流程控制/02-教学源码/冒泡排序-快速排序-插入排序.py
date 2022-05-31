"""
冒泡排序
"""
# 交换位置
my_list = [3, 44, 50, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 48]

for i in range(len(my_list)):
    for j in range(len(my_list)-1-i):
        if my_list[j] > my_list[j+1]:   # ------ j:0  j+1  1
            # # 保存第一个元素的值
            # temp = my_list[j]
            # # 第一个元素 = 第二个元素
            # my_list[j] = my_list[j + 1]
            # # 第二个元素 = 保存的数据
            # my_list[j + 1] = temp

            my_list[j], my_list[j + 1] = my_list[j+1], my_list[j]
print(my_list)



# 冒泡排序排序
# my_list = [2, 5, 9, 1, 12, 3]
# for i in range(len(my_list)):
#     for j in range(0, len(my_list)-1-i):
#         if my_list[j] > my_list[j+1]:
#             my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
# print(my_list)

# 插入排序
# my_list = [2, 5, 9, 1, 3, 12]
# for i in range(1, len(my_list)):
#     if my_list[i-1] < my_list[i]:
#         continue
#     else:
#         tmp = my_list[i]
#         tmp_index = i
#         while tmp_index >0 and my_list[tmp_index -1] > tmp:
#             my_list[tmp_index] =my_list[tmp_index-1]
#             tmp_index -= 1
#         my_list[tmp_index] = tmp
# print(my_list)


# 选择排序：
# my_list = [2, 5, 9, 1, 3, 12]
# for i in range(len(my_list)):
#     min = i
#     for j in range(min, len(my_list)):
#         # 寻找min到len(my_list) - 1 这个范围内的最小数
#         if my_list[min] > my_list[j]:
#             min = j
#         my_list[i], my_list[min] = my_list[min], my_list[i]
# print(my_list)
#
# lst = [1, 5, 6, 2, 4]
#
# for i in range(len(lst)-1, -1, -1):
#     print(lst[i])
