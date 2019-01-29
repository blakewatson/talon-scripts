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

ctx.keymap({
    # working with text
    'word left': Key('alt-left'),
    'word right': Key('alt-right'),
    'grab left': Key('alt-shift-left'),
    'grab right': Key('alt-shift-right'),
    'killer': [Key('backspace')] * 2,
    'copy': Key('cmd-c'),
    'paste': Key('cmd-v'),
    'cut': Key('cmd-x'),
    'big dash': '–',
    'bigger dash': '—',
    'start paragraph': [Key('enter')] * 2,

    # used for textexpander
    'special': '§',

    # navigation
    'last window': Key('cmd-tab'),
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
    'state far': 'var ',
    'op arrow': ' => ',
    'indent': Key('cmd-]'),
    'outdent': Key('cmd-['),
    'terminate': [Key('cmd-right'), ';'],
    'terminate comma': [Key('cmd-right'), ','],

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
    'list la': 'ls -la'
})