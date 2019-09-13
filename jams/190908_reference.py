# https://www.youtube.com/watch?v=No-bBhbJAac

Scale.default="minor"

var.chords = var([0,2],8)

p1 >> gong(P[var.chords,4,6,7][:6], dur=PDur(3,8)*2, amp=2)

p2 >> bell(var.chords + var([(0, 2), (2, 4)]), dur=[1, 1/2], amp=1/2)

# p3 >> prophet(P[3, 2, var.chords].loop(4)|P[4, 4, 4, 4], dur=1/4, amp=2, sus=1/4)

p3 >> prophet(P[3, 2, var.chords].loop(4)|P[var([4 ,6])].stutter(4), dur=1/4, amp=2, sus=1/4, formant=PRand(4)[:16])


b1 >> sawbass(var.chords + var([0, 5, 1], [16, 8, 8]), dur=PDur(5, 8))

d1 >> play("x[ [sn]]", sample=2, dur=2)
d2 >> play("- -- - -- ", dur=1/4)

print(P[0,4,6,7][:6])

print(PDur(3,8)*2)

print(PDur(3,8,[0,2]))
