Scale.default = "minor"

d1 >> play("x-o(-[-(o[x ])])").every([28, 4], "trim", 3)
d2 >> play("#", dur=32)

p1 >> blip([0, 2, 6, 3], sus=1/2, dur=PDur(3, 8)).every([5, 3], "offadd", 1).every([28, 4], "trim", 3)

print(Samples)

var.roots = var([0, 2, -1, (3, 5)], dur=4)

p2 >> keys(var.roots + P(0, 2, 4), dur=PDur(2,5))

b1 >> sawbass(var(var.roots + P[0, 2, 4], dur=1), dur=PDur(3,5), sus=1/2, amp=0.6)
