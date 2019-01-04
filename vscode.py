from talon.voice import Context, Key

ctx = Context("VSCode", bundle="com.microsoft.VSCode")
ctx.keymap({
    'move line up': Key('alt-up'),
    'move line down': Key('alt-down'),
    'add cursors': Key('alt-shift-i'),
    'grab next': Key('cmd-d'),
    'grab all': Key('shift-cmd-l'),
    'master': Key('cmd-p'),
    'gopreev': Key('cmd-shift-['),
    'gonext': Key('cmd-shift-]'),
    'console log': 'console.log('
})