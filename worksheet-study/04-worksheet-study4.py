# line 163

# To play things at the same time, just use multiple Players. Try changing the values and adding keyword
# arguments to the code below:

p1 >> bass([0,2,4,9,7], dur=[1/4, 1/2, 3/4, 1/2, 3/4, 1/4], amp=[1.0, 0.5], octs=[3, 4, 2], rate=0.4)

d1 >> play("X X ", amp=1.5)
d2 >> play("---(-[--])")
d3 >> play("  O( [oo])")
