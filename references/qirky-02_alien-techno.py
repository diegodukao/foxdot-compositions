Scale.default="minor"
Clock.bpm=140
c1 >> play("@", dur=1/4, sample=P[:8].rotate([0,1,3]), rate=4, pan=-0.5)

c2 >> play("#", dur=40, room=1, amp=2, pan=0.5)

d1 >> play("<V:><  * ><[--]>")

b1 >> dbass(dur=PDur(3,8), sus=2, chop=4, shape=PWhite(0,1/2),
            pan=PWhite(-1,1)).sometimes("offadd", 4).stop() + var([0,2],4)

# The P* plays all the notes across the note's
# duration - just like the square brackets in the "play" synth.
p1 >> space([7,6,4,P*(2,1),0], dur=8, pan=(-1,1))

# In a list of tuples of notes, passing a tuple to pan makes each note to be
# played with each pan value. If it's a single note, it's played in the middle
# of the two pan values.
# ex >> blip([(0,4), (3,7), 5, (4,0)], dur=4, pan=(-1,1))

Master().hpf=var([0,4000],[76,4])
