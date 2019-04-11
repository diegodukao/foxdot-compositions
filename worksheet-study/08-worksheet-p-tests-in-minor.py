# line 500

Scale.default = "minor"

p1 >> blip(b1.pitch + P[:10:2], dur=PDur(5,8)*2, sus=2, oct=PStep(7,5,6)).every(6, "reverse").often("trim", 3).every(9, "stutter", 4, dur=3)

d1 >> play("  o   o ")

d3 >> play("X", dur=[1, 1/2, 1, 1/4, 1/2, 1/4, 1/2])

d2 >> play("---(-[--])")

b1 >> dbass([0, 2, 6], dur=8)

c1 >> keys(b1.pitch + (0,2,4), dur=[1, 1/2, 1, 1/4, 1/2, 1/4, 1/2], amp=1)
