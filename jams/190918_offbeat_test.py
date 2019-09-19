Scale.default = "minor"

# var.roots = var([0, 3, 2, 1], dur=[19, 6, 6, 6])
var.roots = var([0], dur=[4])

p1 >> keys(var.roots + (0, 2, 4), dur=[2], sus=1).offbeat(2)

b1 >> bass(var.roots + [0, 2, 3], dur=[1, 1.5, 0.5], sus=1, lpf=2000)
