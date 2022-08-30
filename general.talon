### global ###
mission: key(ctrl-up)
apogee: key(ctrl-down)
flask: key(cmd-tab)
cycle: key(cmd-~)
alley: key(alt-space)
clipper: key(alt-cmd-c)
cleaver: key(cmd-x)
copy: key(cmd-c)
paste: key(cmd-v)
screenshotter: key(cmd-shift-4)
undo: edit.undo()
redo: edit.redo()
search: key(cmd-f)
character map: key(ctrl-cmd-space)
# repeater
<user.ordinal>: core.repeat_command(ordinal-1)

### app ###
save it: key(cmd-s)
new window: app.window_open()
table: app.tab_previous()
tabber: app.tab_next()
new tab: app.tab_open()
close tab: app.tab_close()
go tab <user.numeral>: user.go_to_numbered_tab(numeral)

# app switcher
focus <user.running_applications>: user.switch_app(running_applications)
focus writer: user.switch_app('iA Writer')
archiver: user.switch_app('The Archive')
crafter: user.switch_app('Craft')
vsc: user.switch_app('Code')
bowser: user.switch_app('Google Chrome')
firefox: user.switch_app('Firefox')
nova: user.switch_app('Nova')
terminal: user.switch_app('iTerm2')
tutor: user.switch_app('Tot')

### dictation ###
speak <phrase>: auto_insert(phrase)
