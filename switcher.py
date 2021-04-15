from talon import Module, Context, ui, app

mod = Module()
ctx = Context()

  # build list of currently running applications
def update_running_applications_list():
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

def ui_event(event, arg):
    if event in ("app_launch", "app_close"):
        update_running_applications_list()

# Talon starts faster if you don't use the `talon.ui` module during launch
def on_ready():
  update_running_applications_list()
  ui.register("", ui_event)


# NOTE: please update this from "launch" to "ready" in Talon v0.1.5
app.register("ready", on_ready)