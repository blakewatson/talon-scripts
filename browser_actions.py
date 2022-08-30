from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app.name: Google Chrome
app.name: Firefox
app.name: Firefox Developer Edition
"""

@ctx.action_class('browser')
class BrowserActions:
    def reload():      actions.key('cmd-r')
    def reload_hard(): actions.key('cmd-shift-r')
