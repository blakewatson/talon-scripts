beets: mouse_click()
double beets | beetle:
  mouse_click()
  sleep(0.1)
  mouse_click()

# right click
escort: mouse_click(1)

# middle button click
middleton | midi: mouse_click(2)

# click with modifiers
<user.modifier_key> beets:
  key("{modifier_key}:down")
  mouse_click()
  key("{modifier_key}:up")

# dragging the mouse
dragon: mouse_drag(0)
release: mouse_release(0)
double dragon:
  mouse_click(0)
  mouse_drag(0)

# scrolling
wheeler: mouse_scroll(-300, 0)
dealer: mouse_scroll(300, 0)