Root.default = "A"
Root.default -= 12

Scale.default = "minor"

var.roots = var([0, 4], dur=16)

Clock.bpm = 110

# b1 >> bass(var.roots, dur=4, sus=2)
b1 >> bass(var.roots, dur=[1/2, 1, rest(2.5)], sus=1/2)

p1 >> piano(var.roots + P(0,2,4), dur=2).offbeat(2)

d1 >> play(" x  ", dur=1, amp=3)
d2 >> play(" o  ", dur=1)
d3 >> play("--", dur=[2/3, 1/3], amp=[1, 0.7])
