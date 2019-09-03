Scale.default = "minor"

p0 >> bass(var([0,2], dur=[16, 4]), dur=4, amp=0.7)

p1 >> fuzz(p0.pitch + [0, 2, 3, 5], dur=1/2, lpf=linvar([100, 1000], 12)).every(8, "bubble")

p2 >> karp(p0.pitch + [0, 2, 3, 7, 9], dur=[1/2, 1, 1/2, 1, 1, 1/2], amp=1.2)

p3 >> keys(P[0:7], drive=0.5, dur=var([1/4, 1/2], dur=[2, 4]), sus=1/4, amp=0.6).penta().shuffle()





d1 >> play("^  ^").every(4, "stutter", 4)

d2 >> play("X O ").every(2, "bubble")
d3 >> play(" (x[xx]x)  ", lpf=linvar([300, 900], 8), hpr=0.4, spin=4, amp=1.4).stop()

d4 >> play("[--]", amp=[1.4, 0.4, 0.7, 0.5], hpf=linvar([6000, 10000], 8), hpr=0.3, spin=4)

d5 >> play(" [ç ]  ", drive=0.4)