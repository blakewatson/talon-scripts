# This file will add a notification to tell you what Talon heard you say
import egui
from talon import actions, speech_system, imgui
from talon.types import Rect


class CompactNotification(imgui.GUI):
    async def render(self, ui):
        # Replace imgui's padded frame, while retaining its positioning and updates.
        frame = (egui.Frame.none().inner_margin(2)
                 .fill(egui.Color32.from_hex('#1c1c1c')))
        async with frame.show():
            self.update(imgui.UIWrapper(ui))

    def tick(self):
        super().tick()
        # The default imgui renderer also positions the window. Keep that step
        # outside the drawing callback to avoid locking the native UI thread.
        if self.window is None:
            return
        rect = self.window.rect
        if rect.x != self.x or rect.y != self.y:
            self.window.rect = Rect(self.x, self.y, rect.width, rect.height)

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

# Match the menu-bar space used by this display on the main screen.
@CompactNotification.open(x=976, y=1)
def draw_notification(gui):
    text = phrase if actions.speech.enabled() else '[sleeping]'
    label = (egui.RichText(text).size(13)
             .color(egui.Color32.from_hex('#f2f2f2'))
             .extra_letter_spacing(0.3))
    # Keep long phrases on one line so the display stays inside the menu bar.
    gui.ui.add(egui.Label(label).extend())


speech_system.register('post:phrase', on_phrase)
