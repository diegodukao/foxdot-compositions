Scale.default = "blues"
Root.default = "E"
Clock.bpm = 120

p0 >> piano([0, -1, 2, 1], dur=8)

p1 >> twang(p0.pitch + P[0:14], dur=1/4, sus=1/4).penta().shuffle()

p2 >> sawbass(p0.pitch + P[0, 2, 4, 6], dur=[1, 1/4, 1/4, 1/2], hpf=800, sus=1/4)


d1 >> play("X", dur=PDur(3, 8))
d2 >> play("o", dur=PDur(2, 7))
d3 >> play("X", dur=PDur(1, 7))
d4 >> play("-", dur=1/4)

print(SynthDefs)
