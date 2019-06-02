# Trying to use delay (to make some dub). None of these worked as expected
# p1 >> keys(P[0, -1, -2, -3], delay=[0, 0, 0, (0, 1.5)], dur=4)
# p1 >> keys(P[0, -1, -2, -3], delay=[0, 0, 0, (0, 0.5, 0.8, 0.9, 1, 1.2, 1.5)],
#            dur=4)
# p1 >> keys(P[0, -1, -2, -3], room=0.1, echo=1, decay=8, dur=4)
# d1 >> play("(x )( x)o ", room=0.1, echo=0.75/2, decay=4)

# d1 >> play("xxxx", dur=1)
# d2 >> play(" o o", dur=1)
d1 >> play("<xxxx>< o o>", dur=1, sample=0)
hh >> play("-------[--]", dur=1/2, sample=3)

Scale.default = "minor"
Root.default = "G"

b1 >> sawbass(P[0, 4, 3, 1], dur=PDur(2, 5)*2, sus=1/4)

p1 >> keys(P[0, 0, 5, 4, 3], dur=8) + P(0, 2, 4)

p2 >> blip(p1.pitch[0], dur=[1/2, 1/2, 1/2, 1/2, 1])

print(p1.pitch[0])
