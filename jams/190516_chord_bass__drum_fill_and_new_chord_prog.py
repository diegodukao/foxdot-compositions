Clock.bpm = 120
Scale.default = "minor"
var.chords = var(P[2, 0, 5, 4], dur=4)

p1 >> keys(var.chords, dur=4) + (0, 2, 4, 6)

b1 >> bass(var.chords + P[0, 2, 4, 6], dur=PDur(3, 8), amp=0.7)

p2 >> blip(var.chords + P[0, 2, 4, 6], dur=PDur(7, 8, 1)).every(3, "shuffle")

########

d3 >> play("XXOX[ X][ X]OX").every([28, 4], "trim", 3)
d2 >> play("--------")
c1 >> play("#", dur=32, room=1, amp=2).spread()

var.chords = var(P[3, 4, 2, 3], dur=4)

var.chords = var(P[0, 2, 5, 4], dur=4)
