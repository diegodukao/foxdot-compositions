# TimeVar

# Playing the chords for 8 beats each but with a player that is playing
# notes every quarter beats.

# Using stutter
print(P[0, 3, 0, 4].stutter(4) + (0, 2, 4))

p1 >> pluck(P[0, 3, 0, 4].stutter(32), dur=1/4) + (0, 2, 4)

p1 >> pluck(P[0, 3, 0, 4].stutter(32), dur=[1,1/4,1/4,1/2]) + (0, 2, 4)

# Using TimeVar
a = var([0,3,5,4,2,7,6],4)
print(int(Clock.now()), a)

print(int(Clock.now()), a)

p1 >> pluck(var([0, 3, 0, 4], 8), dur=[1/4]) + (0, 2, 4)

p1 >> pluck(var([0, 3, 0, 4], 8), dur=[1,1/4,1/4,1/2]) + (0, 2, 4)

# line 547

Scale.default = "dorian"
Clock.bpm = 144

var.chords = var([0,5,4,2], dur=[4,4,6,2])


b1 >> sawbass(var.chords, dur=1)

print(PDur(3,8)*2)
b1 >> sawbass(var.chords, dur=PDur(3,8)*2)

b1 >> sawbass(var.chords, dur=1, oct=[5,5,[6,4],5])

b1 >> sawbass(var.chords, dur=PDur(3,8)*2, oct=[5,5,[6,4],5])

b1 >> sawbass(var.chords, dur=PDur(3,8)*2, oct=[5,5,[6,4],5], pan=[0,[-1,1]])


p1 >> blip([var.chords,2,3,4], sus=2)

# Listen to the first note in the sequence, it changes with the chords. We can continue
# to add all sorts of functions to the sequence to make it more interesting

p1 >> blip([var.chords,2,3,4], sus=2).every(6, "offadd", 5)

p1 >> blip([var.chords,2,3,4], sus=2).every(6, "offadd", 5).every(9, "stutter", 3, dur=3, pan=[-1,1], oct=6)

p1 >> blip([var.chords,2,3,4], sus=2).every(6, "offadd", 5).every(9, "stutter", 3, dur=3, pan=[-1,1], oct=6).every(6, "reverse")

# Now let's introduce our triads again. This time we'll use "var.chords" instead
# of "b1.pitch" when adding (0, 2, 4).

p2 >> star(var.chords + (0, 2, 4), dur=PDur(3,8), amp=0.6)
print(var.chords)
print(b1.pitch)

# Question: What happens if we do use b1.pitch? Why does it happen?

p2 >> star(b1.pitch + (0, 2, 4), dur=PDur(3,8))

d1 >> play("x x ")

d1 >> play("x-x(-[--])")

d2 >> play("  H ")


# Let's use a new "var" to apply a high pass filter to the drums for the last bar of an 8 bar cycle
# Set the filter to be 0 for 28 beats (7 bars x 4 beats) and then 4000 for 4 beats (1 bar x 4 beats)

var.filter = var([0,8000], dur=[28,4])

d1 >> play("x-", hpf=var.filter)
d2 >> play("  H ", hpf=var.filter)

# Try and add your elements to the mix - see if there are other interesting ways of
# combining the "var.chords" variable.

# - Try applying the "var.filter" to p1, p2, and b1.
# - Try using brackets and .every to make the percussive sounds more complex
# - What happens when you change "var.chords"? e.g.

var.chords = var([2,3,4,6], dur=4)
