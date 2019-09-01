Scale.default="minor"; Clock.bpm=120

d1 >> play("G(:-)", pshift=var([0,3],[6,2])+(0.1,0), pan=(-1, 1), rate=-1/2, room=3)

d2 >> play("x-").sometimes("stutter", 4, dur=3)

d3 >> play("  I ")

d3 >> play("  I ", sample=2, hpf=(0,2000), lpf=(300,0), hpr=0.5)

b1 >> dbass(var([0,6,5,2],[6,2]), dur=PDur(3,8,[0,2]), sus=2, chop=4, rate=4, amp=0.3).stop()

p2 >> blip([0,1,[[3,4],2]], dur=[4,3,1], drive=PWhite(0.2,0.7), oct=6, lpf=2000, room=1/2, echo=0.75, echotime=6, sus=1).penta().spread().stop()

k1 >> klank(oct=5, lpf=200, lpr=0.5).stop()
