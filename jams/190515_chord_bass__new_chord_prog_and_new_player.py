Clock.bpm = 120
Scale.default = "minor"

# v2 - using the only the roots for the TimeVar and adding the other notes directly 
# to the players
var.chords = var(P[0, 4, 3, 4], dur=4)

p1 >> keys(var.chords, dur=4) + (0, 2, 4, 6)

b1 >> bass(var.chords + P[0, 2, 4, 6], dur=PDur(3, 8), amp=0.7)

# b1 >> bass(var.chords + P[0, 2, 4, 6].shuffle(), dur=PDur(3, 8), amp=0.7)

# b1 >> bass(var.chords + P[0, 2, 4, 6].sample(3), dur=PDur(3, 8), amp=0.7)

p2 >> blip(var.chords + P[0, 2, 4, 6], dur=PDur(7, 8, 1)).every(3, "shuffle")

########

d1 >> play("XXOX    ")
d3 >> play("    [ X][ X]OX")
d2 >> play("--------")


var.chords = var(P[5, 4, 6, 5], dur=4)
