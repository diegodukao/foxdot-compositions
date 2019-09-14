Scale.default = "minor"     

b1 >> bass([0, -1], dur=8, amp=0.8)

p1 >> fuzz(b1.pitch + [0, 2, 3, 5], oct=3, dur=1/2, lpf=linvar([1000, 5000], 12), amp=1).stop()

p2 >> keys(b1.pitch + (0, 2, 4), dur=4).stop()

p3 >> karp(b1.pitch + P[0:7], dur=PDur(3, 8)*2, amp=1.2).penta().every(4, "shuffle")

p4 >> pads(b1.pitch, dur=4, chop=[8, 16], amp=1.5)

p5 >> karp(b1.pitch + P[0:7], dur=PDur(5, 8), amp=1.2).penta().shuffle().stop()

p6 >> viola(p5.pitch, dur=[8, 8, 8, 1, 2, 1, 4], amp=1.3).stop()

~d1 >> play("X o( [ o])")
d2 >> play("[--]").every(6, "stutter", 4)
d3 >> play("^  ^").every(4, "stutter", 4)

d_all.stop()
