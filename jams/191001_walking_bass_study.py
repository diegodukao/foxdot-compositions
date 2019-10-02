Scale.default = "minor"

var.chords = var([0, 0, 4, 4, 0, 3, 4, 0], dur=4)


~b1 >> bass(
    [0, P[2, 4, 6].shuffle(), P[0, 2, 4, 6, 8].shuffle(), P[-2, -1, 1, 2].shuffle()])
    
d1 >> play("-", dur=[1, 0.7, 0.3])

print(var.chords.now())

