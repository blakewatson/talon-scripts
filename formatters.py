from talon import Context, Module
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
  words = m.phrase.split(' ')
  result = words[0]
  for word in words[1:]:
    result += word.capitalize()
  return result

@mod.capture(rule='<phrase>')
def kebab_case_formatter(m) -> str:
  'Format the text in kebab case.'
  words = m.phrase.split(' ')
  return '-'.join(words).lower()

@mod.capture(rule='<phrase>')
def more_formatter(m) -> str:
  'Add a space and then normal text'
  return ' ' + str(m)

@mod.capture(rule='<phrase>')
def pascal_case_formatter(m) -> str:
  'Format the text in pascal case.'
  words = m.phrase.split(' ')
  capitalized_words = []
  for word in words:
    capitalized_words.append(word.capitalize())
  return ''.join(capitalized_words)

@mod.capture(rule='<phrase>')
def sentence_formatter(m) -> str:
  'Capitalize the first word in the phrase.'
  return m.phrase.capitalize()

@mod.capture(rule='<word>')
def shrink_formatter(m) -> str:
  'Shrink the word.'
  word = m.word.lower()
  if word in shrunken_words:
    return shrunken_words[word]
  return ''

@mod.capture(rule='<phrase>')
def smash_formatter(m) -> str:
  'Concatenate the words and lowercase them.'
  return ''.join(m.phrase.split(' ')).lower()

@mod.capture(rule='<phrase>')
def snake_case_formatter(m) -> str:
  'Format the text in snake case.'
  words = m.phrase.split(' ')
  return '_'.join(words).lower()

@mod.capture(rule='<phrase>')
def title_case_formatter(m) -> str:
  'Capitalize each word.'
  words = m.phrase.split(' ')
  title_words = [words[0].capitalize()]
  for word in words[1:]:
    if word not in dont_capitalize_these_words:
      word = word.capitalize()
    title_words.append(word)
  return ' '.join(title_words)

@mod.capture(rule='<word>')
def word_formatter(m) -> str:
  'Return a single word.'
  return str(m.word)
