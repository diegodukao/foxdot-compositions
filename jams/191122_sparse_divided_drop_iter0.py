Scale.defaul = "minor"

p1 >> keys(dur=[1/4, 1/4, 1/4, 1/4, rest(3)])
p2 >> keys(3, dur=[rest(2), 0.75, 0.75, 0.5], sus=1/2)
d1 >> play("H   ", dur=1, sample=0)
d2 >> play("X ", sample=2)


def drop():
    p1 >> keys(dur=[1/4, 1/4, 1/4, 1/4, rest(3)])
    p2 >> keys(3, dur=[rest(2), 0.75, 0.75, 0.5], sus=1/2)
    d1 >> play("H   ", dur=1, sample=0)
    d2 >> play("X ", sample=2)
    d3 >> play("-", dur=1/4)
    d4 >> play("  o ")

p_all.solo()

nextBar(drop())

d_all.stop()

print(Samples)

print(PDur(3,8))
