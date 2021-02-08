from talon.voice import Context, press, Key
from talon import ctrl
import string
from ..utils import normalise_keys, insert

alpha_alt = "air bill cap drum each faint gust ham sit jury crunch little made near orange pink queen red sun trap urge vest wet plex yank zoo".split()
alphabet = dict(zip(alpha_alt, string.ascii_lowercase))

f_keys = {f"F {i}": f"f{i}" for i in range(1, 13)}

simple_keys = normalise_keys(
    {
        "lloyd": "left",
        "chris": "right",
        "jeep": "up",
        "( dune | doom )": "down",
        "( backspace | junk )": "backspace",
        "(delete | forward delete)": "delete",
        "(space | skoosh | next)": "space",
        "(tab)": "tab",
        "( enter | shock )": "enter",
        "( escape )": "escape",
        "home": "home",
        "pagedown": "pagedown",
        "pageup": "pageup",
        "end": "end",
    }
)

symbols = normalise_keys(
    {
        # NOTE:  This should only contain symbols that do not require any modifier
        # keys to press on a standard US keyboard layout. Commands for keys that do
        # require modifiers (e.g. ``"caret": "^"`) should belong in
        # ``text/symbol.py``.
        "(tick | back tick)": "`",
        "(comma | ,)": ",",
        "(dot | period)": ".",
        "(semicolon | semi)": ";",
        "(quote | quatchet)": "'",
        "(square | L square | left square | left square bracket)": "[",
        "(R square | right square | right square bracket)": "]",
        "(slash | forward slash)": "/",
        "backslash": "\\",
        "(minus | dash)": "-",
        "(equals | smaqual)": "=",
    }
)

modifiers = normalise_keys(
    {
        "command": "cmd",
        "(control | troll)": "ctrl",
        "(shift | sky)": "shift",
        "(alt | option)": "alt",
    }
)

keys = {}
keys.update(f_keys)
keys.update(simple_keys)
keys.update(symbols)

digits = {str(i): str(i) for i in range(10)}

# separate arrow dictionary for combining with modifiers
arrows = {"left": "left", "right": "right", "up": "up", "down": "down"}

# map alnum and keys separately so engine gives priority to letter/number repeats
keymap = keys.copy()
keymap.update(alphabet)
keymap.update(digits)
keymap.update(arrows)


def get_modifiers(m):
    try:
        return [modifiers[mod] for mod in m["basic_keys.modifiers"]]
    except KeyError:
        return []


def get_keys(m):
    groups = [
        "basic_keys.keys",
        "basic_keys.arrows",
        "basic_keys.digits",
        "basic_keys.alphabet",
        "basic_keys.keymap",
    ]
    for group in groups:
        try:
            return [keymap[k] for k in m[group]]
        except KeyError:
            pass
    return []


def uppercase_letters(m):
    insert("".join(get_keys(m)).upper())


def press_keys(m):
    mods = get_modifiers(m)
    keys = get_keys(m)

    if mods == ["shift"] and all(key in alphabet.values() for key in keys):
        return uppercase_letters(m)

    if mods:
        press("-".join(mods + [keys[0]]), hold=32000)
        keys = keys[1:]
    for k in keys:
        press(k, hold=32000)


ctx = Context("basic_keys")
ctx.keymap(
    {
        "(uppercase | ship | sky) {basic_keys.alphabet}+ [(lowercase | sunk)]": uppercase_letters,
        "{basic_keys.modifiers}* {basic_keys.alphabet}+": press_keys,
        "{basic_keys.modifiers}* {basic_keys.digits}+": press_keys,
        "{basic_keys.modifiers}* {basic_keys.keys}+": press_keys,
        "(go | {basic_keys.modifiers}+) {basic_keys.arrows}+": press_keys,
        "number {basic_keys.digits}+ [over]": press_keys
    }
)
ctx.set_list("alphabet", alphabet.keys())
ctx.set_list("digits", digits.keys())
ctx.set_list("keys", keys.keys())
ctx.set_list("arrows", arrows.keys())
ctx.set_list("modifiers", modifiers.keys())
ctx.set_list("keymap", keymap.keys())
