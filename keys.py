from talon import Module, Context

# dummy speech engine for testing
from talon.engines.dummy import DummyEngine
from talon import speech_system
#speech_system.add_engine(DummyEngine())

mod = Module()
ctx = Context()

### ALPHABET ###

# my alphabet
phonetic_alphabet = 'air bill cap drum each faint gust ham sit jury crunch little made near open pink queen red sun trap urge vest wet plex yank zoo'

# letters
letters_string = 'abcdefghijklmnopqrstuvwxyz'

# alphabet dictionary
alpha_keys = dict(zip(phonetic_alphabet.split(' '), letters_string))
keys = dict(alpha_keys)

### NUMERIC ###

numbers = 'zero one two three four five six seven eight nine'.split(' ')
numerals = '0123456789'
number_dict = dict(zip(numbers, numerals))

keys.update(number_dict)

mod.list('numeral', desc='Number keys')

ctx.lists['self.numeral'] = number_dict

@mod.capture(rule='{self.numeral}')
def numeral(m) -> str:
    'A number key'
    return str(m)

### SPECIAL CHARACTERS ###

symbol_key_words = {
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": "`",
    ",": ",",  # <== these things
    "tick": "`",
    "comma": ",",
    "clamor": ",",
    "period": ".",
    "semi": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "?": "?",
    "question": "?",
    "exclamation mark": "!",
    "exclamation point": "!",
    "bang": "!",
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
    "prime": "'",
    "L square": "[",
    "left square": "[",
    "square": "[",
    "R square": "]",
    "close square": "]",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "dash": "-",
    "bigger dash": "—",
    "middle dash": "–",
    "equals": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    "dollar": "$",
    "down score": "_",
    "under score": "_",
    "downscore": "_",
    "underscore": "_",
    "paren": "(",
    "L paren": "(",
    "left paren": "(",
    "R paren": ")",
    "close paren": ")",
    "brace": "{",
    "left brace": "{",
    "R brace": "}",
    "close brace": "}",
    "angle": "<",
    "left angle": "<",
    "less than": "<",
    "rangle": ">",
    "R angle": ">",
    "close angle": ">",
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
    "primer": '"',
    "special": "§",
    "ellipsis": "…"
}

keys.update(symbol_key_words)

### OTHER ###
other_keys = [
    "backspace",
    "delete",
    "enter",
    "escape",
    "home",
    "end",
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
        
### ARROWS ###

arrow_keys = ['up', 'down', 'left', 'right']
mod.list('modified_arrow_key', desc='Arrow keys')
ctx.lists['self.modified_arrow_key'] = dict(zip(arrow_keys, arrow_keys))

# we only allow standard arrow key directional words when modified
# for unmodified arrow keys, use the commands defined in text.talon (eg, jeep, dune, etc)
@mod.capture(rule='<self.modifier_key>+ {self.modified_arrow_key}')
def modified_arrow_key(m) -> str:
    'A modified arrow key'
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return '-'.join(mods + [m.modified_arrow_key])

### KEYS ###

mod.list('unmodified_key', desc='Unmodified keys')
ctx.lists['self.unmodified_key'] = keys

mod.list('alpha_key', desc='Alphabetic keys')
ctx.lists['self.alpha_key'] = alpha_keys

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

@mod.capture(rule='bigly {self.alpha_key}+')
def upper_alpha_key(m) -> str:
    'And uppercase alphabetic character'
    return ''.join(m[1:]).upper()


# stuff required by cursorless
##############################

mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("symbol_key", desc="All symbols from the keyboard")

@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter

@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key

@mod.capture(rule="( <self.letter> | <self.numeral> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)

ctx.lists["self.letter"] = dict(alpha_keys)
ctx.lists["self.symbol_key"] = symbol_key_words