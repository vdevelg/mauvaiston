# https://geekbrains.ru/posts/tts_python
# https://pypi.org/project/pyttsx3/
# https://github.com/Olga-Yakovleva/RHVoice/wiki/About-%28Russian%29

import pyttsx3
engine = pyttsx3.init() # Инициализировать голосовой движок.
# У активного движка есть стандартный параметр ‘voices’, где содержится список всех доступных этому движку голосов. Это нам и нужно:
voices = engine.getProperty('voices')
# Перебрать голоса и вывести параметры каждого
"""
for voice in voices:
    print('=======')
    print('Имя: %s' % voice.name)
    print('ID: %s' % voice.id)
    print('Язык(и): %s' % voice.languages)
    print('Пол: %s' % voice.gender)
    print('Возраст: %s' % voice.age)
"""

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

engine.say("Тебя зовут Александр?")
engine.say(" ")
engine.say("Привет, тёска!")
engine.runAndWait()



# Wi-Fi
SSID = "34573457"
password = "385468"
