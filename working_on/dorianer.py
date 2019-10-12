Root.default = 'G'
Root.default -= 12
Scale.default = "dorian"

var.roots = var([-3, 0, 1], [16,8,8])

b1 >> sawbass(var.roots, dur=PDur(5,16), cutoff=P[1000,5000][:5], sus=1/2)

b2 >> bass(var.roots, dur=8, amp=0.7).stop()

# p1 >> karp(var.roots + P[0, 4, 3, 4, 2], dur=PDur(3,8)*2).penta()
p1 >> charm(var.roots + P[0, 4, 3, 4, 2][:6], dur=PDur(3,8), rate=1, pan=1).penta().every(8, "offadd", 4)
p4 >> charm(var.roots + P[0, 4, 3, 4, 2][:6] - 3, dur=PDur(3,8), amp=1, pan=-1)

print(SynthDefs)

# TODO: add a passing chord
p2 >> piano(var.roots + (0, 2, 4), dur=4)

p_all.solo()

p3.stop()

# TODO: extract these notes to make a solo
# p2 >> blip([0,2,3,P*(4,5)] + var([2,3],16), dur=2*P[4,2,1,1], sus=8, rate=linvar([0,8],100), amp=2, room=1, pan=-0.5).penta()
p3 >> blip([0,2,3,P*(4,5)] + var([-2, 2], 16), dur=2*P[4,2,1,1], sus=8, rate=linvar([0,8],100), amp=2, room=1, pan=-0.5).penta()
d1 >> play("xs")
