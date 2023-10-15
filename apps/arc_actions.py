from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app.name: Arc
"""

@ctx.action_class('app')
class AppActions:
    # tabs
    def tab_previous(): actions.key('alt-cmd-up')
    def tab_next():     actions.key('alt-cmd-down')

@ctx.action_class('browser')
class BrowserActions:
    # navigation
    def go_back():          actions.key('cmd-[')
    def go_forward():       actions.key('cmd-]')
    def focus_address():    actions.key('cmd-l')
    
    # devtools
    def toggle_dev_tools(): actions.key('alt-cmd-i')
