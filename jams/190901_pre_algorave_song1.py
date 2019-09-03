Scale.default = "minor"

p0 >> bass(var([0, 2], dur=[16, 4]), dur=4, amp=0.7)

p1 >> fuzz(p0.pitch + [0, 2, 3, 5], dur=1/2, lpf=linvar([100, 1000], 12)).every(8, "bubble").stop()

p2 >> karp(p0.pitch + [0, 2, 3, 7, 9], dur=[1/2,1,1/2,1,1,1/2]).stop()

p4 >> keys(P[0:7], drive=0.5, dur=var([1/4, 1/2], dur=[4, 2]), sus=1/4).penta().shuffle().stop()

p5 >> viola(p4.pitch, dur=[8, 8, 8, 1, 2, 1, 4], amp=2)

d1 >> play("[==]= = = ", amp=var([0.5, 1.4, 1.2], [6, 2]), hpf=linvar(100, 5000), hpr=0.8, spin=4, drive=0.4)

d2 >> play("^ ", dur=[1/2, 1, 1, 1/4, 1/4], drive=0.8, lpf=linvar([0, 440], 16), lpr=0.3)
d3 >> play("X ")
d4 >> play("[--]", amp=[1.3, 0.6, 0.6, 1.4], hpf=linvar([100, 1000], 12)).every(16, "bubble", 2)
d5 >> play(" t t").every(16, "stutter", 4)
d6 >> play("(o[ooo]oo) (o ) ", amp=0.7, hpf=linvar([700, 2000], 12), hpr=0.8)
d7 >> play("X OX")
a1.stop()

d8 >> play("g", amp=[1.4, 1.4, 0.5]).stop()
d9 >> play("T", dur=[1, 1, 1/2], amp=[0.4, 0.3, 1.8]).stop()

a1 >> play("^", dur=var([1/4, 1/4, 1/4, 1/2, 1/2, 1/4], [6, 2]), lpf=linvar([300, 1000], 12), lp4=0.4)

d1.stop()

d2.stop()

d3.stop()

d4.stop()

d5.stop()
d6.stop()
d7.stop()
a1.stop()