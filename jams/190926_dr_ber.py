Scale.default = "minor"

var.chords = var([0, 3], dur=[24, 8, 8, 8])

# p1 >> sitar(var(P[0:7][:14], dur=1/2), dur=(1/2 | P[1/4].stutter(12) | 1/2 ), oct=5).shuffle().stop()

b1 >> bass(var.chords + [0, 4, 2], dur=[1.5, 0.5, 2], sus=1/4, oct=5).often("stutter", 2)
p2 >> keys(var.chords + (0, 2, 4), dur=8)
p3 >> piano(var.chords + [0, 4, 3, 2], dur=PDur(4, 7)*2, amp=1).often("stutter", 2).every(8, "offadd", 3)
Clock.bpm = 120
d1 >> play("X ")
d2 >> play("([--]-)([- - - - ]  [--------])", dur=1)
d3 >> play(" v", dur=4).every(6, "stutter", 4)
d4 >> play(" (  (e[ee]) )", dur=1/2)
d5 >> play("(x )( x)o ", dur=1/2)
