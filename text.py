from talon import Context, clip, actions

ctx = Context()

@ctx.action_class("edit")
class edit_actions:
  def copy():
    actions.key('cmd-c')
    
  def selected_text() -> str:
    with clip.capture() as s:
      actions.edit.copy()
    try:
      return s.get()
    except clip.NoChange:
      return ""