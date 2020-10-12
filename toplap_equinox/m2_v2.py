Scale.default = "dorian"
Root.default = "e"
Root.default -= 12


var.ch = var([0, -1, 3, -1, 0], dur=[4, 4, 3, 1, 4])


b1 >> bass(var.ch, dur=[4], lpf=300, amp=0.8)

p1 >> piano(var.ch + P(0,2,4), dur=PDur(3,8)*2, amp=0.8)
p2 >> gong(var.ch + P[0:7], dur=1/2, amp=1.2).penta().shuffle().every(4, "stutter", 3, pan=[-1,1]).every(4, "offadd", 3)

p3 >> sitar(var.ch + P[0,2,4,6,7], dur=PDur(5,8)*2, pan=-1, amp=0.8).shuffle().every(8, "offadd", 3)
p4 >> sitar(var.ch + P[0,2,4,6,7] + 3, dur=PDur(5,8)*2, pan=1, amp=0.8).shuffle().every(8, "offadd", 3)



d1 >> play('XXO(X[ X])')
d2 >> play('- -- - -- ', dur=1/4).every(8, "stutter", 4)

b1 >> bass(var.ch + P[0].loop(3)|P[3], dur=PDur(5,8), amp=1)
Group(p3,p4,p1,p2).stop()




























Scale.default = "dorian"
Root.default = "e"
Root.default -= 12



var.ch = var([0, -1, 3, -1, 0], dur=[4, 4, 3, 1, 4])

b1 >> bass(var.ch, dur=[4], lpf=600, amp=0.8)

p1 >> piano(var.ch + P(0,2,4), dur=PDur(3,8)*2, amp=0.8).stop()
p2 >> gong(var.ch + P[0:7], dur=1/2, amp=1.2).penta().shuffle().every(4, "stutter", 3, pan=[-1,1]).every(4, "offadd", 3)

p3 >> sitar(var.ch + P[0,2,4,6,7], dur=PDur(5,8)*2, pan=-1, amp=0.8).shuffle().every(8, "offadd", 3).stop()
p4 >> sitar(var.ch + P[0,2,4,6,7] + 3, dur=PDur(5,8)*2, pan=1, amp=0.8).shuffle().every(8, "offadd", 3).stop()

p5 >> pads(var.ch, dur=[4,4,3,1,4], chop=[20,10], amp=1, drive=0.2).stop()

b1 >> bass(var.ch + P[0].loop(3)|P[3], dur=PDur(5,8))
d1 >> play('X X([X ][ X])')
d2 >> play('[--]').every(4, "stutter", 8)
d3 >> play('  O ', amp=0.8).stop()
