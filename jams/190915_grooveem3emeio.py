Root.default = "E"
Root.default -= 7
Scale.default = "minor"

Root.default -= 4

b0 >> bass(dur=4, sus=1/2)
b1 >> bass([0, -1, 2, 3], dur=[1/2, 1, 1, 1], sus=1/2, lpf=1000).every([14, 2], "offadd", -2)

p1 >> karp([0, -1, 2, 3], dur=[1/2, 1, 1, 1], amp=1, sus=1/2).stop()

p2 >> sitar(P[0, -1, 2, 3] -3, dur=[1/2, 1, 1, 1], amp=0.7, sus=1/2).stop()

d1 >> play("x ")
d2 >> play("-- - -[--] --")

