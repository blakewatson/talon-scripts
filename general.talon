### global ###
alley: key(alt-space)
cut: key(cmd-x)
copy: key(cmd-c)
paste: key(cmd-v)

### app ###
save it: key(cmd-s)
flask: key(cmd-tab)
gopreev: app.tab_previous()
gonext: app.tab_next()

# app switcher
focus <user.running_applications>: user.switch_app(running_applications)
foxer: user.switch_app('Firefox')
terminal: user.switch_app('iTerm2')
crummy: user.switch_app('Google Chrome')
coder: user.switch_app('Code')

### text navigation ###
jeep: key(up)
dune: key(down)
lloyd: key(left)
chris: key(right)
gravel: key(shift-left)
grabber: key(shift-right)
peg: key(alt-left)
fran: key(alt-right)
scram: key(shift-alt-left)
scrish: key(shift-alt-right)
clap: key(cmd-right)
lefty: key(cmd-left)
lecksy: key(cmd-shift-left)
recksy: key(cmd-shift-right)
alley: key(alt-space)

### text manipulation ###
killer: key(backspace:2)

### dictation ###
say <phrase>: auto_insert(phrase)
phrase <phrase>: auto_insert(phrase)

