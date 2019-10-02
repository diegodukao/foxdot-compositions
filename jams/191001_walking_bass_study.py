Scale.default = "minor"

var.chords = var([0, 0, 4, 4, 0, 3, 4, 0], dur=4)

b1 >> bass(
    [
        var.chords + 0,
        (var.chords + P[2, 4, 6].shuffle()) % 7,
        (var.chords + P[0, 2, 4, 6, 8].shuffle()) % 7,
        (var.chords[var.chords.now() + 1] + P[-2, -1, 1, 2].shuffle()) % 7,
    ]
)

p1 >> piano(var.chords + (0, 2, 4), dur=PDur(3, 8, 2)*2, amp=0.7)
    
d1 >> play("-", dur=[1, 0.7, 0.3])


