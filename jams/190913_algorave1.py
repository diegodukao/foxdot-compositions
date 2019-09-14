Scale.default = "minor"

Clock.bpm=120

b1 >> bass([0, -1, -2, -3], dur=8, amp=0.7)
p1 >> blip(b1.pitch + P[0:7], dur=[1/2, 1, 1/2, 1/2, 1, 1/2]).penta().every(6, "shuffle")
p2 >> keys(b1.pitch + (0, 2, 4), dur=4)
p3 >> piano(b1.pitch + P[0, 3, 5, 7], amp=1.2).every(6, "shuffle").every(4, "offadd", 4)
p4 >> karp(b1.pitch + P[0:7], dur=PDur(5,8)*2, amp=1.2).penta()

Group(p1, p2,).stop()

d1 >> play("XXOX")
d2 >> play("-").every(4, "stutter", 8)
d3 >> play("^  ^").every(4, "stutter", 4)

d_all.stop()
