lst = [4, 4, 4, 4, 4]
# lst = [4, 4, 4, 1, 1, 1, 1, 1, 1]
# lst = [4, 4, 4, 1, 1, 3, 1, 7, 1]
# 首先确认大小2个参照值
# 1.假设第一和第二值的初始值都是第一个元素
max_value = lst[0]
second_max = lst[0]
# 2.通过循环确定1个和初始值不相同的值,。
for item in lst:  # 循环找到一个比初始值大或者小的值
    if item > max_value:
        max_value = item  # 元素比最大值大，最大值为当前元素
        break  # 找到后跳出循环
    elif item < max_value:  # 元素比最大值小，第二值为当前元素
        second_max = item
        break  # 找到后跳出循环
if max_value == second_max:  # 比较第一和第二值是否相同，
    print("列表中所有值都相同，无第二大值")
else:
    for item in lst:  # 不相同 进行循环确认最大值和最小值
        if item <= second_max:  # 小于等于第二值,就没有必要继续比较了
            continue
        if item > max_value:  # 如果当前值大于第一值，第二值变成第一，第一变为当前值
            second_max = max_value
            max_value = item
        elif item > second_max and item != max_value:  # 如果当前值大于第二值并且不等于第一值，则改变第二值
            second_max = item
    print("最大值为:%s,最小值为：%s"(max_value, second_max))
