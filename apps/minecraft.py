from talon import noise, actions, ui
from time import time
from threading import Timer

is_active = False
start = 0
noise_length = 0.2
t = None

def start_hiss_action():
  global is_active
  
  if is_active:
    actions.key('k:down')

def on_hiss(active):
  global is_active, start, noise_length, t
  
  if 'Minecraft' not in ui.active_window().title:
    return

  if 'java' != ui.active_app().name:
    return

  if active:
    is_active = True
    t = Timer(noise_length, start_hiss_action)
    t.start()
  else:
    is_active = False
    start = 0
    t.cancel()
    actions.key('k:up')

noise.register('hiss', on_hiss)