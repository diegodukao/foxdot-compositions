d1 >> play("x(x )[ x] x[ x][ x]( x)", dur=1, amp=1)

d2 >> play("-------(-[---])", dur=1/2, pan=-0.6, amp=P[0.8,0.6,0.6,0.4])

d3 >> donk(P[0,0,0,2], dur=PDur(5,8)*2, amp=0.3, pan=0.6)

Scale.default = "minor"

d0 >> play("  o( (x[ x]))", amp=0.5)

Group(d2,d0,v4,v3).solo(0)

v2.sus = v2.dur * 0.6

~d5 >> pluck(d4.pitch + 2, dur=d4.dur, pan=1, sus=d4.sus, amp=d4.amp, drive=d4.drive, room=1, mix=0.4, amplify=d4.amplify)
~d4 >> pluck(v1.pitch[0] + P[0,-2,-1,2], dur=PDur(3,8)*2, sus=4, amp=0.02, pan=-1, room=1, mix=0.4, amplify=var([1, 0], dur=[1]), drive=0.2).every(6, "offadd", 3)

# foda :)

~d6 >> bass(
  P[v1.pitch[0],v1.pitch[3]-7,v1.pitch[2]-7,v1.pitch[2]-7,v1.pitch[3]-7,
    v1.pitch[2]-7], dur=P[1.5,1,0.5]*2, amp=0.5, sus=d5.dur*0.7)

print(SynthDefs)


# oie

Scale.default='minorPentatonic'

v1 >> keys([(0,2,4,6), (0,2,3,5), (0,1,5,7)],echo=2, tremolo=4, sus=sinvar([0.2, 2], 16), amp=.6, room=2, dur=4, lpf=linvar([500,4000], [16,32])).spread()

v2 >> sawbass(P[:8], dur=PDur(5,8),oct=(4,5), amp=.1, pan=PWhite(-1,1)).every(4, 'shuffle').every(2, 'palindrome')

v3 >> prophet(d4.pitch + (0,2,4,6), amp=.2, dur=PRand(2,8) + [1/2,1/4,1/4,1/2], oct=5, tremolo=[2,4], coarse=[2,4,8], sus=linvar([1/2,2],4), hpf=linvar([500,4000],32))

v4 >> pulse(P[0,2,4] + P[6,3,2,1], dur=1/4, sus=.05, amp=.5, lpf=sinvar([1000,7000], 8)).every(4,'shuffle')

Group(d0, v4).solo(0)


