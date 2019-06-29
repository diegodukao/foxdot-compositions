Scale.default="minor"; Clock.bpm=126; Root.default=var([0,3],32)

b1 >> dirt([0,0,0.5], dur=PDur(3,8), sus=1, chop=2, drive=0.5, formant=1, oct=(5), room=0.2).spread()

b2 >> bell(var(P[2:10]), dur=2/3, oct=6, pan=[-1,1]).penta()

p1 >> pasha(var([0,2,0.5],[3,1/2,1/2]), dur=PDur(5,8), oct=6, sus=2, pan=PWhite(-1,1)).every(4, "dur.shuffle")

c1 >> play("#", rate=-1/2, hpf=1000, dur=4, amp=4, room=1, coarse=16).spread()
d1 >> play("+", dur=PDur(3,8,[0,2]), amp=2, sample=3).sometimes("rate.offadd", 1)
d2 >> play("nN", dur=1/4, sample=PRand(5, seed=1)[:16], pan=PWhite(-1,1), rate=PRand(1,5))
d3 >> play("<|x1||l(21)|><  *( =)>", formant=0, sample=2).every(14.5, "jump", cycle=16)

d4 >> play("<[--]>< +( +)[ +]>")

c1.stop()
d1.stop()
d2.stop()
d3.stop()
d4.stop()

b1.stop()
b2.stop()
p1.stop()
