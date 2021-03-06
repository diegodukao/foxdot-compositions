Scale.default = "minor"
Root.default = "C"

p1 >> sawbass([0, -1], dur=4)

p1 >> sawbass([2, 4], dur=4)

p2 >> keys(p1.pitch + (0, 2, 4), dur=[1, 1/2, 1/2, 1/4])

p3 >> blip(p1.pitch + P[0:7], dur=[rest(1/2), 1, 1/4, 1]).every(3, "offadd", 4)

d1 >> play("x o ")
d2 >> play("---(-[--])")

d1.stop()
d2.stop()

p2.stop()
p3.stop()
p1.stop()


