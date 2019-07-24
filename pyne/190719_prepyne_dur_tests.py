Scale.default = "minor"
Root.default = "C"
Clock.bpm = 120

var.roots = var(P[0, 2, 1, var([4, 3, 2], dur=[4, 2, 2])], dur=8)

p1 >> piano(var.roots, dur=4)

var.roots = var(P[0, 4, 6, var(P[3, 2, 1], dur=[2, 1, 1])], dur=4)

p1 >> piano(var.roots, dur=[1/2, 1/4, 1/4, 1/2, 1/4, 1/2, 1/2, 1/4]) + (0, 2, 4)

print(p1.pitch)


print(SynthDefs)
