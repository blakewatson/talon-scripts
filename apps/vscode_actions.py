from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app: Code
"""

@ctx.action_class('app')
class AppActions:
    def window_open():  actions.key('cmd-shift-n')
    
    # tabs
    def tab_previous(): actions.key('alt-cmd-left')
    def tab_next():     actions.key('alt-cmd-right')

@ctx.action_class('edit')
class EditActions:
    # coding
    def indent_more(): actions.key('cmd-]')
    def indent_less(): actions.key('cmd-[')
