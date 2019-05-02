Clock.bpm = 130 # Pick your own bpm

print(Scale.names()) # Pick your own scale!

Scale.default = "minor"

Scale.default = "minorPentatonic"

print(SynthDefs) # Pick your own synths!

b1 >> sawbass(var([0, 2], 1/4), dur=1/32).stop()

b1 >> sawbass(var([0, 2, 0, 2, 3, 0, 6], 8), dur=1)

p1 >> keys(b1.pitch + (0, 2, 4), dur=8)

print(b1.pitch)

p2 >> blip(P[0, 2, 4].stretch(8), dur=1/2, sus=2) + var([0, 2], [6, 2])

print(P[0, 2, 4].stretch(8) + var([0, 2], [6, 2]))

print(var([0, 2], [6, 2]))

d1 >> play("xs")

d2 >> play("  * ")

Clock.bpm = 60

d3 >> play("(+  )+( [( +)+])")
