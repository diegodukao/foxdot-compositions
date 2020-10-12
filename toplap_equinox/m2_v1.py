Scale.default = "dorian"
Root.default = "E"
Root.default -= 12

var.ch = var([0, -1, 3, -1, 0], dur=[4, 4, 3, 1, 4])

p1 >> piano(var.ch + P(0, 2, 4), dur=PDur(3,8)*2, amp=0.8)

p2 >> gong(var.ch + P[0:7], dur=1/2, amp=1.2).penta().shuffle().every(4, "stutter", 3, pan=[-1,1]).every(4, "offadd", 3)

~p3 >> sitar(var.ch + P[0, 2, 4, 6, 7], dur=PDur(5,8)*2, amp=0.8, pan=[-1]).shuffle().every([8], "offadd", 3)
~p4 >> sitar(var.ch + P[0, 2, 4, 6, 7] + 3, dur=PDur(5,8)*2, amp=0.8, pan=[1]).shuffle().every([8], "offadd", 3)


b1 >> bass(var.ch + P[0].loop(3)|P[3], dur=PDur(5,8))

b1 >> bass(var.ch, dur=[4], lpf=300)

Group(p1, p2, b1).amplify = var([1], dur=[16,4])

Group(p3, p4).stop()

d1 >> play('XXOX')
d2 >> play('---(---[--])', dur=1/4)

Group(p2, d2).solo()

p1.stop()
p2.stop()

Group(p2, d2).solo()
