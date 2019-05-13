Clock.bpm = 100
Scale.default = "minor"

# v1 - using the chords as values of the TimeVar
var.chords = var(P[0, 4, 3, 4] + (0, 2, 4, 6), dur=4)

p1 >> keys(var.chords, dur=4)

b1 >> bass(var.chords[0], dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.7)

# bass notes varying, but couldn't find a way to pick them randomly
b1 >> bass([var.chords[0], var.chords[1], var.chords[2]], dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.7)


# v2 - using the only the roots for the TimeVar and adding the other notes directly 
# to the players
var.chords = var(P[0, 4, 3, 4], dur=4)

p1 >> keys(var.chords, dur=4) + (0, 2, 4, 6)

b1 >> bass(var.chords + P[0, 2, 4, 6], dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.7)

b1 >> bass(var.chords + P[0, 2, 4, 6], dur=PDur(3, 8), amp=0.7)

b1 >> bass(var.chords + P[0, 2, 4, 6].shuffle(), dur=PDur(3, 8), amp=0.7)

# bass notes picked ramdonly, but since the TimeVar only contain the roots, we need to
# manually add the other notes to every player. it would be much better if we use the full
# chord as TimeVar and just pick the notes from it.
b1 >> bass(var.chords + P[0, 2, 4, 6].sample(3), dur=PDur(3, 8), amp=0.7)

########

d1 >> play("XXOX    ")
d3 >> play("    [ X][ X]OX")

d2 >> play("--------")

