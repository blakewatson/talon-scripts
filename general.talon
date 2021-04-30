### global ###
mission: key(ctrl-up)
apogee: key(ctrl-down)
alley: key(alt-space)
clipper: key(alt-cmd-c)
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
new window: app.window_open()
gopreev: app.tab_previous()
gonext: app.tab_next()
new tab: app.tab_open()
close tab: app.tab_close()
go tab <user.numeral>: user.go_to_numbered_tab(numeral)
action(app.tab_close): key(cmd-w)
action(app.tab_open): key(cmd-t)

# app switcher
focus <user.running_applications>: user.switch_app(running_applications)
focus writer: user.switch_app('iA Writer')
coder: user.switch_app('Code')
crummy: user.switch_app('Google Chrome')
foxer: user.switch_app('Firefox')
terminal: user.switch_app('iTerm2')
tutor: user.switch_app('Tot')

### dictation ###
speak <phrase>: auto_insert(phrase)