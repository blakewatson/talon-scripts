import time
from talon.voice import Context, Key, press
from talon import ctrl
from ..utils import parse_words_as_integer

ctx = Context("minecraft")

def place(m):
    times = 1
    if len(m._words) > 1:
        times = parse_words_as_integer(m._words[1:])
    for t in range(times):
        ctrl.key_press('u')
        time.sleep(0.25)

def hold_key(m):
    keymap = {
        'attack': 'k',
        'eat': 'u'
    }
    half_seconds = parse_words_as_integer(m._words[1:])
    if half_seconds != None and half_seconds > 0 and half_seconds < 10:
        microseconds = half_seconds * 500000
        key_to_press = keymap[m._words[0]]
        ctrl.key_press(key_to_press, hold=microseconds)

def jump(m):
    ctrl.key_press('space', hold=500000)

def climb(m):
    repeat = 1
    if len(m._words) > 1:
        repeat = parse_words_as_integer(m._words[1:])
    for r in range(repeat):
        ctrl.key_press('space', down=True)
        time.sleep(0.25)
        ctrl.key_press('u')
        ctrl.key_press('space', up=True)
        time.sleep(0.25)

def start_attack(m):
    ctrl.key_press('k', down=True)

def stop_attack(m):
    ctrl.key_press('k', up=True)

ctx.keymap({
    'attack (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': hold_key,
    'eat (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': hold_key,
    'jumper': jump,
    'place [(1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)]': place,
    'tower (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': climb,
    'hitter': start_attack,
    'stop': stop_attack,
    'dismount': Key('shift')
})