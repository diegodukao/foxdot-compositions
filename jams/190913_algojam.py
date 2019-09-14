Clock.bpm = 180
var.roots = var(0)

b0 >> bass([0, 2], dur=[12, 4])

p1 >> piano(b0.pitch + (0, 2, 4), dur=8, amp=2)

p2 >> piano(b0.pitch + P[0:7], dur=1, amp=2.2).shuffle()

print(SynthDefs)
p3 >> bass(b0.pitch + [0, 4, 0, 4, 0, 4, 5], dur=1/2, amp=1.5)

p4 >> viola(b0.pitch + [2, 5, 7, 0], dur=1, amp=2)

p4.stop()

p5 >> bass(dur=2).stop()


d1 >> play("x", amp=5)
d2 >> play("w").every(4, "offadd", 2).stop()
d3 >> play("~").every(2, "stutter", 32, amp=4)

d4 >> play("xo XO").every(2, "stutter", 32).stop()

d5 >> play("X ", amp=5).stop()

d6 >> play("X oX XO " , amp=5).stop()
d7 >> play(" o  o        Oxx" , amp=6).stop()