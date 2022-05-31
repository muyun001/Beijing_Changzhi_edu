import pyttsx3

# 微软语音包
# 官网：https://pypi.org/project/pyttsx3/


engine = pyttsx3.init()

# 设置语速
engine.setProperty('rate', 150)
engine.say("牛皓冬迟到了")
engine.runAndWait()

# 设置语速
# 数值越大，速度越快
# engine = pyttsx3.init()
# rate = engine.getProperty('rate')  # 获取默认的语速
# print(rate)
# engine.setProperty('rate', 170)
# engine.say("盼望着，盼望着，东风来了，春天的脚步近了...")
# engine.runAndWait()
# engine.stop()


# 变换声音
# rate = engine.getProperty('rate')  # 获取默认的语速
# print(rate)
#
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  # 设置为男声
# # engine.setProperty('voice', voices[1].id)  # 设置为女声
# engine.say("Hello World!")
# engine.runAndWait()
# engine.stop()

# 保存音频
# engine.save_to_file('牛皓冬迟到了', '../files/test.mp3')
# engine.runAndWait()
# engine.stop()
