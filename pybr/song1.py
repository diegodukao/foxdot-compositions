# Diego Moreira Guimarães
# @diegodukao
# Música com FoxDot - Python Brasil 2019

# synths, roots, oitavas,
# acordes, timevar, escalas

# dó | ré | mi | fá | sol | lá | si
# C  | D  | E  | F  | G   | A  | B

Root.default = 'C'
Scale.default = "major"
Clock.bpm = 120

var.roots = var([0, 2], dur=4)

b1 >> bass(var.roots, dur=[1/2])

p1 >> piano(var.roots + (0, 2, 4), dur=4)

p2 >> karp(var.roots + [0, 2, 4,6], dur=1/4).every(4, "offadd", 4)

p3 >> sitar(var.roots + P[0:7], dur=PDur(5,8))
p4 >> karp(var.roots + P, dur=PDur(3,8))


d1 >> play("X o ")
d2 >> play("----", dur=1/2)

p_all.solo()
























var.roots = var([0, -1], dur=8)

b1 >> bass(var.roots, dur=1/2)
p1 >> piano(var.roots + (0, 2, 4), dur=4)
p2 >> karp(var.roots + [0, 2, 4, 6], dur=1/4).every(4, "offadd", 4)

p3 >> sitar(var.roots + P[0:7][:10], dur=PDur(5,8)).every(4, "stutter", 2).every(16, "shuffle")

d1 >> play("X O ")
d2 >> play("----")

p_all.solo()
