Scale.default = "minor"

var.roots = var(0)

p1 >> keys(var.roots + (0, 2, 4), dur=[2], sus=1).offbeat(2)

b1 >> bass(var.roots + [0, 2, 3], dur=[1, 1.5, 0.5], sus=1, lpf=2000)
