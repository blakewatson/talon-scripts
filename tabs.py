from talon import Module, Context, actions

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
  def go_to_numbered_tab(num: str):
    'Switch to a tab by number.'
    actions.key(f"cmd-{num}")