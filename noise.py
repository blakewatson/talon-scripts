from talon import ctrl, noise
from time import sleep, time

start = 0
noise_length = 0.2

def mouse_click_on_hiss(is_active):
  global start
  print(is_active)
  if is_active:
    start = time()
  elif time() - start > noise_length:
    ctrl.mouse_click()
    
#noise.register('hiss', mouse_click_on_hiss)