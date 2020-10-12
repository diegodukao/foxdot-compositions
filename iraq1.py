Scale.default = "minor"

var.roots = var([0])

b1 >> bass(var.roots, dur=8)

p1 >> fuzz(var.roots + [0,2,3,5],oct=4, dur=1/2, lpf=linvar([300, 2000], 12)).every(8, "bubble").stop()

p2 >> karp(var.roots + [0,2,3,7,9], dur=[.5,1,.5,1,1,.5], amp=0.6).stop()

p3 >> keys(P[0:7], drive=0.1, dur=var(P[.25,.5], dur=[2,4]), sus=1/4, amp=1).penta().shuffle().stop()

p4 >> viola(p2.pitch, dur=[8, 8, 1, 2, 1, 4]).stop()


d1 >> play("Xs").every(4, 'stutter', 2).stop()
d2 >> play("-", amp=0.9, hpf=linvar([500, 4000], 16), hpr=0.7).every(8, 'bubble', 4).every(3, 'stutter', 4)
d3 >> play("VV", room=1, dur=8, amp=0.6)
d5 >> play("X O ").stop()

d6 >> play("T[tt]")

