print(SynthDefs)

Clock.bpm = 120

var.off = var([3, 5, 6], dur=8)

p1 >> keys(P[0:8:4].offadd(var.off), scale=Scale.minor)

print(P[0:8:4].stretch(5))

d1 >> play("xxxxx   ")

d2 >> play("     * *")

d3 >> play("-[--]------")



print(p1.pitch)


