print(SynthDefs)

Clock.bpm = 120

var.off = var([3, 5, 6], dur=8)

# TODO: expand the P range for more than the size of the melody and get random
# notes
p1 >> keys(P[0:8:4].offadd(var.off), scale=Scale.minor)

# didn't work well
# p2 >> bass(var(p1.pitch + var.off, dur=4), dur=[1,2,1/2,1,1/2], oct=5, amp=0.7)


print(P[0:8:4].stretch(5))

d1 >> play("x[x ]xxx x[ x]")

d4 >> play("  O  O [Oo]")

d2 >> play("     * *")

d3 >> play("-[--]------")

# d5 >> play("1! !1 1!")

d5 >> play("$$ $ $ ( !)")

print(Samples)

print(p1.pitch)


