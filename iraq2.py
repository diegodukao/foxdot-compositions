Scale.default = "minor"

var.roots = var([0, 2], [32, 8, 8, 8])

b1 >> bass(var.roots + [0,2,4], dur=[1,1/2,1/2], sus=1/2, amp=0.7)

p1 >> piano(var.roots + (0, 2, 4), dur=[rest(3), 1/2, 1/2], sus=1/2, amp=0.6)

p2 >> karp(var.roots + P[0:7], dur=PDur(5,8)*2, amp=1.2).penta().shuffle()


d6 >> play("((TT[ T]T)T[ T][TTTT])[tt]")
d7 >> play("^", dur=1)
d8 >> play("  (e[ee] [eeee][ee ee e ](e[eeee]ee)) ", dur=1, lpf=600, drive=0.1, echo=[0, 0.25, 0, 0.5], amp=1.2)
d9 >> play("  o ")

