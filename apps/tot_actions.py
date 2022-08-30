from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app: Tot
"""

@ctx.action_class('app')
class AppActions:
    ### tabs ###
    def tab_previous(): actions.key('alt-cmd-left')
    def tab_next():     actions.key('alt-cmd-right')
