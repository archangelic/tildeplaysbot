from datetime import datetime
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
    'save',
    'reload',
]

# clear the screen
print('\n' * 100)

# poverty logger
def tp_logger(nick, text):
    stamp = datetime.now().strftime('[%m.%d.%y %H:%M:%S] ')
    print('<' + nick + '> ', text)
    with open('log_tildeplays.log', 'a') as f:
        f.write(stamp + '<' + nick + '> ' + text + '\n')


def presskey(key):
    k.press_key(key)
    time.sleep(0.15)
    k.release_key(key)


def run(nick, text):
    x, y = m.screen_size()
    m.click(x // 2, y // 2, 1)
    if text.startswith('tildeplaysbot:'):
        text = ''.join([i + ' ' for i in text.split(' ')[1:]]).strip()
        tp_logger(nick, text)
    if text.startswith('!ff'):
        tp_logger(nick, text)
    if text in cmds:
        tp_logger(nick, text)
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
        elif text == 'save':
            presskey(k.function_keys[5])
        elif text == 'reload':
            presskey(k.function_keys[7])
    else:
        pass
