from talon import Module, Context

# dummy speech engine for testing
from talon.engines.dummy import DummyEngine
from talon import speech_system
#speech_system.add_engine(DummyEngine())

mod = Module()
ctx = Context()

### ALPHABET ###

# my alphabet
phonetic_alphabet = 'air bill cap drum each faint gust ham sit jury crunch little made near orange pink queen red sun trap urge vest wet plex yank zoo'

# letters
letters_string = 'abcdefghijklmnopqrstuvwxyz'

# alphabet dictionary
keys = dict(zip(phonetic_alphabet.split(' '), letters_string))

### NUMERIC ###

numbers = 'zero one two three four five six seven eight nine'.split(' ')
numerals = '0123456789'

keys.update(dict(zip(numbers, numerals)))

### ARROWS ###

keys.update({
    'up': 'up',
    'down': 'down',
    'left': 'left',
    'right': 'right'
})

### SPECIAL CHARACTERS ###

keys.update({
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": "`",
    ",": ",",  # <== these things
    "back tick": "`",
    "comma": ",",
    "period": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "exclamation point": "!",
    "dollar sign": "$",
    "asterisk": "*",
    "hash sign": "#",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",
    "dot": ".",
    "quote": "'",
    "L square": "[",
    "left square": "[",
    "square": "[",
    "R square": "]",
    "right square": "]",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    "dollar": "$",
    "down score": "_",
    "under score": "_",
    "paren": "(",
    "L paren": "(",
    "left paren": "(",
    "R paren": ")",
    "right paren": ")",
    "brace": "{",
    "left brace": "{",
    "R brace": "}",
    "right brace": "}",
    "angle": "<",
    "left angle": "<",
    "less than": "<",
    "rangle": ">",
    "R angle": ">",
    "right angle": ">",
    "greater than": ">",
    "star": "*",
    "pound": "#",
    "hash": "#",
    "percent": "%",
    "caret": "^",
    "amper": "&",
    "pipe": "|",
    "dubquote": '"',
    "double quote": '"',
})

### ALTERNATES ###

keys.update({
    "junk": "backspace",
    "next": "space"
})

### OTHER ###
other_keys = [
    "backspace",
    "delete",
    "end",
    "enter",
    "escape",
    "home",
    "insert",
    "pagedown",
    "pageup",
    "space",
    "tab",
]

keys.update({ k: k for k in other_keys})

### MODIFIERS ###

mod.list('modifier_key', desc='Modifier keys')

ctx.lists['self.modifier_key'] = {
    'command': 'cmd',
    'option': 'alt',
    'control': 'ctrl',
    'shift': 'shift'
}

@mod.capture(rule='{self.modifier_key}')
def modifier_key(m) -> str:
    'A modifier key.'
    return str(m)


### KEYS ###

mod.list('unmodified_key', desc='Unmodified keys')

ctx.lists['self.unmodified_key'] = keys

@mod.capture(rule='{self.unmodified_key}')
def unmodified_key(m) -> str:
    'A single unmodified key'
    return str(m)

@mod.capture(rule='<self.modifier_key>* <self.unmodified_key>')
def key(m) -> str:
    'A single key with optional modifiers'
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return '-'.join(mods + [m.unmodified_key])
