Scale.default = "minor"
Root.default = "C"
Clock.bpm = 120

p1 >> keys([0, 4, 6, 3, 2, 1], dur=[4, 4, 4, 2, 1, 1], oct=5)

p2 >> keys(p1.pitch, dur=p1.dur, amp=1.5) + (0, 2, 4)

p3 >> sawbass(p1.pitch + P[0, 2, 4, 6], dur=[1/2, 1, 1/4, 1/4, 1/4, 1/2, 1/4],
              lpf=2000, amp=2, sus=1/4)
              
p4 >> prophet(p1.pitch + P[0:8], dur=PDur(3, 8), drive=0.2).penta()

print(SynthDefs)
              
d1 >> play('X O( [ O])').every([28, 4], 'trim', 3)
d2 >> play('---([- ][--])', dur=1/4).every([28, 4], 'trim', 3)
d3 >> play('#', dur=32, amp=3)

print(Samples)

d1.stop()
d2.stop()
d3.stop()

p1.stop()
p2.stop()
p3.stop()
p4.stop()
