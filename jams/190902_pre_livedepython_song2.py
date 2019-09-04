Scale.default = "minor"

p1 >> sawbass([0, -1, 1, -2], dur=4)

p2 >> keys(p1.pitch + (0, 2, 4), dur=PDur(3, 8))

d3 >> blip(p1.pitch + P[0:7], dur=[rest(1/2), 1/4, 1/4, 1/2, 1/2]).penta().shuffle()

p4 >> karp(p1.pitch + [0, 2, 4, 6], dur=PDur(5, 8), sus=1/2).every(4, "offadd", 4).every(4, "shuffle")

p5 >> pads(p4.pitch, dur=4, oct=5, amp=1.2, chop=[8, 16])

d1 >> play("x o ")
d2 >> play("----")


