app: Baldur's Gate 3
--
settings():
  key_hold: 100

camera: mouse_drag(2)
over: mouse_release(2)

zoom out: mouse_scroll(-20, 0)
closer: mouse_scroll(20, 0)

party up: key("{")
party down: key("}")

spinner:
  key(e:down)
  sleep(0.5)
  key(e:up)
rusty:
  key(q:down)
  sleep(0.5)
  key(q:up)

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