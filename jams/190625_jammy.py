Scale.default = "blues"
Root.default = "e"

var.roots = var([0], dur=8)

p1 >> pads(var.roots, dur=PDur(3, 7), oct=4)

p2 >> keys(p1.pitch + P[0, 2, 4], dur=[1/2, 1, 1/2, 1, 1/2], pan=0).every(3, "shuffle").every(4, "offadd", 3)

b1 >> sawbass(var(p1.pitch + P[0, -2, -1, 1], dur=[16, 8, 4, 4]), dur=4)

b2 >> bass(b1.pitch + P[0:7], dur=PDur(2, 5), sus=0.2)

d1 >> play('X X(  [ X])')
d2 >> play('  o ')
d3 >> play('-([- ]-)-(-[- ])', dur=1/4)

d1.stop()
d2.stop()
d3.stop()
