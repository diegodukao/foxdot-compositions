Scale.default = "minor"
Root.default = "e"
Clock.bpm = 120

p1 >> sawbass([0, -1], dur=8)

p1 >> sawbass([1, -3], dur=8)

p2 >> keys(p1.pitch + (0, 2, 4), dur=PDur(3, 8))

p3 >> prophet(p1.pitch + P[0:6], dur=PDur(3, 8), amp=2).every(1, "shuffle")

d8 >> play("X ", amp=2).stop()


d9 >> pluck(p1.pitch, dur=1/2)


d1 >> play("o  oo    o   o  ", amp=2)
d2 >> play(" oo  oooo ooo oo", amp=0.8)
d3 >> play("X       xX  xX  ", amp=2)
d4 >> play("        x   x   ", amp=0.6).stop()
d5 >> play("T T T  T ")



print(Samples)
