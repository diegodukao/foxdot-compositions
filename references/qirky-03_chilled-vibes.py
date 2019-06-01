# https://github.com/Qirky/ten-lines-or-less/blob/master/chilled-vibes.py

Clock.bpm=100; Scale.default="minor"

# p1 >> pulse([0,-1,-2,-3], dur=8, lpr=1, crush=0) + (0,2,4,const(6))
# p1 >> pulse([0,-1,-2,-3], dur=8, lpf=600, lpr=0.2, crush=25) + (0,2,4,const(6))
# p1 >> pulse([0,-1,-2,-3], dur=8, lpf=600, lpr=0.2, crush=45) + (0,2,4,const(6))
# p1 >> pulse([0,-1,-2,-3], dur=8, lpf=600, lpr=0.2, crush=50) + (0,2,4,const(6))
p1 >> pulse([0,-1,-2,-3], dur=8, lpf=600, lpr=0.2, crush=8) + (0,2,4,const(6))

# BUG FOUND: adding (+) to player a list of notes containing a P* works great,
# but if you decide to execute a print(p3.pitch), the player goes nuts and plays
# a whole lot of notes on the first index of the P*, than it plays the other
# ones normally. And it will always play like this on the first note, you will
# have to close and reopen FoxDot to fix it.
p3 >> blip(p1.pitch, dur=8, sus=4, room=1, oct=6) + [0,0,0,P*(2,4,3,-1)]

# p3 >> blip(p1.pitch, dur=8, sus=4, room=1, oct=6) + [0,0,0,2]
# print(p1.pitch)
# print(p3.pitch)  # it will break p3

p2 >> saw(P[:5][:9][:16], dur=1/4, oct=var([3,4],[12,4])).penta()
print(P[:5][:9][:16])

d1 >> play("(x )( x)o{ vx[xx]}", crush=16, rate=.8) \
    .every([24,5,3], "stutter", 4, dur=3)

d2 >> play("<-s>< ~*~>").every(30.5, "jump", cycle=32)

d2.stop()
d1.stop()

p2.stop()

p1.stop()
p3.stop()
