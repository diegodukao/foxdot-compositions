Clock.bpm = 100
Scale.default = "minor"
var.chords = var(P[0, 4, 3, 4] + (0, 2, 4, 6), dur=4)

# p1 >> keys(P[0, 4, 3, 4] + (0, 2, 4, 6), dur=4, scale=Scale.minor)

p1 >> keys(var.chords, dur=4)

# b1 >> bass(p1.pitch[0], dur=4, amp=0.5)

b1 >> bass(var.chords[0], dur=[1, 1, 1, 1], amp=0.6)

# chords = var.chords
# print(chords.current_value)
# var.cur_chords = var.chords.current_value
# how to pick random note from a pattern each iteration?
# TODO: try to use Pvar and if it doesn't work, ask at forum
# b1 >> bass(var.cur_chords.sample(1), dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.5)

# None of these worked either
# def pick(pnotes):
#     return pnotes.sample(1)

# b1 >> bass(pick(var.chords.current_value), dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.6)

# b1 >> bass([n for n in var.chords], dur=[1, 1, 1, 1], amp=0.6)

# b1 >> bass(var([n for n in var.chords], dur=1), dur=[1, 1, 1, 1], amp=0.6)

# b1 >> bass(var.chords, dur=1, amp=0.6, oct=6).every(1, 'limit', len, 1)

# b1 >> bass(list(var.chords), dur=1, amp=0.6)

# b1 >> bass(list(var.chords.now()), dur=1, amp=0.6)

b1 >> bass(var.chords[0], dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.6)

# this one worked, but the notes are not randomly picket
b1 >> bass([var.chords[0], var.chords[1], var.chords[2]], dur=[1, 1/4, 1, 1/4, 1/2, 1], amp=0.6)

d1 >> play("XXOX    ")
d3 >> play("    [ X][ X]OX")

d2 >> play("--------")

print(var.chords[:])

print(list(var.chords))

print(var.chords.now())

