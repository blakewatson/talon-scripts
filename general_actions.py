from talon import Context, actions
ctx = Context()

@ctx.action_class('edit')
class EditActions:
    def undo(): actions.key('cmd-z')
    def redo(): actions.key('cmd-shift-z')

@ctx.action_class('app')
class AppActions:
    def tab_close(): actions.key('cmd-w')
    def tab_open():  actions.key('cmd-t')
