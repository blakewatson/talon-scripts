from talon import tap, voice
from talon.engine import engine
from talon_plugins import speech

sleep_group = voice.ContextGroup('sleepy')
sleepy = voice.Context('sleepy', group=sleep_group)

# toggle button
def on_key(typ, e):
   if e == 'alt-ctrl-f12' and e.down:
        speech.set_enabled(not voice.talon.enabled)
        e.block()
tap.register(tap.KEY|tap.HOOK, on_key)

sleepy.keymap({
    'talon sleep': lambda m: speech.set_enabled(False),
    'talon wake': lambda m: speech.set_enabled(True),

    'dragon mode': [lambda m: speech.set_enabled(False), lambda m: engine.mimic('wake up'.split())],
    'talon mode': [lambda m: speech.set_enabled(True), lambda m: engine.mimic('go to sleep'.split())],
})
sleep_group.load()