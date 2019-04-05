Scale.default = "dorian"

Clock.bpm = 144

d1 >> play("xo xxo( [xo])[x ]", dur=1/2)

d3 >> play("---(-[--])")

d1 >> play("x-")

d2 >> play("  * ")


b1 >> sawbass([0,-1,3], dur=[4,4,8])


p1 >> star(b1.pitch)

p1 >> star(b1.pitch + (0,2,4), dur=1)

p1 >> star(b1.pitch + (0,2,4), dur=[3/4, 3/4, 1/2])


p2 >> blip(b1.pitch + [0,3,5], dur=[1/4,1/4,1/2,1/4, rest(1/2)]).every(9, "offadd", 5).every(12, "stutter", 3, dur=1/2)

p3 >> viola(b1.pitch + [7,3,5,1], dur=[3,3,1,1])


# What happens to our chords if we change the bass?

b1 >> sawbass([2,3,4,6], dur=4)
