app.name: Google Chrome
app.name: Firefox
app.name: Firefox Developer Edition
-
back: browser.go_back()
go forward: browser.go_forward()
URL | locator: browser.focus_address()
developer tools: browser.toggle_dev_tools()
tabby:
  key(cmd-shift:down)
  mouse_click()
  key(cmd-shift:up)
reload: browser.reload()
hard reload: browser.reload_hard()
action(browser.reload): key(cmd-r)
action(browser.reload_hard): key(cmd-shift-r)