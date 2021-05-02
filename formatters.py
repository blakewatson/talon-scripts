from talon import Context, Module, actions, clip
from random import randint
import pprint

mod = Module()
ctx = Context()

dont_capitalize_these_words = ['a', 'an', 'and', 'or', 'the', 'of', 'in']

shrunken_words = {
    "administrator": "admin",
    "alternate": "alt",
    "apartment": "apt",
    "applications": "apps",
    "arguments": "args",
    "attributes": "attrs",
    "authentication": "auth",
    "button": "btn",
    "command": "cmd",
    "compute": "cmp",
    "context": "ctx",
    "concatenate": "concat",
    "configure": "config",
    "control": "ctrl",
    "format": "fmt",
    "image": "img",
    "jason": "json",
    "message": "msg",
    "package": "pkg",
    "parameter": "param",
    "source": "src",
    "standard": "std",
    "temporary": "tmp",
    "text": "txt",
    "user": "usr",
    "user id": "uid",
    "utilities": "utils",
    "user": "usr",
    "error": "err",
    "boolean": "bool",
    "return": "ret",
    "package": "pkg",
    "python": "py",
    "project": "proj",
    "random": "rand",
    "frequency": "freq",
    "operations": "ops",
    "initialize": "init",
    "iterator": "iter",
    "vector": "vec",
    "convolution": "conv",
    "deconvolution": "deconv",
    "derivative": "deriv",
    "destination": "dest",
    "distribution": "dist",
    "contribute": "contrib",
    "delete": "del",
    "different": "diff",
    "square root": "sqrt",
    "sequence": "seq",
    "predict": "pred",
    "ending": "end",
    "yaml": "yml",
    "condition": "cond",
    "validation": "val",
    "optimization": "opt",
    "generator": "gen",
    "memory": "mem",
    "environments": "envs",
    "environment": "env",
    "application": "app",
    "inc.": "inc",
    "_c": "char",
    "administrator": "admin",
    "administrators": "admins",
    "allocate": "alloc",
    "alternate": "alt",
    "apartment": "apt",
    "application": "app",
    "applications": "apps",
    "architecture": "arch",
    "argument": "arg",
    "arguments": "args",
    "attribute": "attr",
    "attributes": "attrs",
    "authentic": "auth",
    "authenticate": "auth",
    "author": "auth",
    "binary": "bin",
    "button": "btn",
    "calculate": "calc",
    "call": "col",
    "car": "char",
    "care": "char",
    "certificate": "cert",
    "character": "char",
    "column": "col",
    "command": "cmd",
    "concatenate": "concat",
    "configuration": "config",
    "configure": "config",
    "constant": "const",
    "define": "def",
    "descending": "desc",
    "develop": "dev",
    "developer": "dev",
    "development": "dev",
    "dictionary": "dict",
    "directory": "dir",
    "divider": "div",
    "document": "doc",
    "environment": "env",
    "execute": "exec",
    "extend": "ext",
    "extension": "ext",
    "favorite": "fav",
    "function": "func",
    "image": "img",
    "imager": "int",
    "incorporate": "inc",
    "increment": "inc",
    "initialize": "init",
    "integer": "int",
    "iterate": "iter",
    "jason": "json",
    "language": "lang",
    "large": "lg",
    "latitude": "lat",
    "length": "len",
    "library": "lib",
    "locate": "loc",
    "location": "loc",
    "longitude": "lng",
    "medium": "md",
    "minimum": "min",
    "miscellaneous": "misc",
    "navigate": "nav",
    "navigation": "nav",
    "number": "num",
    "object": "obj",
    "parameter": "param",
    "parameters": "params",
    "position": "pos",
    "previous": "prev",
    "production": "prod",
    "pseudo": "sudo",
    "reference": "ref",
    "references": "refs",
    "repeat": "rep",
    "request": "req",
    "result": "res",
    "revision": "rev",
    "source": "src",
    "standard": "std",
    "standing": "stdin",
    "standout": "stdout",
    "string": "str",
    "system": "sys",
    "temporary": "tmp",
    "text": "txt",
    "thanks": "thx",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "variable": "var",
    "velocity": "vel",
    # months,
    "january": "jan",
    "february": "feb",
    "march": "mar",
    "april": "apr",
    "june": "jun",
    "july": "jul",
    "august": "aug",
    "september": "sept",
    "october": "oct",
    "november": "nov",
    "december": "dec",
}

@mod.action_class
class Actions:
  def format_text(formatter: str):
    'Format existing text.'
    text = actions.edit.selected_text()
    text = format_functions[formatter](text)
    actions.auto_insert(text)

mod.list('formatters', desc='A list of text formatters.')
ctx.lists['self.formatters'] = {
  'camel': 'camel',
  'dotsway': 'dotsway',
  'kebab': 'kebab',
  'lower': 'lower',
  'more': 'more',
  'pascal': 'pascal',
  'pathway': 'pathway',
  'say': 'say',
  'sentence': 'sentence',
  'smash': 'smash',
  'snake': 'snake',
  'spongebob': 'spongebob',
  'title': 'title',
  'upper': 'upper',
  'yelsnik': 'yelsnik'
}

mod.list('slicers', desc='Shorthand for returning a substring.')
ctx.lists['self.slicers'] = {
  'tree': '3',
  'quad': '4'
}

def allcaps(s):
  return s.upper()

def camel(s):
  words = s.split(' ')
  result = words[0]
  for word in words[1:]:
    result += word.capitalize()
  return result

def dot_join(s):
  words = s.split(' ')
  return '.'.join(words).lower()

def kebab(s):
  words = s.split(' ')
  return '-'.join(words).lower()

def lowercase(s):
  return s.lower()

def pascal(s):
  words = s.split(' ')
  capitalized_words = []
  for word in words:
    capitalized_words.append(word.capitalize())
  return ''.join(capitalized_words)

def sentence(s):
  text = s[0:1].capitalize()
  text += s[1:]
  return text

def slash_join(s):
  words = s.split(' ')
  return '/'.join(words).lower()

def slicer(s, num):
  return s[0:num]

def smash(s):
  return ''.join(s.split(' ')).lower()

def snake(s):
  words = s.split(' ')
  return '_'.join(words).lower()

def spongebob(s):
  capitalize = bool(randint(0, 1))
  formatted_string = ''
  
  for char in s:
    if not char.isalpha():
      formatted_string += char
    elif capitalize:
      formatted_string += char.upper()
    else:
      formatted_string += char.lower()
    capitalize = not capitalize

  return formatted_string

def title(s):
  words = s.split(' ')
  title_words = [words[0].capitalize()]
  for word in words[1:]:
    if word not in dont_capitalize_these_words:
      word = word.capitalize()
    title_words.append(word)
  return ' '.join(title_words)

format_functions = {
  'camel': lambda s: camel(s),
  'dotsway': lambda s: dot_join(s),
  'kebab': lambda s: kebab(s),
  'lower': lambda s: lowercase(s),
  'more': lambda s: ' ' + s,
  'pascal': lambda s: pascal(s),
  'pathway': lambda s: slash_join(s),
  'say': lambda s: lowercase(s),
  'sentence': lambda s: sentence(s),
  'smash': lambda s: smash(s),
  'snake': lambda s: snake(s),
  'spongebob': lambda s: spongebob(s),
  'title': lambda s: title(s),
  'upper': lambda s: allcaps(s),
  'yelsnik': lambda s: allcaps(snake(s))
}

@mod.capture(rule='<word>')
def shrink_formatter(m) -> str:
  'Shrink the word.'
  word = m.word.lower()
  if word in shrunken_words:
    return shrunken_words[word]
  return ''

@mod.capture(rule='<word>')
def word_formatter(m) -> str:
  'Return a single word.'
  return str(m.word)

@mod.capture(rule='^{self.slicers} <word>')
def slicer_formatter(m) -> str:
  'Returns the first n characters of the provided word.'
  return slicer(m.word, int(m.slicers))

@mod.capture(rule='format {self.formatters}')
def formatters(m) -> str:
  'Format the selected text with the given formatter.'
  return str(m.formatters)

@mod.capture(rule='{self.formatters} <phrase>')
def format(m) -> str:
  'Format the next spoken text according to the provided formatter.'
  return format_functions[m.formatters](m.phrase)
