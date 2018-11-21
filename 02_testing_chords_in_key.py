from FoxDot.lib import Chords

## Playing chords from a key
p1 >> pluck([Chords.I, Chords.IV, Chords.II, Chords.IV], dur=4)

Scale.default = 'minor'
p1 >> pluck([Chords.I, Chords.IV, Chords.II, Chords.IV], dur=4)

Scale.default = 'yu'
p1 >> pluck([Chords.I, Chords.IV, Chords.II, Chords.IV], dur=4)
