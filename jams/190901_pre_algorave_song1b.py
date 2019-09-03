Scale.default = "minor"

p0 >> bass(var([0,2], dur=[16, 4]), dur=4, amp=0.7).stop()

p1 >> fuzz(p0.pitch + [0, 2, 3, 5], dur=1/2, lpf=linvar([100, 1000], 12)).every(8, "bubble").stop()

p2 >> karp(p0.pitch + [0, 2, 3, 7, 9], dur=[1/2, 1, 1/2, 1, 1, 1/2], amp=1.2).stop()

p3 >> keys(P[0:7], drive=0.5, dur=var([1/4, 1/2], dur=[4, 2]), sus=1/4, amp=0.6).penta().shuffle()

p4 >> viola(p3.pitch, dur=[8 ,8 ,8, 1, 2, 1, 4], amp=1.8)




d1 >> play("^  ^").every(4, "stutter", 4)
d2 >> play("X O ").every(2, "bubble")
d3 >> play(" (x[xx]x)  ", lpf=linvar([300, 900], 8), hpr=0.4, spin=4, amp=1.4)
d4 >> play("[--]", amp=[1.4, 0.4, 0.7, 0.5], hpf=linvar([6000, 10000], 8), hpr=0.3, spin=4).every(4, "bubble")
d5 >> play(" ([~~] [~~] )  ", drive=0.4)
d6 >> play("  (o[oo] o) ")


d1.stop()
d2.stop()
d3.stop()
d5.stop()
d4.stop()
d6.stop()