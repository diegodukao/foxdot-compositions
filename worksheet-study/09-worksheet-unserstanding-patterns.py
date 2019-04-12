# line 500


print(P[:10:2][:8].rotate(-3))
p1 >> blip(P[:10:2][:8].rotate(-3), dur=PDur(3,8), sus=2, pan=PSine(16).shuffle())

print(PStep(8,[0,3]))
p1 >> blip(PStep(8,[0,3]), dur=PDur(3,8), sus=2, pan=PSine(16).shuffle())

print(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]))
p1 >> blip(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]), dur=PDur(3,8), sus=2, pan=PSine(16).shuffle())

print(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]).rotate())
p1 >> blip(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]).rotate(), dur=PDur(3,8), sus=2, pan=PSine(16).shuffle())

print(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]).rotate() | P[9,11])
p1 >> blip(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]).rotate() | P[9,11], dur=PDur(3,8), sus=2, pan=PSine(16).shuffle())

d1 >> play("Xs")

b1 >> dbass([0, 2, 3, 4], dur=8, amp=0.5)
