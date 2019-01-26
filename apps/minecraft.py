import time
from talon.voice import Context, Key, press
from talon import ctrl
from ..utils import parse_words_as_integer

ctx = Context("minecraft")

def hold_key(m):
    keymap = {
        'attack': 'k'
    }
    half_seconds = parse_words_as_integer(m._words[1:])
    if half_seconds != None and half_seconds > 0 and half_seconds < 9:
        microseconds = half_seconds * 500000
        key_to_press = keymap[m._words[0]]
        ctrl.key_press(key_to_press, hold=microseconds)

def jump(m):
    ctrl.key_press('space', hold=1000000)

""" ctx.keymap({
    'attack (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': hold_key,
    'jumper': jump,
    'place': 'u'
}) """