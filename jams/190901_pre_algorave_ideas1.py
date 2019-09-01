# heavily based on reference 09-qirky-driving_force.py

Scale.default = "minor"

p0 >> bass([0, 2], dur=8, amp=0.7)

b0 >> bass([0, 3, 6, 3, 4], sus=1/4, amp=0.6, dur=[rest(10), 1/4, 1/2, 1/2, 1/4, 1/2, 1/4, 1/2, 1/4]).every(8, "shuffle")

b1 >> fuzz([0, 2, 3, 5], dur=1/2, lpf=linvar([100, 1000], 12), lpr=0.3, oct=3).every(16, "shuffle").every(8, "bubble", 4)

p2 >> karp([0, 2, 3, 7, 9], dur=[1/2, 1, 1/2, 1, 1, 1/2]).every(12, "shuffle").every(5, "bubble")


d1 >> play("XXoX").stop()


d1 >> play("[--]", dur=1/2, amp=[1.3, 0.5, 0.8, 0.5], hpf=linvar([6000, 10000], 16), hpr=0.4, spin=2).every([16, 4], "bubble").stop()

d2  >> play("=", dur=[1/2, 1/4, 1/4, 1/2], sus=1/2, amp=[1.3, 0.4, 0.4, 1.3, 0.4, 1.3]).every([16, 4], "bubble").stop()

d3 >> play(" t")

d4 >> play("T ", dur=1/2, amp=[1.2, 0.6, 0.4, 1.2], spin=2).every([12, 4], "bubble").stop()

d5 >> play("    [tt] [tt] ")

d4 >> play("XXOX").stop()


p1.every(2, "stutter", 4).stop()

b1.every(8, "rotate").stop()
