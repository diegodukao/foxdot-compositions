Scale.default = "minor"
Root.default = "A"
Root.default -= 12

d1 >> play("x", dur=[1/2,rest(1),1/2], amp=0.5)
d2 >> play("t", sample=3, dur=PDur(7,16,2)*2, amp=1.2)
d3 >> play("-", amp=[0.8,0.3], pan=-0.8)

var.r = var([0,4], dur=4)
var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
p1 >> piano(var.r + var.f, dur=PDur(7,16,2)*2, amp=0.45, pan=-0.4)
b1 >> bass(
        P[0,4,4,0,   4-7,8-7,13-7,11-7,8-7],
        dur=P[1.5, 0.5, 1, 1,    1, 0.5, 0.5, 1,1],
        sus=P[1.5, 0.5, 1, 1,    1, 0.4, 0.3, 0.9,1],
        lpf=800, amp=0.4)
p2 >> quin(P[7, 9, 11, 6, 8,   -3+7, 6, 8, 10][:11], dur=PDur(var([9,11,7], dur=[6,4,6]),16)*var([2,4], dur=[1.5,0.5]), amp=0.3, pan=0.5, room=1, mix=0.5, sus=p2.dur*0.5)


## hidden
var.r = var([5,3], dur=[4])
var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
b1 >> bass(
    P[5-7,9-7,5-7,9-7,8-7,        3, 1, 2, 3, 2, 1],
    dur=P[1.5,0.5, 0.5, 0.5, 1,   0.75, 0.75, 0.5, 1, 0.5, 0.5],
    sus=P[1.5,0.5, 0.5, 0.5, 1,   0.7, 0.7, 0.4, 1, 0.4, 0.4],
    lpf=800, amp=0.45)
~s1 >> play("#", dur=1, pan=0.6, amplify=var([1,0], dur=[1,2]), room=1, mix=0.5)

s1.stop()

p2 >> quin(P[12, 14, 16-7, 11, 13,   0+7, 9, 11, 13][:11], dur=PDur(var([9,11,7], dur=[6,4,6]),16)*var([2,4], dur=[1.5,0.5]), amp=0.3, pan=0.5, room=1, mix=0.5, sus=p2.dur*0.5)
p2.amplify = var([0,1], dur=[1,1,0.5,1.5])



####################################################

f2 >> play("k", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.04)

f3 >> play("V", sample=0,dur=8, room=1, mix=0.5)
f4 >> play("x", sample=0,dur=8, room=1, mix=0.5)
f5 >> play("X", sample=1,dur=8, room=1, mix=0.5)

~p1 >> pluck(P[0,1,2, 3,4,5, 6,7,4, 2,3,2] -7, dur=PDur(3,8)*2, drive=0.2, amp=0.1, room=1, mix=0.5, pan=0.8).every(4, "stutter", 3)
p1.amplify = 0
~b1 >> jbass(p1.pitch +7, dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8, lpf=73, hpf=0)

d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.1, pan=-0.8)

Group(p1,b1,f3,f4,f5).solo()

Group(p1, b1,f3,f4,f5).solo(-1)
f2 >> play("k", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.04)
d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4])
d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.2, pan=-0.8).stop()
d3 >> play("o", dur=[rest(1), 1])
d4 >> play("x", dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])
~b1 >> jbass(p1.pitch +7, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], amp=0.8, lpf=73, hpf=0)


~p1 >> pluck(P[0,1,2, 3,4,5, 6,7,4, 2,3,2] -7, dur=PDur(3,8)*2, drive=0.2, amp=0.1, room=1, mix=0.5, pan=PWhite(-0.3,0.3)).every(4, "stutter", 3)
p1.amplify = 1


d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.1, pan=-0.8)

d2.stop()

# Beatbox do Catra 

f1 >> play("X", dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8)
~b1 >> jbass(p1.pitch +7, dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8, lpf=73, hpf=0)
d_all.stop()

p1.amplify =0






