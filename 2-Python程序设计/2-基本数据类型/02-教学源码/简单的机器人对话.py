#通过 find for循环 做出一个简单的聊天机器人, 用户通过各种方式询问名字及在哪,回答这是我的名字叫小米,或我在北京市昌平职业高中
import pyttsx3
engine = pyttsx3.init()
list1=['名字','name','谁','你叫']
list2 = ['where','哪','地方']


while True:
    a = True
    user = input('主人,有什么可以帮您的?')
    for i in list1:
        if user.find(i)>=0:
            print('我的名字叫小米')
            engine.say('我的名字叫小米')
            engine.runAndWait()
            a=False
            break
    for i in list2:
        if user.find(i) >= 0:
            print('我在北京昌平职业高中')
            engine.say('我在北京昌平职业高中')
            engine.runAndWait()
            a = False
            break
    if a:
        print('听不明白你说什么')