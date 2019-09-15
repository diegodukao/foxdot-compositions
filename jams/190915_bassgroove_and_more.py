Root.default = "E"
Root.default -= 7
Scale.default = "minor"

Root.default += 4

var.roots = var([4, 5, 6], [32, 8, 8])

b0 >> bass(dur=4, sus=1/2)
b1 >> bass([0, -1, var.roots, 1, 2, 1], dur=[1/2, 1, 3/4, 1/4, 1, 1/2], sus=1/4, lpf=1000).every([14, 2], "offadd", -2)
p1 >> karp([0, var.roots], dur=1, chop=4)
p2 >> pads(P(0, var.roots) + var([0, 2], dur=1/2), sus=1/8, dur=[1, 1/2])
p3 >> gong([var.roots, var.roots + 2, var.roots + 4], dur=[4, 2, 2], amp=2).every(4, "offadd", 3)
p4 >> sitar(var.roots + P[0:7], dur=PDur(3,8, [0, 2])*2, amp=0.6).penta().shuffle()
d1 >> play("x ")
d2 >> play("-- - -[--] --")
d3 >> play("^  ^").every(4, "stutter", 4)
d4 >> play("  o ", sample=1)
d5 >> play("#", dur=32)

d1 >> play("x")
d2 >> play("[--]")
d2 >> play("[----]")

Group(p3, p4).solo()

d_all.stop()
d4.stop()

