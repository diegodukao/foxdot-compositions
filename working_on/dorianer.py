Root.default = 'G'
Root.default -= 12
Scale.default = "dorian"

var.roots = var([-3, 0, 1], [16,8,8])

b1 >> sawbass(var.roots, dur=PDur(5,16), cutoff=P[1000,5000][:5], sus=1/2)

b2 >> bass(var.roots, dur=8, amp=0.7).stop()

~p1 >> charm(var.roots + P[0, 4, 3, 4, 2][:6], dur=PDur(3,8)*2, pan=1).penta()
p4 >> charm(var.roots + P[0, 4, 3, 4, 2][:6] - 3, dur=PDur(3,8)*2, amp=1, pan=-1)

p1 >> charm(var.roots + P[0, 4, 3, 4, 2][:6], dur=PDur(3,8), rate=1, pan=1).penta().every(8, "offadd", 4)
p4 >> charm(var.roots + P[0, 4, 3, 4, 2][:6] - 3, dur=PDur(3,8), amp=1, pan=-1)

Group(p1, p4).stop()


print(SynthDefs)

# TODO: add a passing chord
p2 >> piano(var.roots + P(0, 2, 4) + var([0, -5], [30, 2]), dur=[4, 4, 4, 4, 4, 4, 4, 2, 2])

~p3 >> piano(var.roots + P[0, 2, 4, 6, 8][:10].shuffle() - P[5], dur=PDur(5, 8)*2)

p3 >> piano(var.roots + P[0, 2, 4, 6, 8][:10].shuffle() - P[5], dur=PDur(5, 8)*4)

Group(p2, p3, p5).stop()

p_all.solo()

p3.stop()

# TODO: extract these notes to make a solo
# p2 >> blip([0,2,3,P*(4,5)] + var([2,3],16), dur=2*P[4,2,1,1], sus=8, rate=linvar([0,8],100), amp=2, room=1, pan=-0.5).penta()
p5 >> blip([0,2,3,P*(4,5)] + var([-2, 2], 16), dur=2*P[4,2,1,1], sus=8, rate=linvar([0,8],100), amp=2, room=1, pan=-0.5).penta()
d1 >> play("Xs")
liberta()

p5 >> blip([7, 0, 1, P*(2, 3), 2, 4, 5, P*(6, 7)], dur=[8, 4, 2, 2], sus=8).penta()

print(p3.pitch)

d1 >> play("Xs")


def liberta():
    p3.dur = PDur(5,8)*2
    p1.dur = PDur(3,8)
    p4.dur = PDur(3,8)
