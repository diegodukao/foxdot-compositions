Scale.default = "minor"

p0 >> bass(var([0, 2], dur=[12, 4]), dur=4)

p1 >> fuzz(p0.pitch + [0, 2, 3, 4], dur=1/2, oct=3, lpf=linvar([1000, 5000], 12), amp=1.2).every(8, "bubble")

p2 >> keys(p0.pitch + P(0, 2, 4), dur=var([1/2, 1], dur=4), amp=1.2)

p3 >> karp(p0.pitch + [0, 2, 3, 7, 9], dur=[1/2, 1, 1/2, 1, 1, 1/2], amp=1.4).every(8, "shuffle")

p4 >> keys(P[0:7], drive=0.4, dur=var([1/4, 1/2], dur=[4, 2]), sus=1/8, amp=0.5).penta().every(8, "shuffle")

p5 >> viola(p3.pitch, dur=[8, 8, 8, 1, 2, 1, 4], amp=1.2)

d1 >> play("XXOX")
d2 >> play("[--]", amp=[1.4, 0.4, 0.7, 0.5])
d3 >> play("^  ^").every(4, "stutter", 4)
