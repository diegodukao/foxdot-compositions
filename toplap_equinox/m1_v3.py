Scale.default = "minor"
Root.default="e"
Root.default-=12

var.ch = var([0,2,3], dur=[32,4,4])

b1 >> bass(var.ch, dur=[1/2,1/2,rest(1), 1/4,1/4,1/2,1/2,rest(1/2), 1/2], lpf=600, amp=0.8)

p1 >> pulse(var.ch + P[0, 7, 0, 12], dur=[rest(1),1]).every(4,"offadd",4)

p2 >> karp(var.ch + P[0:7].loop(3)|P[0], dur=PDur(5,8), amp=1, oct=5).every(4,"offadd", 4).penta().shuffle().every(8,"shuffle")

print(SynthDefs)

d1 >> play("X X( [X ][ X])")
d2 >> play("[--]")
d3 >> play("  O ")

p_all.stop()

d4 >> play("[ss]", dur=var([1/2,1,1/2],4))
