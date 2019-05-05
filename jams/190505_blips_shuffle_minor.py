# p1 >> blip(P[0:16].shuffle())

var.blips = P[0:16].shuffle()

p1 >> blip(var.blips, dur=1/4)

p1 >> blip(var.blips, dur=[1/4,1/2,1/2,1/4])

p1 >> blip(var.blips, dur=[1/4,1/2,1/2,1/4], scale=Scale.minor)

# d1 >> play("xx xxx x", dur=[1/4, 1/2, rest(3/4), 1/4, 1/2, 1/4, rest(1/4), 1/4])

# b1 >> sawbass(p1.pitch, dur=[1, 1/2, 1/2, 1.5, 1/2, 1, 3/4, 1/4], amp=0.8)

# p2 >> keys(p1.pitch + (0, 2, 4), dur=6)

# d1 >> play()


