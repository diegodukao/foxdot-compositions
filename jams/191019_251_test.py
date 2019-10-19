Scale.default = "major"
# var.roots = var([2, 5, 1], dur=[4, 8, 4])
# var.roots = var([2, 5, 3, 0], dur=[4, 4, 4, 4])
# var.roots = var([2, 5, 3, 1], dur=[4, 4, 4, 4])

var.roots = var([1, 4, 0], dur=[4, 8, 4])

p1 >> piano(var.roots + P(0, 2, 4, 6), dur=2)

p2 >> karp(var.roots + P[0, 2, 4, 6][:6], dur=PDur(5, 8)*2)
