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
lucy: key(left)
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
righty: key(cmd-shift-right)
select all: key(cmd-a)
grab it:
    key(alt-right)
    key(shift-alt-left)
    
    ### text manipulation ###
next: key(space)
junk | chunk | junky | junker: key(backspace)
slap: key(cmd-right enter)
killer: key(backspace:2)
blaster: key(alt-backspace)
slurpy:
    key(backspace)
    key(delete)
indent: edit.indent_more()
dedent: edit.indent_less()

### quick text ###
lolly: key(l o l)

### code ###
assignment:
    key(space)
    key('=')
    key(space)
koala | equator:
    key(=)
    key('"')
    key('"')
    key(left)
pointer: key(- >)
fat arrow: key(space = > space)
node script: insert('npm run ')
<user.npm_script>: insert(npm_script)
run script: insert('npm run ')
slasher: key(/ / space)
block: key(space { enter)
nolan: insert('null')
fizzle: insert('this.')
sinker:
    key(cmd-right)
    key(;)
console log: insert('console.log(')
console error: insert('console.error(')
spacer: key(space left space)
triple equals: insert(' === ')
not equals: insert(' !== ')

code import:
    insert('import {  } from \'\';')
    key(left:2)
    # moves the cursor to the import body: { $here }
code members:
    key(cmd-left)
    key(alt-right)
    key(right:3)
code export: insert('export const ')
code export enum: insert('export enum ')
code export type: insert('export type ')
code export default: insert('expert default ')
code constant: insert('const ')
code let: insert('let ')
code far: insert('var ')
code if: insert('if (')
code and: insert(' && ')
code or: insert(' || ')
code for: insert('for (')
code for let: insert('for (let ')
code question: insert(' ?? ')
code function:
    insert('function ()')
    key(left:2)
code (aero | arrow) empty: insert('() => ')
code (aero | arrow):
    insert('() => ')
    key(left:5)
(aero | arrow) body: key(right:5)
(aero | arrow) block:
    key(right:5)
    key({ enter)
code public: insert('public ')
code protected: insert('protected ')
code private: insert('private ')
code get: insert('get ')
code enum: insert('enum ')
code type: insert('type ')
code return: insert('return ')
