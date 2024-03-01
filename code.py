from talon import Module, Context

mod = Module()
ctx = Context()

@mod.capture(rule='runner <word>')
def npm_script(m) -> str:
  'Run an npm script.'
  return 'npm run ' + str(m.word).lower()