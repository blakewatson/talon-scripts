from talon.voice import Context, Key, press
from ..utils import parse_words_as_integer

def jump_tab(m):
    tab_number = parse_words_as_integer(m._words[1:])
    if tab_number != None and tab_number > 0 and tab_number < 10:
        press("ctrl-%s" % tab_number)

ctx = Context("VSCode", bundle="com.microsoft.VSCode")
ctx.keymap({
    '(lineup | line up)': Key('alt-up'),
    'line down': Key('alt-down'),
    'expand': Key('ctrl-e'),
    'add cursors': Key('alt-shift-i'),
    'grab next': Key('cmd-d'),
    'grab all': Key('shift-cmd-l'),
    'pallet': Key('shift-cmd-p'),
    'phylum': Key('cmd-p'),
    'gopreev': Key('cmd-shift-['),
    'gonext': Key('cmd-shift-]'),
    'go tab (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': jump_tab,
    'console log': 'console.log('
})