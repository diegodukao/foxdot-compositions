# diegodukao

# alo meu povo :))

Scale.default="minor"

var.r = var(P[0,0,-1], dur=8)

# OBRIGADO :))
# Até ano que vem!


Group(d1,d4,d5, d3,v3,v4).solo()

var.r = var(P[-2, -2, 2], dur=8)


d1 >> viola(var.r, dur=8, amp=0.4, drive=0)
d4 >> viola(d1.pitch +2, dur=8, amp=0.4, drive=0)
d5 >> viola(d1.pitch +4, dur=8, amp=0.4, drive=0)

d2 >> pluck(d1.pitch + P(0,2,4,6-7), dur=PDur(3,16)*2, amp=0.07, room=0).stop()

d3 >> keys(P[d1.pitch, 4, 2, 1], dur=PDur(5,8,2)*2, amp=0.8, sus=1/4, pan=1)


# alovictor
# alo alo :D

v1 >> play('v', dur=1, amp=.3)
v2 >> play('{pP}', dur=PDur(5,8), amp=.3, pan=PWhite(-1,1), sample=PRand(3))

v3 >> glass(P[0,2,4], amp=.5, tremolo=2, lpf=sinvar([500,4000],[4,16]))

v4 >> pulse(P[2,3,5,4], scale=Scale.minorPentatonic, oct=5, dur=[1,2,1/2], blur=2, amp=.2, lpf=5000, pan=expvar([-1,1],8)).spread().every(4,'shuffle')

v5 >> sawbass(d1.pitch, dur=PDur(3,7), amp=.3, tremolo=[4,2,1], fmod=sinvar([1,5],8)).spread()

## valeu galeraaa!!!
# fora bolsonaro!!

