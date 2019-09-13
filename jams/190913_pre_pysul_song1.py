# https://www.youtube.com/watch?v=No-bBhbJAac

Scale.default="minor"

Clock.bpm = 120

p1 >> blip(P[0:7], dur=[1/4], sus=1/4).shuffle()

b1 >> sawbass([0, -1], dur=8, amp=0.8)

p2 >> piano(b1.pitch + (0, 2, 4), amp=0.6, dur=PDur(3,8))

p3 >> karp([b1.pitch, 3, 4, 6], dur=PDur(5,8,[0,2])*2, sus=1/2).every(4, "offadd", 4)

p4 >> pads(b1.pitch, dur=4, sus=4, chop=[8, 16], amp=2).penta().shuffle()

p5 >> sitar(b1.pitch + P[0:7], dur=PDur(3,8,[0,2])).penta().every(16, "shuffle").every(4, "offadd", 4).every(6, "stutter", 4, dur=3, pan=[-1, 1], room=1)

Group(b1, p5).solo()

d1 >> play("X XX")

d2 >> play("[--]")
d3 >> play("  o ")

d_all.stop()
