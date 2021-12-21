# FoxDot: Fazendo a pista dançar com Python
# @diegodukao

# linktr.ee/diegodukao

Clock.bpm = 80

Scale.default = "minor"

d1 >> loop("blabla.mp3")


for i in range(10):
    d1 >> play("oo", dur=[1/4, 3/4])
    d2 >> play("xx", dur=[1/4, 3/4])
    
d2 >> play("...xx", dur=[1/2, 1/4, 1/4, 1/2, 1/2])
d1 >> play("x.o.o", dur=[1/2, rest(1/4), 1/4, rest(1/2), 1/2])


d2 >> play("...xx", dur=[1/2, 1/4, 1/4, 1/2, 1/2])

d1 >> play("x.o.o", dur=[1/2, rest(1/4), 1/4, rest(1/2), 1/2])
# b1 >> bass([0,0,0,2,4,0,0,0,2,-1], dur=[1/2, rest(1/4), 1/4, rest(1/2), 1/2], sus=1/4)
p1 >> keys(P(0,2,4), dur=[rest(1/2), rest(1/4), 1/4, rest(1/2), 1/2], sus=1/4)

b1 >> bass([0,0,0,2,4,0,0,0,2,-1], dur=[1/2, rest(1/4), rest(1/4), 1/2, 1/2], sus=1/4)

p1 >> keys(P(0,2,4), dur=[1/2, rest(1/4), 1/4, rest(1/2), 1/2], sus=1/4)



d1 >> play("oo", dur=[1/4, 3/4])
d2 >> play("xx", dur=[1/4, 3/4])
p1 >> keys(P(0,2,4), dur=[1/4, 3/4], sus=1/4)
b1 >> bass(dur=[1/4, 3/4], sus=1/4)




print(SynthDefs)
