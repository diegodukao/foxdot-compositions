Scale.default = "minor"
Clock.bpm = 150

p1 >> sawbass([0, -2, -1, 1], dur=8, sus=7, amp=1)

p2 >> karp(p1.pitch + [0, 2, 4])

p3 >> keys(p1.pitch + P[0:8], dur=PDur(3, 8), amp=2, drive=1, sus=1/4).shuffle().penta()

p4 >> bass(p1.pitch + [0, 2, 4], dur=PDur(3, 8), sus=1/4)

print(SynthDefs)

p4.stop()
p2.stop()
p3.stop()

d1 >> play("X O( [ X])").stop()
d2 >> play("----", dur=1/2).every(4, "stutter", 8).stop()
d3 >> play("[^^]  ( [~~]) ").stop()
d4 >> play("Xx  (X )  ").stop()
d5 >> play("!       ", amp=2, room=1).every(8, "stutter", 1).stop()
d6 >> play("     2  ").stop().stop()
d7 >> play(" [xx]    [xx] X o", room=3).stop()
d8 >> play("  o  o  ", room=3).stop()
d9 >> play("#", dur=32, amp=6).stop()

d1 >> play("X   (X[XX])   ")
d2 >> play("  [oo]  o  ", amp=0.8)
d3 >> play(" - -  --").every(4, 'stutter', 8)
d4 >> play("^  ^   ^")
d5 >> play("      [~ ] ")
d6 >> play("X X ")

print(SynthDefs)