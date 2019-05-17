Clock.bpm=144
Scale.default="major"

d1 >> play("x-o[-(-o)]", sample=0).every([28,4], "trim", 3)
c1 >> play("#", dur=32, room=1, amp=2).spread()

# p1 >> sawbass([0, 3, 2, 6], dur=PDur(3,8), sus=1/2, cutoff=4000)
p1 >> sawbass([0, 3, 2, 6, 4, -1], dur=PDur(3,8), sus=1/2, cutoff=4000).every([28,4], "trim", 3)

p2 >> karp(dur=1/4, pan=PWhite(-1, 1), rate=PWhite(40))

print(list(PWhite(-1, 1)))

print(list(PWhite(40)))


# original reference: algo-grave.py
# p1 >> sawbass(var([0, 1, 5, var([4, 6], [14, 2])], 1), dur=PDur(3,8), cutoff=4000,
#               sus=1/2, amplify=var.switch)

# p1 >> karp(dur=1/4, rate=PWhite(40), pan=PWhite(-1,1), amplify=var.switch,
#            amp=1, room=0.5)
