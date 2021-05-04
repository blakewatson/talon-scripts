### text formatters ###
(phrase | speak) <phrase>$: auto_insert(phrase)
shrink <user.shrink_formatter>$: auto_insert(shrink_formatter)
word <user.word_formatter>$: auto_insert(word_formatter)
<user.slicer_formatter>$: auto_insert(slicer_formatter)
<user.formatters>$: user.format_text(formatters)
<user.format>$: auto_insert(format)

### text navigation and selection ###
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
smear:
  key(cmd-right)
  key(left)
clap: key(cmd-right)
lefty: key(cmd-left)
lecksy: key(cmd-shift-left)
rexy: key(cmd-shift-right)
select all: key(cmd-a)

### text manipulation ###
slap: key(cmd-right enter)
killer: key(backspace:2)
slurp:
  key(backspace)
  key(delete)
indent: edit.indent_more()
dedent: edit.indent_less()

### code ###
assign:
  key(space)
  key('=')
  key(space)
arrow: key(- >)
fat arrow: key(space = > space)
<user.npm_script>: insert(npm_script)
slasher: key(/ / space)
block: key(space { enter)
nolan: insert('null')
thistle: insert('this')
sinker:
  key(cmd-right)
  key(;)
console log: insert('console.log(')
spaceer: key(space left space)
triple equals: insert(' === ')