Root.default = "E"
Root.default -= 7
Scale.default = "minor"

Root.default -= 4

b0 >> bass(dur=4, sus=1/2)
b1 >> bass([0, -1, var([2, 4], 32), 1, 2, 1], dur=[1/2, 1, 3/4, 1/4, 1, 1/2], sus=1/4, lpf=1000).every([14, 2], "offadd", -2)

d1 >> play("x ")
d2 >> play("-- - -[--] --")
d3 >> play("^  ^")
d4 >> play("  o ", sample=1)

