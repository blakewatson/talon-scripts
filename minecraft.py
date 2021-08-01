from talon import noise, actions, Context
from time import sleep, time
from threading import Timer

ctx = Context()
ctx.matches = r"""
app: java
title: /Minecraft/
"""

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