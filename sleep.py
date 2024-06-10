from talon import app, actions

def disable():
    actions.speech.disable()

app.register("ready", disable)