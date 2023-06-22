# Alex 2.0

import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from text_to_num import text2num
import webbrowser
import random

print(f"{config.VA_NAME} ({config.VA_VER}) начал свою работу...")
tts.va_speak("Слушаю, хозя!")

def va_respond(voice: str):
    print(voice)
    
    if voice.startswith(config.VA_ALIAS):
        cmd = recognize_cmd(filter_cmd(voice))
        
        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])
            

def filter_cmd(raw_voice: str):
    cmd = raw_voice
    
    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, '').strip()
        
    for x in config.VA_TBR:
        cmd = cmd.replace(x, '').strip()
        
    return cmd

def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():
    
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
            
    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        text = "Я умею: ..."
        text += "проговаривать время ..."
        text += "открывать браузер ..."
        text += "и рассказывать анекдоты"
        tts.va_speak(text)
        
    elif cmd == 'ctime':
        now = datetime.datetime.now()
        text = "Сейч+ас " + text2num(now.hour) + ' ' + text2num(now.minute)
        tts.va_speak(text)
    
    elif cmd == 'joke':
        jokes = ['Как смеются програмисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. м+ожно присоединится',
                 'Програмист это машина для преобразования кафе в кофе, а кофе в код']
        
        tts.va_speak(random.choice(jokes))
    
    elif cmd == 'open_browser':
        chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome).open("chrome://newtab")
    
    
stt.va_listen(va_respond)
