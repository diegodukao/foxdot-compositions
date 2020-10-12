Scale.default = "minor"

var.chords = var([0, -1], [32, 8, 8, 8])

p1 >> karp(P[3, 2, var.chords].loop(4)|P[4, 4, 4, 4].loop(2), dur=1/4, pan=1)
p2 >> karp(P[var.chords, 4, 7].loop(4)|P[2, 2, 2, 2].loop(2), dur=1/4, pan=-1)

b1 >> bass(var.chords, dur=[2, 1/2, 1/2, rest(1), 1/4, 1/2, 1/4, 1/2, rest(1/2), 1/2, 1/2, rest(1/2), 1/4, 1/4], amp=1.2, lpf=500)

b2 >> sawbass(var.chords, dur=8, sus=6, amp=1.7)

d1 >> play('X ')

Group(b_all, d_all).amplify = var([1, 0], [104, 8])

Group(p_all).amplify = var([1,0], [1])

Group(p_all).amplify = 1

Group(b1, d1).solo(0)

p_all.solo()
