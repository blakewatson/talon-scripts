from talon.voice import Context, Key

ctx = Context('blake')
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

    # code
    'state far': 'var ',
    'op arrow': ' => ',
    'indent': Key('cmd-]'),
    'outdent': Key('cmd-['),
    'terminate': [Key('cmd-right'), ';'],
    'terminate comma': [Key('cmd-right'), ',']
})