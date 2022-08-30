from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app: Craft
"""

@ctx.action_class('app')
class AppActions:
    # tabs
    def tab_next():     actions.key('ctrl-tab')
    def tab_previous(): actions.key('ctrl-shift-tab')

@ctx.action_class('edit')
class EditActions:
    # indention
    def indent_more(): actions.key('tab')
    def indent_less(): actions.key('shift-tab')
