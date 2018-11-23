# print(SynthDefs)

# p1 >> nylon([0, 2, 4], dur=[1, 1/2, 1/2])
# p1 >> creep([0, 5, 3, 6], dur=[1, 1/3, 1/3, 1/3], amp=0.75)

## Adding values to change the pitch ##
# p1 >> pluck([0, 1, 2, 3], dur=2)
# p1 >> pluck([0, 1, 2, 3], dur=2) + [0, 0, 4]
# p1 >> pluck([0, 1, 2, 3], dur=2) + [0, 0, 0, 8]
# p1 >> pluck([0, 1, 2, 3], dur=2) + [0, 8, 0, 8]

## Playing chords ##
# p1 >> pluck([0, 1, 2, 3], dur=2)
# p1 >> pluck([0, 1, 2, 3], dur=2) + (0, 2, 4)
# p1 >> pluck((0, 2, 4), dur=2)
# p1 >> pluck([(0, 2, 4), (4, 6, 8)], dur=2)
# p1 >> pluck([(0, 2, 4), (0, 3, 5)], dur=4)

## Playing samples ##
# d1 >> play("x-o-")
# d1 >> play("(xo)---")
# d1 >> play("(x-)(-x)o-")
# d1 >> play("x-o[---]", dur=1)
# d1 >> play("[xx]-o[---]", dur=1)
# d1 >> play("x-o{-=*}")  # picking a random
d1 >> play("(x[--])xo{-[--][-x]}")  # TODO: study

## Stutter: repeats values in a Pattern n times
# p1 >> pluck(P[0, 3, 0, 4].stutter(4))
# p1 >> pluck(P[0, 3, 0, 4].stutter(4) + (0, 2, 4))
p1 >> pluck(P[(0, 2, 4), (0, 3, 5)].stutter(2), dur=2)
