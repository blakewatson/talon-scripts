### global ###
scroll mode: key(f6)
breaker: key(shift-enter)
mission: key(ctrl-up)
windows: key(ctrl-down)
flask: key(cmd-tab)
cycle: key(cmd-~)
alley | alfred: key(alt-space)
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
toggle desk heater: key(alt-`)

### app ###
save it | supersave: key(cmd-s)
new window: app.window_open()
table: app.tab_previous()
tabber | tipsy: app.tab_next()
new tab: app.tab_open()
close tab: app.tab_close()
go tab <user.numeral>: user.go_to_numbered_tab(numeral)

# app switcher
focus <user.running_applications>: user.switch_app(running_applications)
focus writer: user.switch_app('iA Writer')
archiver: user.switch_app('The Archive')
crafter: user.switch_app('Craft')
vsc: user.switch_app('Code')
cursor: user.switch_app('Cursor')
bicycle: user.switch_app('Bike')
^google$: user.switch_app('Google Chrome')
firefox: user.switch_app('Firefox')
edgy: user.switch_app('Microsoft Edge')
archie: user.switch_app('Arc')
bowser: user.switch_app('Vivaldi')
obsidian: user.switch_app('Obsidian')
^screens$: user.switch_app('Screens 5')
^brainwave$: user.switch_app('BrainWave Chat')
fastmill|fastmail: user.switch_app('Fastmail')
# discord tab in arc
discord: user.switch_app('Discord')
# brainwave tab in chrome
#brainwave:
  #5user.switch_app('Google Chrome')
  #5sleep(0.1)
  #5key(cmd-1)
# fastmail tab in chrome
#fastmill|fastmail:
  #user.switch_app('Google Chrome')
  #sleep(0.1)
  #key(cmd-2)
# a fine start in the current arc space
finer tab:
  user.switch_app('Arc')
  sleep(0.1)
  key(cmd-1)
nova: user.switch_app('Nova')
terminal:
  user.switch_app('Terminal')
  user.switch_app('iTerm2')
  user.switch_app('Warp')
tutor: user.switch_app('Tot')
sketcher: user.switch_app('Sketch')

### dictation ###
speak <phrase>: auto_insert(phrase)
^dictate$:
  speech.disable()
  key(cmd-y)

### mouseless ###
mousy: key(cmd-alt-')
scatter: key(cmd-alt-;)