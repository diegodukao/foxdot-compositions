Clock.bpm = 100

var.chords = var(P[0, 4, 3, 4] + (0, 2, 4, 6), dur=4)

# p1 >> keys(P[0, 4, 3, 4] + (0, 2, 4, 6), dur=4, scale=Scale.minor)

Scale.default = "minor"

p1 >> keys(var.chords, dur=4)

print(p1.pitch)

# b1 >> bass(p1.pitch[0], dur=4, amp=0.5)

b1 >> bass(var.chords[0], dur=[1, 1, 1, 1], amp=0.5)

# chords = var.chords
# print(chords.current_value)
# chords = var.chords.current_value
# how to pick random note from a pattern each iteration?
# TODO: try to use Pvar and if it doesn't work, ask at forum
# b1 >> bass(chords.sample(1), dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.5)

b1 >> bass(var.chords[0], dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.5)

d1 >> play("XXOX    ")

d3 >> play("    [ X][ X]OX")

d2 >> play("--------")
