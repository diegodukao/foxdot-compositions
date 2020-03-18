Scale.default = "minor"

var.chords = var([0, 2, 3], dur=[32, 4, 4])

b1 >> bass(var.chords, dur=[1/2, 1/2, rest(1)], lpf=600, amp=0.8)

b1 >> bass(var.chords, dur=[1/2, 1/2, rest(1), 1/4,1/4,1/2,1/2, rest(1/2), 1/2], lpf=600, amp=0.8)

b1 >> bass(var.chords, dur=[1/2, 1/2, rest(1), 1/4,1/4,1/2,1/2, rest(1/2), 1/2], lpf=600, amp=0.8, oct=P[5].loop(3)|P[6])


p1 >> karp(var.chords + P[0, 7, 0, 12], dur=[rest(1), 1]).every(4, "offadd", 4).stop()

p1 >> karp(var.chords + P[0,7].loop(3)|P[0].loop(1), dur=PDur(5,8), amp=0.8).penta().shuffle()

d1 >> play('  o ')
d3 >> play('xs')
d2 >> play('[--]')

d4 >> play("[ss]", dur=var([1/2, 1, 1/2], 4))

d5 >> play("+", dur=var([4, 1/4, 4, 1/2], 4), lpf=0).every(16, "stutter", 4)
