app: Divinity - Original Sin 2
--
settings():
  key_hold: 100

zoom out: mouse_scroll(-20, 0)
closer: mouse_scroll(20, 0)

# cycle party members
party last: key("[")
party next: key("]")

# select continuous
selection:
  key(ctrl:down)
  sleep(0.1)
  mouse_click()
  sleep(0.1)
  key(ctrl:up)

# select continuous
sequence:
  key(shift:down)
  sleep(0.1)
  mouse_click()
  sleep(0.1)
  key(shift:up)

# camera ##########

# rotate with mouse
camera: mouse_drag(2)
shudder | shutter: mouse_release(2)

# rotate left and right
spinner:
  key(end:down)
  sleep(0.5)
  key(end:up)
rusty:
  key(delete:down)
  sleep(0.5)
  key(delete:up)

# up down left right
ahead:
  key(w:down)
  sleep(0.5)
  key(w:up)
behind:
  key(s:down)
  sleep(0.5)
  key(s:up)
leader:
  key(a:down)
  sleep(0.5)
  key(a:up)
riddle:
  key(d:down)
  sleep(0.5)
  key(d:up)