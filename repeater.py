from talon import Module, Context

mod = Module()
ctx = Context()

ordinals = {
  'second': '2',
  'third': '3',
  'fourth': '4',
  'fifth': '5',
  'sixth': '6',
  'seventh': '7',
  'eighth': '8',
  'ninth': '9',
  'tenth': '10'
}

mod.list('ordinals', desc='Ordinal words')

ctx.lists['self.ordinals'] = ordinals

@mod.capture(rule='{self.ordinals}')
def ordinal(m) -> str:
  'A single integer based on an ordinal word'
  return int(str(m))