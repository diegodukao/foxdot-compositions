Scale.default = "minor"

Clock.bpm = 150

p0 >> bass(var([0, 2], dur=[12, 4]), dur=4)

p1 >> fuzz(p0.pitch + [0, 2, 3, 5], oct=3, dur=1/2, lpf=linvar([1000, 5000], 12)).every(8, "bubble").stop()

p2 >> karp(p0.pitch + [0, 2, 3, 7, 9], dur=[1/2, 1, 1/2, 1, 1, 1/2], amp=1.2).stop()

p3 >> keys(P[0:7], drive=0.5, sus=1/4, amp=0.6, dur=var([1/4, 1/2], dur=[4, 2])).penta().every(4, "shuffle").stop()

p4 >> viola(p2.pitch, dur=[8, 8, 8, 1, 2, 1, 4], amp=1.5).stop()

d1 >> play("---[--]", amp=[1.4, 0.7, 1, 0.6]).every(4, "bubble")
d2 >> play("X([ X][X ])O([X ][ O])")
d3 >> play("^  ^").every(4, "stutter", 4)
d4 >> play(" (x[xx]x) ")
