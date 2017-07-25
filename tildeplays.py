from datetime import datetime
from os import environ, path
from textwrap import wrap
import time
import subprocess

from pykeyboard import PyKeyboard

k = PyKeyboard()
cmds = {'up': k.up_key,
        'down': k.down_key,
        'left': k.left_key,
        'right': k.right_key,
        'a': 'a',
        'b': 'b',
        'start': k.return_key,
        'select': k.shift_key,
        'save': k.function_keys[5],
        'reload': k.function_keys[7]}

# clear the screen
print('\n' * 100)

# poverty logger
def tp_logger(nick, text):
    stamp = datetime.now().strftime('[%m.%d.%y %H:%M:%S] ')
    print('<' + nick + '> ', text)
    with open('log_tildeplays.log', 'a') as f:
        f.write(stamp + '<' + nick + '> ' + text + '\n')
    line = '<' + nick + '>  ' + text
    output = wrap(line, width=25)
    with open('log.txt', 'a') as chat:
        for i in output:
            chat.write(i + '\n')


def presskey(key):
    k.press_key(key)
    time.sleep(0.15)
    k.release_key(key)


def run(nick, text):
    subprocess.call('xdotool search --name "FCEUX 2.2.2" windowactivate', shell=True)
    if text.startswith(('tildeplaysbot:', '!ff')):
        text = ''.join([i + ' ' for i in text.split(' ')[1:]]).strip()
        tp_logger(nick, text)
    if text == 'power':
        game = path.join(environ['HOME'], 'Final Fantasy (USA).nes')
        subprocess.call('fceux "{}" &'.format(game), shell=True)
        subprocess.call('obs --startstreaming &', shell=True)
    if text in cmds:
        tp_logger(nick, text)
        presskey(cmds[text])
    else:
        pass
