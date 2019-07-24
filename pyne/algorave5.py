Scale.default = "minor"
Clock.bpm = 150

p1 >> sawbass([0, -2], dur=8, sus=7, amp=2)

p2 >> blip(p1.pitch + [0, 2, 4, 6], drive=0.4, room=1)

p3 >> pads(p1.pitch, dur=4, spin=4, oct=4, amp=8, chop=[8, 16], drive=10)

p4 >> prophet(p1.pitch + P[0:8], dur=PDur(3, 8), sus=1/4, amp=5, drive=0.2).penta().shuffle()


d1 >> play("X O( [ X])").stop()
d2 >> play("----", dur=1/2).every(4, "stutter", 8)
d3 >> play("[^^]  ( [~~]) ").stop()
d4 >> play("[ x]").stop()
d5 >> play("!       ").stop()
d6 >> play("     2  ").stop()
d7 >> play(" [xx]    [xx] X o").stop()
d8 >> play("  o  o  ").stop()
d9 >> play("#", dur=32, amp=6).stop()




print(SynthDefs)