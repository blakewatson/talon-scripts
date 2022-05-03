app: sixtyforce
-
settings():
  key_hold = 50

# L, R, A, and B
little: key(a)
red: key(s)
air: key(x)
bill: key(b)
billy:
  key(b:down)
  sleep(3)
  key(b:up)

# C buttons
see up: key(i)
see down: key(k)
see left: key(j)
see right: key(l)

# Z
zoo: key(z)

# view routes
look left:
  key(a:down)
  sleep(2)
  key(a:up)

look right:
  key(s:down)
  sleep(2)
  key(s:up)