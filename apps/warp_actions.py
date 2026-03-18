from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app.name: Warp
"""

@ctx.action_class('app')
class AppActions:
    # tabs
    def tab_previous(): actions.key('ctrl-shift-tab')
    def tab_next():     actions.key('ctrl-tab')
