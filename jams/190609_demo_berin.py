Scale.default = "minor"
Root.default = "d"


var.roots = var([0, 5, 2], dur=8)

p1 >> keys(var.roots, sus=1, dur=PDur(2, 7|3)) + (0, 2, 4)

b2 >> sawbass(var.roots, dur=2).every(5, "stutter", 4).every(3, "offadd", 4)

p3 >> blip(var.roots + P[0:7], sus=1/2, dur=[rest(1/2), 1/2, 1/4, 1/2]).every(2, "offadd", 5).every(2, "shuffle")

p4 >> blip().every([6, 2], "offadd", 4)
    
d1 >> play("X o ")
d2 >> play("---(-[--])")

d1.stop()
d2.stop()

p1.stop()
b2.stop()
p3.stop()
