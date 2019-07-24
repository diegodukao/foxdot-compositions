Scale.default = "minor"
Root.default = "e"
Clock.bpm = 120

p1 >> blip([0, -1], dur=4, oct=4)

p2 >> keys(p1.pitch + (0, 2, 4), dur=PDur(3, 8))

c, d, e, f, g, a
0, 1, 2, 3, 4

p3 >> bass(p1.pitch + [0, 2, 4], dur=1, sus=P[]).every(4, "offadd", 4)

p4 >> viola(p1.pitch + P[0:6], dur=PDur(3, 8), oct=5).penta().shuffle()


print(SynthDefs)

print(Samples)

d1 >> play("X O( [ X])")
d2 >> play("----", amp=2).every(4, "stutter", 16)


d1.stop()
d2.stop()






























