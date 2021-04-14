from talon import Context, Module

mod = Module()
ctx = Context()

@mod.capture(rule='<phrase>')
def allcaps_formatter(m) -> str:
  'Format the text in allcaps.'
  return str(m).upper()

@mod.capture(rule="<phrase>")
def camel_case_formatter(m) -> str:
  'Format the text in camel case.'
  print(m)
  return 'camel'
