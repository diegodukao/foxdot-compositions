print(SynthDefs)

Clock.bpm = 120

var.off = var([3, 5, 6], dur=8)

p1 >> keys(P[0:16:4].shuffle().offadd(var.off), scale=Scale.minor)

# doesn't work as expected
# var.bass = var(p1.pitch[1], dur=4)
# p2 >> bass(var.bass, dur=[2,1,1/2,1], oct=4)

p2 >> bass(p1.pitch[1], dur=4, oct=3)

d1 >> play("x[x ]x[x x]x[[x ] ]x[  x]")

d4 >> play("  o  o [oo]")

d2 >> play("s s( s)")

d3 >> play("--------")

d5 >> play("(T ) ")

# d5 >> play("1! !1 1!")

# d5 >> play("$$ $ $ ( !)")

print(Samples)

print(p1.pitch)
