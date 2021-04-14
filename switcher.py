from talon import Module, Context, ui

mod = Module()
ctx = Context()

# build list of currently running applications
running = {}

for cur_app in ui.apps(background=False):
  name = cur_app.name
  running[name.lower()] = name

mod.list('running', desc='List of currently running applications')
ctx.lists['self.running'] = running

@mod.action_class
class Actions:
  def switch_app(name: str):
    'Switch the currently focused app'
    for cur_app in ui.apps(background=False):
      if cur_app.name == name:
        return cur_app.focus()

@mod.capture(rule='{self.running}')
def running_applications(m) -> str:
  'A running application'
  return str(m)