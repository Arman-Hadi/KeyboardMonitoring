from pynput.keyboard import Listener, Key, Controller
import json
from datetime import datetime as dt

dirpath = f'E:/!Programming/django/Keyboard/KEYDATA/{dt.now().year}-{dt.now().month}-{dt.now().day}.json'
try:
    keysave = open(dirpath, 'r')
    key_save = json.loads(keysave.read())
except FileNotFoundError:
    keysave = open(dirpath, 'w')
    keysave.write("{}")
    key_save = json.loads("{}")

keysave.close()
keyboard = Controller()

def savekey(key):
    if key in key_save:
        key_save[key] += 1
    else:
        key_save[key] = 1

def changekey(key):
    if key==Key.f12:
        keyboard.press('=')
        key_save.pop(str(Key.f12))
    elif key==Key.f7:
        keyboard.press('-')
        key_save.pop(str(Key.f7))
    elif key==Key.f10:
        keyboard.press(Key.delete)
        key_save.pop(str(Key.f10))

def onpress(key):
    savekey(str(key))
    changekey(key)
    savejson()

def savejson():
    keysave = open(dirpath, 'w')
    jsonfile = json.dumps(key_save)
    keysave.write(jsonfile)
    keysave.close()
    print('saved')


with Listener(on_press=onpress) as lis:
    lis.join()
