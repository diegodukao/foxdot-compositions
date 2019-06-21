Scale.default="harmonicMajor"
Clock.bpm=144

# Introduce one line at a time using Alt+Return
d1 >> play("<(x )(sx)d(@hb)>< + +( [ +])>", sample=var([1,2]),
           crush=var([16,32],2), amp=var([1,0],[60,4])) \
           .every(3, "stutter", 4, dur=var([3,1],[7,3]), rate=2, pan=[-1,1])

c1 >> blip(((0,2,4,6) + var([0,3],[24,8])) % 7, dur=8, sus=2, echo=0.75,
           echotime=8, lpf=3000, lpr=0.2, room=0.25).spread()

p1 >> sinepad([0,4,[6,[8,9]],7], dur=1/2, sus=1, drive=0.1, room=1, amp=0.4,
              lpf=expvar([20,2000],32)).sometimes("rotate") + var([0,2],[12,4])

p2 >> pads(p1.pitch, dur=PDur(3,8)*4, pan=PWhite(-1,1), chop=4, oct=4)

c1.stop()
p1.stop()
