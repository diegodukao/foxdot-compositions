from FoxDot.lib import Chords

## Playing chords from a key
# p1 >> pluck([Chords.I, Chords.IV, Chords.II, Chords.IV], dur=4)

# Scale.default = 'minor'
# p1 >> pluck([Chords.I, Chords.IV, Chords.II, Chords.IV], dur=4)

# Scale.default = 'yu'
# p1 >> pluck([Chords.I, Chords.IV, Chords.II, Chords.IV], dur=4)

# Scale.default = 'minor'
# p1 >> pluck(P[Chords.I, Chords.IV, Chords.II, Chords.IV].stutter(2), dur=2)

Scale.default = 'major'
Root.default = 'D'
# p1 >> pluck(P[Chords.VI, Chords.IV, Chords.I, Chords.V], dur=5)
p1 >> pluck(P[Chords.VI, Chords.IV, Chords.I, Chords.V].stutter(2), dur=2)
