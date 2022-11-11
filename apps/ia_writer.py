from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app: iA Writer
"""

@ctx.action_class('app')
class AppActions:
    # tabs
    def tab_next():     actions.key('ctrl-tab')
    def tab_previous(): actions.key('ctrl-shift-tab')