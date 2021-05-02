app: Nova
-
pallet: key(shift-cmd-p)
phylum: key(cmd-p)
action(app.window_open): key(cmd-shift-n)

# tabs
action(app.tab_previous): key(cmd-{)
action(app.tab_next): key(cmd-})
#action(user.go_to_numbered_tab): key(numeral)
go tab <user.numeral>: key("cmd-{numeral}")

# coding
action(edit.indent_more): key(cmd-])
action(edit.indent_less): key(cmd-[)
add cursors: key(alt-shift-i)
grab next: key(cmd-d)
line up: key(alt-up)
line down: key(alt-down)