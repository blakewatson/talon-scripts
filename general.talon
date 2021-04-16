### global ###
alley: key(alt-space)
cut: key(cmd-x)
copy: key(cmd-c)
paste: key(cmd-v)
undo: edit.undo()
redo: edit.redo()
action(edit.undo): key(cmd-z)
action(edit.redo): key(cmd-shift-z)
search: key(cmd-f)
# repeater
<user.ordinal>: core.repeat_command(ordinal-1)

### app ###
save it: key(cmd-s)
flask: key(cmd-tab)
gopreev: app.tab_previous()
gonext: app.tab_next()
new tab: app.tab_open()
close tab: app.tab_close()
action(app.tab_close): key(cmd-w)
action(app.tab_open): key(cmd-t)

# app switcher
focus <user.running_applications>: user.switch_app(running_applications)
foxer: user.switch_app('Firefox')
terminal: user.switch_app('iTerm2')
crummy: user.switch_app('Google Chrome')
coder: user.switch_app('Code')

### dictation ###
speak <phrase>: auto_insert(phrase)

### code ###
assign:
  key(space)
  key('=')
  key(space)