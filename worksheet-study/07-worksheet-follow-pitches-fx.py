Scale.default = "dorian"

Clock.bpm = 144


# d1 >> play("xo xxo( [xo])[x ]", dur=1/2)

d1 >> play("x-")

d2 >> play("  * ")

d3 >> play("---(-[--])")


b1 >> sawbass([0,-1,3], dur=[4,4,8])


p1 >> star(b1.pitch)

p1 >> star(b1.pitch + (0,2,4), dur=1)

p1 >> star(b1.pitch + (0,2,4), dur=[3/4, 3/4, 1/2], chop=4, sus=2, amp=0.5)


p2 >> blip(b1.pitch + [0,3,5], dur=[1/4,1/4,1/2,1/4, rest(1/2)], room=1, mix=[1,0.25,0.5,0.75], amp=1.5).every(9, "offadd", 5).every(12, "stutter", 3, dur=1/2)

p3 >> viola(b1.pitch + [7,3,5,1], dur=[3,3,1,1], amp=0.8)


# Bass change

b1 >> sawbass([2,3,4,6], dur=4)
