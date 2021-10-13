Clock.bpm = 126

l1 >> loop("/home/diego/Projects/music-lc/foxdot-compositions/pybr/2021/samples", dur=[2,2, rest(2),1,1, rest(2),1,1, 4], rate=0.805, amp=0.5, room=0.8)

# volt mix 
d1 >> play("-", dur=1/2)
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4]).stop()
d3 >> play("x", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)])
d4 >> play("o", dur=[rest(1),1])

d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2], pan=-0.8)

Root.default = "E"
Scale.default = "minor"

var.r = var([0,-1], dur=8)

Clock.set_time(-1)

p1 >> piano(var.r + P(0,2,4) -7, dur=8, amp=0.6)

p2 >> piano(var.r + P[0,2,4,6,7,9], dur=PDur(var([5,3,7], dur=[3,2,3]),8)*2, amp=0.6, pan=0.8).shuffle().sometimes("offadd", 3)

b1 >> bass(var.r, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)], sus=1/4)

Group(d1,d2,d3,d4,b1).stop()


s1 >> loop('/home/diego/Projects/music-lc/foxdot-compositions/pybr/2021/samples', sample=0, rate=1, dur=[1,1/2,1]).stop()

s2 >> play('b', sample=[3,4,3,3,4,4,5,6], dur=[1/2], rate=P[1,1,2,2,1,1,2,2]/2, drive=0.2)

d_all.stop()

~s3 >> play('b', sample=[3,4,3,3,4][:8], dur=PDur(3,8), rate=1, drive=0.2).stop()


# planet rock
d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4])

d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.2)

d3 >> play("o", dur=[rest(1), 1])
d4 >> play("x", dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])
d5.stop()

Root.default = "E"
Scale.default = "minor"



var.r = var([0,-1], dur=8)

Clock.set_time(-1)

b1 >> bass(var.r, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])

p1 >> piano(var.r + P(0,2,4), dur=8, amp=0.8)

print(Samples)

Clock.bpm=130

# Tamborzão
d1 >> play("p",sample=1, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,1/2,rest(1/2)])
d2 >> play("p",dur=[1,rest(1)])
d3 >> play("p", sample=6, dur=[rest(2),rest(1/2),1/2,1/2,1/2])
d4 >> play("V", sample=2,dur=[1, rest(3)])
d5 >> play("V", sample=2, dur=[rest(2),rest(1/2),1/2,rest(1/2),1/2], rate=-1)

Clock.bpm=126
# Beatbox do Catra 
f1 >> play("x", dur=[3/4,rest(1/4),rest(1),1/2,1/2,rest(3/4),1/4])
f2 >> play("o", dur=[rest(3/4),1/4,rest(1/2),1/2,rest(1),1])

d_all.stop()

print(Samples)
