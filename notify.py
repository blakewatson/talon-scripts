# This file will add a notification to tell you what Talon heard you say
from talon import actions, app, speech_system, imgui

phrase = ''

def on_phrase(j):
    global phrase
    try:
        phrase = getattr(j["parsed"], "_unmapped", j["phrase"])
        phrase = " ".join(word.split("\\")[0] for word in phrase)
        draw_notification.show()
    except KeyError:
        # do nothing
        return

#    app.notify(phrase)

@imgui.open(y=0)
def draw_notification(gui):
    if not actions.speech.enabled():
        gui.text('[sleeping]')
        return
    gui.text(phrase)


speech_system.register('post:phrase', on_phrase)

