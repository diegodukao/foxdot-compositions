Clock.bpm=144; Scale.default="minor"

p1 >> pulse([0,-1,-2,-3], dur=8, lpf=600, lpr=0.2, crush=35) + (0,2,4,const(6))

d1 >> play("(x )( x)o{ vx[xx]}", crush=16, rate=.8).every([24,5,3], "stutter", 4, dur=3)

p2 >> saw(P[:5][:9][:16], dur=1/4, oct=var([3,4],[12,4])).penta()

d2 >> play("<-s>< ~*~>").every(30.5, "jump", cycle=32)


print(P[:5][:9][:16])

# original reference: qirky_03_chilled-vibes.py
# p3 >> blip(p1.pitch, dur=8, sus=4, room=1, oct=6) + [0,0,0,P*(2,4,3,-1)]
