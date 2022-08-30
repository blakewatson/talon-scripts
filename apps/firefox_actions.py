from talon import Context, actions
ctx = Context()
ctx.matches = r"""
app.name: Firefox
app.name: Firefox Developer Edition
"""

@ctx.action_class('app')
class AppActions:
    # tabs
    def tab_previous(): actions.key('alt-cmd-left')
    def tab_next():     actions.key('alt-cmd-right')

@ctx.action_class('browser')
class BrowserActions:
    # navigation
    def go_back():          actions.key('cmd-[')
    def go_forward():       actions.key('cmd-]')
    def focus_address():    actions.key('cmd-l')
    
    # devtools
    def toggle_dev_tools(): actions.key('alt-cmd-i')
