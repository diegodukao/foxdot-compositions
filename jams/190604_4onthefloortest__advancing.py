# Trying to use delay (to make some dub). None of these worked as expected
# p1 >> keys(P[0, -1, -2, -3], delay=[0, 0, 0, (0, 1.5)], dur=4)
# p1 >> keys(P[0, -1, -2, -3], delay=[0, 0, 0, (0, 0.5, 0.8, 0.9, 1, 1.2, 1.5)],
#            dur=4)
# p1 >> keys(P[0, -1, -2, -3], room=0.1, echo=1, decay=8, dur=4)
# d1 >> play("(x )( x)o ", room=0.1, echo=0.75/2, decay=4)

# d1 >> play("xxxx", dur=1)
# d2 >> play(" o o", dur=1)

Clock.bpm = 110

d1 >> play("<xxxx>< * *>", dur=1, sample=0)
hh >> play("-------[--]", dur=1/2, sample=3)

h2 >> play("- -  ---", dur=1/2, sample=2).stop()

print(Samples)

Scale.default = "major"
Root.default = "G"

var.roots = var(P[0, 2, 1, var([4, 3, 2], dur=[4, 2, 2])], dur=8)

# p1 >> keys(var.roots, dur=[1, 1/2, 1, 1, 1/2, 1, 2, 1/4, 1/4, 1/4, 1/4]) + (0, 2, 4)
p1 >> keys(var.roots, dur=PDur(2, 5)) + (0, 2, 4)

# how to change the sus of the offadd
# b1 >> sawbass(var.roots + P[0, 2, 4, 6], dur=1, sus=1).every(32, "shuffle").every(4, "offadd", 7, "sus", 1/2)
b1 >> sawbass(var.roots + P[0, 2, 4, 6], dur=1, sus=1/2).every(32, "shuffle").every(4, "offadd", 7)
