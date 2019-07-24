Scale.default = "minor"
Root.default = "e"
Clock.bpm = 120

p1 >> sawbass([0, -1], dur=8)

var.roots = var([0, 3, 2, 1], dur=[8, 4, 2, 2])

p1 >> keys(var.roots, dur=PDur(3, 8)) + (0, 2, 4)

p1 >> sawbass([1, -3], dur=8)

p2 >> keys(p1.pitch + (0, 2, 4), dur=PDur(3, 8))

p3 >> prophet(p1.pitch + P[0:6], dur=PDur(3, 8), amp=2).every(1, "shuffle")

d8 >> play("X ", amp=2)


d7 >> play("!#O", dur=4, amp=3)
d9 >> play("X- -XO", dur=1/2, amp=0.75).every(2, "stutter", 16)
p9 >> pads([0, 2, 4, 5], dur=[1, 1/2, 1/4, 1], tremolo=4, fmod=3, amp=0.8).every(4, "offadd", 4).shuffle()


d7 >> play("#", dur=32, amp=3)



d1 >> play("o  oo    (o[oo])   o  ", amp=2).stop()
d2 >> play(" oo  oooo ooo oo", amp=0.8).stop()

d3 >> play("X       xX  xX  ", amp=4)

d4 >> play("T   T   T   T   ", amp=3, room=2).stop()

d5 >> play("  T   T  T T  T ", amp=1).stop

d6 >> play("(MM[MMM]) (m[ eee]) ", PDur=(3, 8))



d7 >> play(" T T T")
d8 >> play("T T   ")  


print(Samples)
