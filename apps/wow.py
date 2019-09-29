import time
from talon.voice import Context, Key, press
from talon import ctrl, tap
from ..utils import parse_words_as_integer

ctx = Context('minecraft', func=lambda app, win: win.title.startswith('World of Warcraft'))

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None


def on_move(typ, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True


tap.register(tap.MMOVE, on_move)

def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]


def mouse_drag(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, down=True)
    ctrl.mouse_click(x, y, button=1, down=True)


def mouse_release(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, up=True)
    ctrl.mouse_click(x, y, button=1, up=True)

def jump(m):
    ctrl.key_press('space', hold=500000)

def key_down(m):
    keymap = {
        'walker': 'up',
        'backer': 'down'
    }
    ctrl.key_press(keymap[m._words[0]], down=True)

def key_up(m):
    ctrl.key_press('up', up=True)
    ctrl.key_press('down', up=True)


ctx.keymap({
    'walker': key_down,
    'backer': key_down,
    'stopper': key_up,
    # pet
    'pet attack | pit attack': Key('ctrl-1'),
    'pet follow': Key('ctrl-2'),
    'pet stay': Key('ctrl-3'),
    'pet growl': Key('ctrl-4'),
    'pet aggressive': Key('ctrl-8'),
    'pet defend': Key('ctrl-9'),
    'pet passive': Key('ctrl-0'),
    # secondary pet controls
    'heal pet | heal pit | hill pit | hill pet': Key('ctrl-a'),
    'revive pet | revive pit': Key('ctrl-b'),
    'call pet | call pit | pullpit': Key('ctrl-c'),
    'dismiss pet | dismiss pit': Key('ctrl-d'),
    # attacks
    'target': Key('shift-a'),
    'me attack': Key('shift-b'),
    'raptor': Key('shift-c'),
    'shooter': Key('shift-d'),
    'fury': Key('shift-e'),
    'mark': Key('shift-f'),
    'follow': Key('shift-g'),
    'arcane': Key('shift-h'),
    'concussive': Key('shift-i'),
    'wing clip': Key('shift-j'),
    'serpent': Key('shift-k'),
    'distracting': Key('shift-l'),
    # secondary controls
    'trade beasts': Key('shift-m'),
    'trade humanoids': Key('shift-n'),
    'aspect of the hawk': Key('shift-r'),
    'aspect of the monkey': Key('shift-x')
})

""" 'attack (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': hold_key,
'eat (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': hold_key,
'jumper': jump,
'place [(1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)]': place,
'tower (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': climb,
'hitter': start_attack,
'stop': stop_attack,
'dismount': Key('shift'),
'sniper': draw_bow,
'fire bow': fire_bow,
'where am i': Key('f3') """