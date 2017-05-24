import time

from pykeyboard import PyKeyboard
from pymouse import PyMouse

k = PyKeyboard()
m = PyMouse()
cmds = [
    'up',
    'down',
    'left',
    'right',
    'a',
    'b',
    'start',
    'select',
]

def presskey(key):
    k.press_key(key)
    time.sleep(0.15)
    k.release_key(key)

def run(nick, text):
    x, y = m.screen_size()
    m.click(x//2, y//2, 1)
    if text in cmds:
        print(nick, text)
        if text == 'up':
            presskey(k.up_key)
        elif text == 'down':
            presskey(k.down_key)
        elif text == 'left':
            presskey(k.left_key)
        elif text == 'right':
            presskey(k.right_key)
        elif text == 'a':
            presskey(text)
        elif text == 'b':
            presskey(text)
        elif text == 'start':
            presskey(k.return_key)
        elif text == 'select':
            presskey(k.shift_key)
    else:
        pass
