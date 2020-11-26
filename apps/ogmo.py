from talon.voice import Context, Key, Str, press
from talon import ctrl

ctx = Context("ogmo", func=lambda app, win: win.title.endswith('Ogmo Editor'))

def start_pan(m):
    ctrl.key_press('space', down=True)

def stop_pan(m):
    ctrl.key_press('space', up=True)

ctx.keymap({
  'panning': start_pan,
  'punt': stop_pan
})