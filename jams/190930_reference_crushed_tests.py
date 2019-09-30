Scale.default="minor"
Clock.bpm=120

var.chords = var(P[0, -2], 2)

b1 >> bass((var.chords + P[0, 2, 4, 6]) % 7, dur=[1/2, 1/4, 1/4, 3/4, 1/2, rest(1/4), 1/2]).every(5, "stutter", 2).every(8, "shuffle")

c1 >> blip((var.chords + (0,2,4,6) + var([0,3],[24,8])) % 7, dur=4, sus=2, echo=0.75,
           echotime=8, lpf=3000, lpr=0.2, room=0.25).spread().stop()
           
print(c1.pitch)

# p1 >> sinepad([0,4,[6,[8,9]],7], dur=1/2, sus=1, drive=0.1, room=1, amp=0.4,
#               lpf=expvar([20,2000],32)).sometimes("rotate") + var([0,2],[12,4])

# p2 >> pads(p1.pitch, dur=PDur(3,8)*4, pan=PWhite(-1,1), chop=4, oct=4)

c1.stop()
p1.stop()
