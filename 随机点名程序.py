import random


def random_choice():
    # input("欢迎来到随机点名小程序。请按任意键开始！")
    s = ["崔昊元", "贾靖程", "吴俊岳", "王浩羽", "吕梦丽", "牛皓冬", "张阔", "孙佳奇", "郑佳睦", "王孝天", "付一鸣", "李蓉轩", "陈观绅",
         "赵鑫博", "张子豪", "叶平"]

    # while True:
    #     print('--------------')
    #     print(random.choice(s))
    #     print('--------------')
    # if input("q结束，其他键回车继续") == "q":
    #     break

    print('--------------')
    print(random.choice(s))
    print('--------------')


if __name__ == '__main__':
    random_choice()
