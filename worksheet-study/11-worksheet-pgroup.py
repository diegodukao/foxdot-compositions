# line 634

# Along with playing notes together like so:
    
p1 >> pads(P(0, 2, 4, 6), dur=4)

p1.stop()

# PGroups can also be used to play notes in quick succession by putting
# different symbols between the 'P' and the brackets:

p1 >> pads(P(0, 2, 4, 6), dur=4)    

p1 >> pads(P[0, 2, 4, 6], dur=4)

p1 >> pads(P*(0, 2, 4, 6), dur=4)

p1 >> pads(P[0, 2, 4, 6], dur=2)

p1 >> pads(P*(0, 2, 4, 6), dur=2)


p1.stop()

# Notice the difference? The P* plays all the notes across the note's
# duration - just like the square brackets in the "play" synth. You
# can use the + symbol to spread the notes over a note's sustain
# as opposed to the duration, which can be useful when using varying
# lengths of durations:
    
p1 >> pluck(P*(0, 4), dur=PDur(3,8), sus=1)

p1 >> pluck(P*(0, 4), dur=4, sus=2)

p1 >> pluck(P+(0, 4), dur=4, sus=2)

p1 >> pluck(P+(0, 4), dur=PDur(3,8), sus=1)

p1 >> pluck(P+(0, 4), dur=3, sus=1)

p1 >> pluck(P*(0, 4, 6, 6, 2,), dur=3, sus=1)

p1 >> pluck(P+(0, 4, 6, 6, 2,), dur=3, sus=1)

p1 >> pluck(P+(0, 4), dur=PDur(3,8), sus=2)

print(PDur(3,8))
