"""
    @diegodukao

    http://www.groovemechanics.com/euclid/
"""

p1 >> blip(P[0:8], dur=1/4).shuffle()

p2 >> sawbass(var([0, -1], 8), dur=1)


d1 >> play("X", dur=PDur(3, 8))
d2 >> play("O", dur=PDur(1, 8))
d3 >> play("-", dur=PDur(7, 8))



















# p1 >> pasha(P[0:8], dur=1/4, lpf=2000).shuffle()
# p2 >> bass(var([0, -1], dur=4), dur=PDur(3, 8))
#
# print(SynthDefs)
#
# d1 >> play("X", dur=PDur(3, 8))
# d2 >> play("o", dur=PDur(1, 8))
# d3 >> play("-", dur=PDur(7, 8))
