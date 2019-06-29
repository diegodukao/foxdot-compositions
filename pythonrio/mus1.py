Root.default = "C"
Scale.default = "minor"

b1 >> sawbass([0, -1], dur=8)

p1 >> keys(b1.pitch + (0, 2, 4), dur=PDur(3,7))

p2 >> blip(b1.pitch + P[0:7], dur=[1/2, 1, 1/2, 1/4, 1/2]).every(3, "offadd", 3)

b1 >> sawbass([-2, -4], dur=8)

p4 >> pads(b1.pitch + [0, 2, 4, 6], dur=4, spin=4, oct=4, amp=2, chop=[8, 16]).every(8, "shuffle")

d1 >> play("X X ")
d2 >> play("  O ")
hh >> play("---(-[--])")


b1.stop()
p1.stop()
p2.stop()

d1.stop()
d2.stop()
hh.stop()
