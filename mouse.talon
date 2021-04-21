click: mouse_click()
double click | dubclick:
  mouse_click()
  sleep(0.1)
  mouse_click()

# right click
escort: mouse_click(1)

# click with modifiers
<user.modifier_key> click:
  key("{modifier_key}:down")
  mouse_click()
  key("{modifier_key}:up")

# scrolling
wheeler: mouse_scroll(-300, 0)
dealer: mouse_scroll(300, 0)