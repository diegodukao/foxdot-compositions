b1 >> sawbass(var([0,1,-2],[8,8,16]), dur=PDur(5,16), cutoff=P[1000,5000][:5], sus=1/2)

# p2 >> blip([0,2,3,P*(4,5)] + var([2,3],16), dur=2*P[4,2,1,1], sus=8, rate=linvar([0,8],100), amp=2, room=1, pan=-0.5).penta()
p2 >> blip([0,2,3,P*(4,5)] + var([-2, 2], 16), dur=2*P[4,2,1,1], sus=8, rate=linvar([0,8],100), amp=2, room=1, pan=-0.5).penta()
