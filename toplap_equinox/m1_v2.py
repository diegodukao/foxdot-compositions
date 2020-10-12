Scale.default = "minor"

var.ch = var([0, 2, 3], dur=[32,4,4])


b1 >> bass(var.ch, dur=[1/2, 1/2, rest(1)], lpf=600)

b1 >> bass(var.ch, dur=[1/2, 1/2, rest(1), 1/4,1/4,1/2,1/2, rest(1/2), 1/2], lpf=600)


p1 >> karp(var.ch + P[0, 7].loop(3)|P[0], dur=PDur(5,8), amp=0.8).every(4, "offadd", 4).penta().every(8, "shuffle").solo(0)


p1 >> pulse(var.ch + P[0, 7, 0, 12], dur=[rest(1),1]).every(4,"offadd",4)

p2 >> karp(var.ch + P[0:7].loop(3)|P[0], dur=PDur(5,8), amp=1, oct=5).penta().shuffle()

Group(b1, p1, d2).solo()

~d1 >> play('Xs').every([36,4], "trim", 3)

d1 >> play('XX ([X ][ X])')

d2 >> play('[--]')

~d3 >> play('  O( [ O])', amp=0.8).every([36,4], "trim", 3)

d5 >> play("#", dur=40)

d4 >> play("[ss]", dur=var([1/2,1,1/2], 4)).stop()
