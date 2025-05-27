app: Baldur's Gate 3
--
settings():
  key_hold: 100

zoom out: mouse_scroll(-20, 0)
closer: mouse_scroll(20, 0)

# psycho party members
party up: key("{")
party down: key("}")

# menu
choices:
  key(':down)
  sleep(0.25)
  key(':up)

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
  key(e:down)
  sleep(0.5)
  key(e:up)
rusty:
  key(q:down)
  sleep(0.5)
  key(q:up)

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