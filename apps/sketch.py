from talon.voice import Context, Key, Str, press
from talon import ctrl

ctx = Context("sketch", bundle="com.bohemiancoding.sketch3")

def start_pan(m):
    ctrl.key_press('space', down=True)

def stop_pan(m):
    ctrl.key_press('space', up=True)

ctx.keymap({
  'group': Key('cmd-g'),
  'ungroup': Key('shift-cmd-g'),
  'locker': Key('shift-cmd-l'),
  'panning': start_pan,
  'punt': stop_pan
})