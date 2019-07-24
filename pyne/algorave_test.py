b1 >> bass([0, 4], oct=5, dur=[1, 1/2])

b1 >> sawbass([1, 3], oct=5, dur=[1, 1/2])


k1 >> keys(b1.pitch + (0, 2, 4), amp=0.7, pan[-1, 0, 1])

k2 >> dirt(b1.pitch, amp=0.7, dur=1/4)

k3 >> pads(b1.pitch + [0, 2, 4, 6, 4, 6, 0], dur=[1/2, 1/4, 1/4], amp=0.5)

p2 >> pads(b1.pitch + [0, -1], dur=8)

d1 >> play("--o( [oo])--", dur=1/2).every(4, "stutter", 4)
d2 >> play("[ ^]^")
d3 >> play("x  x   (x[ x])")


p1 >> prophet(b1.pitch + [0, 2, 4, 6], sus=1/2, room=1).shuffle().every(4, "offadd", 4)

p4 >> pads(p1.pitch + [0, 2, 4, 6], dur=4, spin=4, oct=4, amp=4, chop=[8, 16])


p1 >> keys([0, 4, 6, 3, 2, 1], dur=[4, 4, 4, 2, 1, 1])

p2 >> keys(p1.pitch + (0, 2, 4))


p1.stop()
p2.stop()
k1.stop()
k3.stop()
k2.stop()
b1.stop()