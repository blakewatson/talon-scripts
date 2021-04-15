from talon import Context, Module
import pprint

mod = Module()
ctx = Context()

@mod.capture(rule='<phrase>')
def lowercase_formatter(m) -> str:
  'Format the text in lowercase.'
  return str(m).lower()

@mod.capture(rule='<phrase>')
def allcaps_formatter(m) -> str:
  'Format the text in allcaps.'
  return str(m).upper()

@mod.capture(rule='<phrase>')
def camel_case_formatter(m) -> str:
  'Format the text in camel case.'
  result = m[0]

  for word in m:
    print('`'+word+'`')
    result += word.capitalize()
  return str(result)

@mod.capture(rule='<phrase>')
def snake_case_formatter() -> str:
  'Format the text in snake case.'
  return 'snake'
