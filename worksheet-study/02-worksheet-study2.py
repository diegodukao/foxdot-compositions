Scale.default = "dorian"

# All of the timing is handled by "Clock" and we can change the tempo if we want

Clock.bpm = 144

# 1. Let's start with a basic drum beat

d1 >> play("x ")

# 2. Add a bassline

b1 >> sawbass([0,-1,3], dur=[4,4,8])

# 3. Let's add some chords - we can make sure they fit with the bass by setting the pitch relative
# to the pitch of the bass, b1, using the addition operator (+ sign).

p1 >> star(b1.pitch)

p1 >> star(b1.pitch + (0,2,4))

p1 >> star(b1.pitch + (0,2,4), dur=[3/4, 3/4, 1/2])

# 4. Create you own melody to go with it - pitch a SynthDef

print(SynthDefs) # e.g. blip

# e.g. p2 >> blip([0,7,6,4,2], dur=1/2, sus=1)

p2 >> fuzz([0,3,6,5,5,0,0], dur=[1/2, 1/2, 1/2, 1, 1/4, 1/2])

# 5. Let's add to our drums. Try making this more complex by using the different brackets

d1 >> play("x-[x-x]")

d2 >> play("  * ")

# What happens to our chords if we change the bass?

b1 >> sawbass([2,3,4,6], dur=4)