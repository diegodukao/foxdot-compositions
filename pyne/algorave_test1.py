Scale.default = "minor"

p0 >> keys([0, -1], dur=8)

p1 >> bass(p0.pitch + [0, 2, 0, 4, 5]).shuffle()

p2 >> pads(p0.pitch + [0, 0, 2, 2, 4], dur=PDur(3, 8), sus=1/4).shuffle().every(4, "offadd", 4)

p3 >> dirt(p0.pitch, amp=0.8, dur=[1/2])

p4 >> keys(p0.pitch + (0, 2, 4))

p5 >> viola(p0.pitch + P[0:8], dur=1/4, room=1, lpf=2000).every(16, "shuffle").every(4, "offadd", 4).penta()

p6 >> pads(p0.pitch, dur=4, oct=4, spin=4, drive=0.4, amp=4, chop=[8,16])

p0 >> keys([1, -3], dur=8)

d1 >> play("XX( o)(X[ X])").every([28, 4], "trim", 3)
d2 >> play("   o").every([12, 4], "trim", 3)
d3 >> play("----").every(4, "stutter", 4)
d4 >> play("  [   ~]  ")
d5 >> play("#", amp=3, dur=32)

p2.stop()
p3.stop()
p4.stop()
p5.stop()


d1.stop()
d2.stop()
d3.stop()
d4.stop()
d5.stop()

print(SynthDefs)