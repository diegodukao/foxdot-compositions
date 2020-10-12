Scale.default = "minor"
Root.default = "E"
Root.default -= 12

var.roots = var([0], dur=[8])

b1 >> bass(var.roots + [0,3], dur=[1.5,2.5], sus=1/2).every(2, "stutter", 2, oct=5, pan=0).every(4, "offadd", 7)

b1.stop()


p2 >> karp(var.roots, dur=PDur(5,8), amplify=1, amp=1.2)

notes = P[0:7][:8].shuffle()

p_all.stop()

p3 >> piano(var.roots + notes, dur=P[1/2,1/2,1/2,1], pan=1).penta().every(4, "offadd", 2)
p4 >> piano(var.roots + notes+ 4, dur=P[1/2,1/2,1/2,1], pan=-1).penta().every(4, "offadd", 2)

Group(p_all).amplify = 1

d_all.amplify = 1

p2.stop()

Group(p2, b0).solo(0)

# ((TT[ T]T)T[ T][TTTT])

d7 >> play("([ss][ssss][ss][ss][ss][ss][ss] )", echo=[0.25, 0])
d8 >> play("(^[^^^^]^[^^])p(PPPp)( [^^][pppp]^){pP}{ppPP pP [pp]P}")

d9 >> play("(t[tt])   ", hpf=2000).stop()

print(Attributes)

