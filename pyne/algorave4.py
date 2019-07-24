Scale.default = "minor"
Clock.bpm = 150

p1 >> sawbass([0, -2], dur=8, sus=7, amp=2)

p2 >> blip(p1.pitch + [0, 2, 4, 6], drive=0.4, room=1)

p3 >> pads(p1.pitch, dur=4, spin=4, oct=4, amp=5, chop=[8, 16], drive=5)


d1 >> play("X O( [ X])")
d2 >> play("----", dur=1/2).every(4, "stutter", 8)
d3 >> play("[^^]  ( [~~]) ")
d4 >> play("[ x]")
d5 >> play("!       ")
d6 >> play("     2  ")
d7 >> play(" [xx]    [xx] X o")

d8 >> play("  o  o  ")

d2.stop()
d4.stop()
d6.stop()
d5.stop()


print(SynthDefs)