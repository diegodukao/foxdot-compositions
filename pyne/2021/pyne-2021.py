# FoxDot: Fazendo a pista dançar com Python
# @diegodukao

# linktr.ee/diegodukao

### brega funk ####

Scale.default = "minor"
Clock.bpm = 80

# base
d1 >> play("x.o.o", dur=[1/2, 1/4, 1/4, 1/2, 1/2])
d2 >> play("........xx", dur=[1/2, 1/4, 1/4, 1/2, 1/2])

b1 >> bass([0,0,0,2,4, 0,0,0,1,2], sus=1/4,
    dur=[1/2, rest(1/4), rest(1/4), 1/2, 1/2])
p1 >> keys(P(0,2,4), dur=[rest(1/2), rest(1/4), 1/4, rest(1/2), 1/2],
       oct=6, sus=1/4)

# variacao
d1 >> play("oooo", dur=[1/4, 3/4])
d2 >> play("xxxx", dur=[1/4, 3/4])
p1 >> keys(P(0,2,4), dur=[1/4, 3/4], oct=6, sus=1/4)
b1 >> bass(0, dur=[1/4, 3/4], sus=1/4)
    

################ metal #########
Scale.default = "minor"
Clock.bpm = 120

var.metal = var([2])
~a1 >> play("X XX ", dur=P[1/4,1/4,1/8,1/8,1/4]*var.metal)
~a2 >> play(" O O", dur=P[1/4]*var.metal, amp=0.7)
~a3 >> play(" = =", dur=P[1/4]*var.metal)

c1 >> sawbass([0,0,6,4], dur=[8,8,8,8], oct=4, dist=0.08)

c1 >> sawbass([0,6,0,0,6,0], dur=[8,8,8,8], oct=4, dist=0.08)

p1 >> karp(P(0,4,7) + c1.pitch, dur=1/4, amp=0.8, oct=3, dist=0.05, drive=0.1)




