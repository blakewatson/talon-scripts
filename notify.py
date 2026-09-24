# Show the most recently recognized Talon phrase in a compact menu-bar window.
import time

import egui
from talon import actions, speech_system
from talon.egui import Window
from talon.types import Rect


phrase = ''
speech_enabled = True
_shown = False
_pending_render_at = None


async def draw_notification(ui: egui.Ui):
    global _pending_render_at
    if _pending_render_at is not None:
        elapsed = time.monotonic() - _pending_render_at
        _pending_render_at = None
        if elapsed > 0.5:
            print(f'notify: phrase-to-render delay {elapsed:.3f}s')

    text = phrase if speech_enabled else '[sleeping]'
    label = (egui.RichText(text).size(13)
             .color(egui.Color32.from_hex('#f2f2f2'))
             .extra_letter_spacing(0.3))
    frame = (egui.Frame.none().inner_margin(1)
             .fill(egui.Color32.from_hex('#1c1c1c')))
    async with frame.show():
        # Keep long phrases on one line so the display stays inside the menu bar.
        # Center the non-selectable label vertically without stretching it to
        # the row width, so the window can autosize closely around the phrase.
        async with ui.with_layout(egui.Layout.left_to_right(egui.Align.Center)):
            ui.add_space(8)
            ui.add(egui.Label(label).selectable(False))


window = Window()
window.rect = Rect(976, 1, 1, 1)
window.autosize = True
window.decorated = False
window.draggable = True
window.resizable = False
window.focusable = False
window.toplevel = True
window.transparent = True
window.set_content(draw_notification)


def on_phrase(j):
    global phrase, speech_enabled, _shown, _pending_render_at
    try:
        words = getattr(j['parsed'], '_unmapped', j['phrase'])
    except KeyError:
        return

    phrase = ' '.join(word.split('\\')[0] for word in words)
    speech_enabled = actions.speech.enabled()
    _pending_render_at = time.monotonic()
    if _shown:
        window.refresh()
    else:
        window.show()
        _shown = True
        # Position after opening; Talon may choose its own initial placement.
        # Do this only once so dragging keeps the user's chosen position.
        window.rect = Rect(976, 1, 1, 1)
        window.refresh()


def after_phrase(_):
    global speech_enabled
    enabled = actions.speech.enabled()
    if enabled != speech_enabled:
        speech_enabled = enabled
        if _shown:
            window.refresh()


speech_system.register('pre:phrase', on_phrase)
speech_system.register('post:phrase', after_phrase)
