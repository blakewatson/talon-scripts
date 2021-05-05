touch: mouse_click()
double touch | dubtouch:
  mouse_click()
  sleep(0.1)
  mouse_click()

# right click
escort: mouse_click(1)

# middle button click
middle click | midi: mouse_click(2)

# click with modifiers
<user.modifier_key> click:
  key("{modifier_key}:down")
  mouse_click()
  key("{modifier_key}:up")

# scrolling
wheeler: mouse_scroll(-300, 0)
dealer: mouse_scroll(300, 0)