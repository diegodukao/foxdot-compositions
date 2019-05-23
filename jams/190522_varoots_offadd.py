Scale.default="minor"

# TODO: make the drums better
d1 >> play("x-o[-(-o)]", sample=2)

def c(degree):
    return P(0, 2, 4, 6) + degree

var.roots = var([0, 4, 3, 1, 2], dur=[4, 4, 4, 2, 2])

k1 >> keys(c(var.roots), dur=PDur(3,8))

b1 >> sawbass(var(var.roots + P[0, 2, 4, 6], dur=1/2),
              dur=PDur(12, 20), sus=1/4)


b2 >> bass(var.roots, dur=[4, 4, 4, 2, 2])

p1 >> blip(var.roots).every(3, "offadd", 2)


print(var.roots)

print(b1.pitch)

print(SynthDefs)
