Clock.bpm = 180
var.roots = var(0)

Scale.default = "minor"

b0 >> bass([0, 2], dur=[12, 4]).solo()
p1 >> piano(b0.pitch + (0, 2, 4, 6), dur=[8, 4, 4], amp=1).solo()
p2 >> piano(b0.pitch + P[0:7], dur=1, amp=1).shuffle().solo()

print(SynthDefs)

p3 >> bass(b0.pitch + [0, 4, 0, 4, 0, 4, 5], dur=1/2, amp=1.3)

p4 >> viola(b0.pitch + [2, 5, 7, 0], dur=1, amp=1)

p4.stop()

p5 >> bass(dur=2)


d1 >> play("x", amp=1)
d2 >> play("w").every(4, "offadd", 2).stop()
d3 >> play("~").every(2, "stutter", 32, amp=1)

d4 >> play("xo XO").every(2, "stutter", 32)

d5 >> play("X ", amp=1)

d6 >> play("X oX XO " , amp=1)
d7 >> play(" o  o        Oxx" , amp=1)
