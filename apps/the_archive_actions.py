from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app: The Archive
"""

@ctx.action_class('edit')
class EditActions:
    def indent_more(): actions.key('cmd-]')
    def indent_less(): actions.key('cmd-[')

@ctx.action_class('app')
class AppActions:
    def tab_next():     actions.key('ctrl-tab')
    def tab_previous(): actions.key('ctrl-shift-tab')
