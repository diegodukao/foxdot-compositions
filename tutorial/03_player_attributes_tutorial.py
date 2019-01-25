## octs
# p1 >> pluck(oct=[3, 4, 5], dur=1/2)
p1 >> pluck([0, 2, 1], oct=[3, 4, 3], dur=1/2)

## dur
# p1 >> pluck([0, 1, 2, 3], dur=[1,1/2,0.5])
# p1 >> pluck([0, 1, 2, 3], dur=[0.1,0.3,0.43,0.17])
# p1 >> pluck([0, 1, 2, 3], dur=[1, 1, 0])  # skip every third note
p1 >> pluck([0, 1, 2, 3], dur=[1, 1, rest(2)])  # rest every third note for 2 beats

## scale
# p1 >> pluck([0, 2, 4, 6, 7])
p1 >> pluck([0, 2, 4, 6, 7], scale=Scale.dorian)

## amp
# p1 >> pluck([0, 1, 2], dur=[1, 1/2, 1/2], amp=[1, 0.5, 1/3])
p1 >> pluck(dur=1/4, amp=[1, 1/2, 1/2, 1, 0, 1, 0, 1, 1/2, 1/2, 1, 0, 1, 1/2, 1/4, 1])

## samples
# p1 >> play("x-o-")
# p1 >> play("x-o-", sample=1)
p1 >> play("x-o-", sample=[0, 1, 2])

## delay
# p1 >> pluck([0, 1, 2, 3], delay=[0, 0, 0.5])
# "Stutter" every third note
# p1 >> pluck([0, 1, 2], delay=[0, 0, (0, 0.5)])
# Delay a note to play *after* the following one
p1 >> pluck([0, 1, 2], delay=[0, 0, (0, 1.5)])
