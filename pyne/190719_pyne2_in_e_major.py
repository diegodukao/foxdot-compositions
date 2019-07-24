Scale.default = "major"
Root.default = "E"
Clock.bpm = 120

p1 >> piano([0, -2], dur=8)

p2 >> piano(p1.pitch, dur=p1.dur) + (0, 2, 4)

p3 >> sawbass(p1.pitch + P[0, 2, 4, 6], sus=1/4, dur=[1, 1/4, 1/4, 1/2], amp=1.5).every(4, "offadd", 3)

p4 >> viola(p1.pitch + P[0:8], dur=1/4, amp=1).penta()

p1 >> piano([1, -3], dur=8)

d1 >> play("XXX X  X")
d2 >> play(" o    (o[ o]) ")
d3 >> play("----", dur=1/4)

print(SynthDefs)
