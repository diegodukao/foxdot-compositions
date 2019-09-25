Clock.bpm = 100

Scale.default = "minor"
Root.default = "g"

var.chords = var([0, 2], [32, 8, 8, 8])

b1 >> bass(var.chords + [0, 2, 4], dur=[1, 1/2, 1/2], oct=4)

p1 >> keys(var.chords + (0, 2, 4), dur=[rest(3), 1/2, 1/2], sus=1/2)

p2 >> karp(var.chords + P[0:7], scale=Scale.minor, dur=PDur(5, 8)*2).penta().shuffle()
