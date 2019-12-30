from talon import ctrl, tap, ui
from talon.canvas import Canvas

class Button:
    def __init__(self, chain, x, y, width=100, height=100):
        self.chain = chain
        self.tick = 0
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.canvas = Canvas(x, y, width, height)
        tap.register(tap.MCLICK|tap.HOOK, self.on_click)
        self.active = False
        self.pressed = False

    def hit_test(self):
        x, y = ctrl.mouse_pos()
        return (self.x <= x < self.x + self.width
            and self.y <= y < self.y + self.width)

    def draw(self, canvas):
        paint = canvas.paint

        if self.hit_test():
            if self.pressed:
                paint.color = '00cc0099'
            else:
                paint.color = '33333399'
        else:
            paint.color = '00000099'

        paint.style = paint.Style.FILL
        canvas.draw_rect(canvas.rect)

        paint.color = 'white'
        paint.style = paint.Style.FILL
        paint.textsize = 20
        key = self.chain[self.tick]
        _, trect = paint.measure_text(key)
        canvas.draw_text(key, canvas.x + canvas.width  / 2 - trect.width / 2,
                              canvas.y + canvas.height / 2 + trect.height / 2)

    def on_click(self, typ, e):
        if not self.active:
            return
        if self.hit_test():
            e.block()
            if e.down:
                self.pressed = True
            else:
                self.pressed = False
                key = self.chain[self.tick]
                self.tick = (self.tick + 1) % len(self.chain)
                ctrl.key_press(key)

    def show(self):
        if not self.active:
            self.active = True
            self.canvas.register('draw', self.draw)

    def hide(self):
        if self.active:
            self.active = False
            self.canvas.unregister('draw', self.draw)

x = 100
y = 100
button1 = Button(['space', 'space', 'down'], x, y)
button2 = Button(['up'],   x + 100, y)
button3 = Button(['down'], x, y + 100)

buttons = [button1, button2, button3]

def update(*args):
    if 'Talon Speech Collection' in ui.active_window().title:
        for button in buttons:
            button.show()
    else:
        for button in buttons:
            button.hide()
ui.register('', update)
update()
