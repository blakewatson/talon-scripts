from talon import Context, actions
ctx = Context()

@ctx.action_class('edit')
class EditActions:
    def indent_more(): actions.key('cmd-]')
    def indent_less(): actions.key('cmd-[')
