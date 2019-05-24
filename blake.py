from talon.voice import Context, Key, press
from .utils import parse_words, join_words, insert, parse_words_as_integer

ctx = Context('blake')

def git_commit(m):
    message = join_words(parse_words(m)).lower()
    text = 'git commit -m "%s"' % message
    insert(text)

def multi_arrow(m):
    times = parse_words_as_integer(m._words[1:])
    if times > 0 and times < 10:
        for t in range(times):
            press(m._words[0])

def word_travel(m):
    times = parse_words_as_integer(m._words[2:])
    direction = m._words[1]
    repeat_press(times, 'alt-'+direction)

def grab_lines(m):
    times = parse_words_as_integer(m._words[2:])
    direction = m._words[1]
    repeat_press(times, 'shift-'+direction)
    press('cmd-shift-right')
    

def repeat_press(times, command, limit = 10):
    if times > 0 and times < limit:
        for t in range(times):
            press(command)

ctx.keymap({
    # working with text
    'word left': Key('alt-left'),
    'word right': Key('alt-right'),
    'words (left | right) (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': word_travel,
    'grab left': Key('alt-shift-left'),
    'grab right': Key('alt-shift-right'),
    'cover (up | down) (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': grab_lines,
    'killer': [Key('backspace')] * 2,
    'copy': Key('cmd-c'),
    'paste': Key('cmd-v'),
    'cut': Key('cmd-x'),
    'big dash': '–',
    'bigger dash': '—',
    'start paragraph': [Key('enter')] * 2,
    'clap': Key('cmd-right'),
    'klapper | clapper': Key('cmd-left'),
    'emoticon': Key('ctrl-cmd-space'),

    # used for textexpander
    'special': '§',

    # navigation
    'flask': Key('cmd-tab'),
    'alley': Key('alt-space'),
    'clipper': Key('alt-cmd-c'),

    # browsers
    'refresh': Key('cmd-shift-r'),

    # global
    'file save': Key('cmd-s'),
    'undo': Key('cmd-z'),
    'search': Key('cmd-f'),
    'mission': Key('ctrl-up'),
    'left (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': multi_arrow,
    'up (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': multi_arrow,
    'right (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': multi_arrow,
    'down (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': multi_arrow,

    # code
    # 'state far': 'var ',
    # 'op arrow': ' => ',
    'indent': Key('cmd-]'),
    'outdent': Key('cmd-['),
    'terminate': [Key('cmd-right'), ';'],
    'terminate comma': [Key('cmd-right'), ','],
    'terminate colon': [Key('cmd-right'), ':'],
    'terminate prop': [Key('cmd-right'), ': '],
    'plug-in': 'plugin',
    'in-line': 'inline',
    'panhandle': ['<?php  ?>'] + ([Key('left')] * 3),
    'echolocation': ['<?=  ?>'] + ([Key('left')] * 3),
    'purana | piranha': ['(  )'] + ([Key('left')] * 2),
    'spacer': ['  '] + [Key('left')],

    # termmnal
    'pseudo': 'sudo ',
    'get pull': 'git pull',
    'get push': 'git push',
    'get status': 'git status',
    'get add': 'git add ',
    'get add all': 'git add *',
    'get commit <dgndictation>': git_commit,
    'CD': 'cd ',
    'lister': 'ls',
    'list la': 'ls -la',

    # troublesome words
    'e-mail | e mail': 'email'
})