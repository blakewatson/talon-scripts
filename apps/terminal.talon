app: iTerm2
app: Terminal
app: Warp
-
CD: key(c d space)
lister: insert('ls ')
list all: insert('ls -la')
make directory: insert('mkdir ')
get status: insert('git status')
get push: insert('git push')
get pull: insert('git pull')
get add: insert('git add ')
get add all: insert('git add *')
get commit:
  insert('git commit -m ""')
  key(left)

# destinations and shortcuts
talon user: insert('cd ~/.talon/user')
talon log: insert('~/.talon/.venv/bin/tail_log')
talon ripple: insert('~/.talon/.venv/bin/repl')
# jumpy shortcut
jumpy: insert('j ')