Scale.default = "minor"

Clock.bpm = 70

var.roots = var([0, -3], dur=8)

p1 >> piano(var.roots + P(0, 2, 4), dur=1).offbeat(1)

b1 >> bass(var.roots + P[0, 6, 6, 0, 2, 0, 4, 2, 4], dur=[1, 1/4, 1/2, rest(1/2), 1/4, 1/2, 1/4, rest(1/4), 1/2], lpf=600)

p2 >> piano(var.roots + P[0, 6, 6, 0, 2, 0, 4, 2, 4], dur=[1, 1/4, 1/2, rest(1/2), 1/4, 1/2, 1/4, rest(1/4), 1/2])

d1 >> play("X-")
