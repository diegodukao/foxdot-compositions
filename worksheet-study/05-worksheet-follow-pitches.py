# Part 2: Putting together a tune
# -------------------------------

# Ok, so we've got the basics, lets make a basic tune! So far we've only used the major
# scale, which the default, but we can use a whole bunch and even make up our own!
# To see the list of scales, use:

print(Scale.names())

Scale.default = "dorian"
Clock.bpm = 144

d1 >> play("xo xxo( [xo])[x ]", dur=1/2)
d2 >> play("---(-[--])")

b1 >> sawbass([0,-1,3], dur=[4,4,8])

# 3. Let's add some chords - we can make sure they fit with the bass by setting the pitch relative
# to the pitch of the bass, b1, using the addition operator (+ sign).

p1 >> star(b1.pitch)

p1 >> star(b1.pitch + (0,2,4), dur=1)

p1 >> star(b1.pitch + (0,2,4), dur=[3/4, 3/4, 1/2])

# 4. Create you own melody to go with it - pitch a SynthDef

print(SynthDefs) # e.g. blip

p2 >> blip(b1.pitch + [0,3,5], dur=[1/4,1/4,1/2,1/4, rest(1/2)])

p3 >> viola(b1.pitch + [7,3,5,1], dur=[3,3,1,1])

# What happens to our chords if we change the bass?

b1 >> sawbass([2,3,4,6], dur=4)
