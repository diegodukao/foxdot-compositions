Scale.default = "minor"

p1 >> bass([0, 4, 6, 3, 2, 1], dur=[4, 4, 4, 2, 1, 1])

p2 >> keys(p1.pitch + (0, 2, 4, 6), dur=p1.dur, amp=1.5)

p3 >> sawbass(p1.pitch + [0, 2, 4, 6], dur=[1/2, 1, 1/4, 1/4, 1/4, 1/2, 1/4], sus=1/4, lpf=2000)

p4 >> prophet(p1.pitch + P[0,8], dur=PDur(3, 8), drive=0.2, sus=1/4).shuffle().penta()

p5 >> pads(p1.pitch + P[0, 2, 4, 6], amp=0.7, sus=1/2, pan=[-1, 0, 1])

p6 >> keys([0, -1], dur)

d1 >> play("X O ")
d2 >> play("----", dur=1/4)



d1.stop()
d2.stop()
d3.stop()



print(SynthDefs)