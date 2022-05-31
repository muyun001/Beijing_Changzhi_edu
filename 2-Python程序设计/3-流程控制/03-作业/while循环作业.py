

"""
9. 用while实现循环猜年龄
需求： 允许用户猜3次，若还不对，告诉他，你真笨，还想继续猜么？ 如果用户选择yes, 就让他继续，
如果选择no, 就退出。
"""
# i = 0
# age = 18
# while True:
#     i += 1
#     a = int(input('请输入年龄'))
#     if a > age:
#         print("猜大了")
#     elif a < age:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#
#     if i < 3:
#         continue
#     aa = input('你真笨，还想继续猜么？yes or no')
#     if aa == 'yes':
#         i = 0
#     else:
#         break


"""
10. 练习：
a. 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
b. 使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
c. 使用 while 循环实现输出 1-100 内的所有奇数
d. 使用 while 循环实现输出 1-100 内的所有偶数
e. 使用while循环实现输出2-3+4-5+6…+100 的和
"""

"""
11.分别使用for循环和while循环打印出如下的99乘法表

1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
1*4=4 2*4=8 3*4=12  4*4=16
1*5=5 2*5=10  3*5=15  4*5=20  5*5=25
1*6=6 2*6=12  3*6=18  4*6=24  5*6=30  6*6=36
1*7=7 2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49
1*8=8 2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64
1*9=9 2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81
"""
# for b in range(1, 9+1):
#     for a in range(1, 9+1):
#         if a <= b:
#             print(f"{a}*{b}={a*b}",end="\t")
#     print()


# for b in range(1, 9+1):
#     for a in range(1, b+1):
#         print(f"{a}*{b}={a*b}",end="    ")
#         time.sleep(0.3)
#     print()
#     time.sleep(0.3)
#
# a = 1
# b = 1
# while b <= 9:
#     a = 1
#     while a <= b:
#         print(f'{a}*{b}={a * b}', end='\t')
#         a += 1
#     print()
#     b += 1

"""
12.
已知1号是周四，这个月31天。
请写出本月的每一天是周几。
比如“1号是周四，2号是周五，3号是周六...”
"""

"""
13.
假如本月1号是周三，请输入一个日期，输出该日期是周几。
比如，输入9，输出“9号是周三”。
要求：使用while循环，每次输入一个数，就输出相对应的结果。
"""


"""
1号是周四，这个月31天，请写出几号是周几
"""
s = ["周一", "周二", "周三", "周四", "周5⃣️", "周六", "周七"]

for i in range(1, 31 + 1):
    # 因为初始的i是1，s[1]为周二，所以得到的1号是周二
    # index = i % 7
    # # 现在的要求是1号是周四，所以只需要把1号的"周二"往后移2天，使1号变成周四，即可
    # index = (i + 2) % 7
    # 现在的要求是1号是周三，所以只需要把1号的"周二"往后移1天，使1号变成周三，即可
    index = (i + 1) % 7
    print(f"{i}号是{s[index]}")

"""
假如本月1号是周三，请输入一个日期，输出该日期是周几。
"""
import re
while True:
    date = input("请输入一个日期（如：2号）：")
    # date = int(date.replace("号", ""))
    rege = re.compile("^(\d.*?)")
    date = re.match(rege, date)
    if not date:
        print("输入有误，请输入几号")
        continue
    date = int(date.group())
    if date >= 31:
        print("输入有误，请输入正确的日期")
        continue
    index = (date + 1) % 7
    print(f"{date}号是{s[index]}")
    is_continue = input("还需要继续查看吗？yes or no?")
    if is_continue == "yes" or is_continue == "y" or is_continue == "Y":
        continue
    break


