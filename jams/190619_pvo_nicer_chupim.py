Scale.default = "minor"
Root.default = "C"

p1 >> sawbass([0, -1], dur=4)

p2 >> keys(p1.pitch + (0, 2, 4), dur=PDur(3, 8))

p3 >> blip(p1.pitch + P[0:7], dur=[rest(1/2), 1/4, 1/4, 1/2, 1/2]).penta().shuffle().every(3, "offadd", 4)

d1 >> play("x o ")
d2 >> play("---(-[--])")

p1 >> sawbass(P[-2, -4], dur=4)

# gotten from qirky-05_crazytown
d3 >> play("x-o-x-o-x-o-x-oo(oo)", room=0.8, mix=0.4, amp=[0.7, 0.6, 0.7, 0.8])\
           .every(5, "trim", 2)

# gotten from qirky-05_crazytown
p4 >> pads(p1.pitch + P[0,2,4,6], dur=4, spin=4, oct=4, amp=2.0, chop=[8,16],
           hpf=linvar([500,2000],16), hpr=0.2).every(8, "shuffle")

# gotten from qirky-05_crazytown
p5 >> karp(p1.pitch + P[0,2,4,6,9], dur=[1,2,1.5], amp=0.5, echo=0.75, decay=0.5,
           sustain=0.1).every(8, "shuffle")

d1.stop()
d2.stop()
d3.stop()

p2.stop()
p5.stop()

p3.stop()
p4.stop()
p1.stop()
