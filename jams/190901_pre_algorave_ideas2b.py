Scale.default="minor"; Clock.bpm=150

d1 >> play("G(:-)", pshift=var([0,3],[6,2])+(0.1,0), pan=(-1, 1), rate=-1/2, room=3).stop()

d2 >> play("x-").sometimes("stutter", 4, dur=3).stop()

d3 >> play("  o ", sample=3, hpf=1, hpr=0.5).stop()

d4 >> play("[tt]", amp=[1.3, 0.4]).every(8, "bubble", 2)

d5 >> play("^ ", dur=PDur(3, 8, [0, 2]))

d6 >> play(" o    o ", dur=1, drive=0.5).stop()




b1 >> dbass(var([0,6,5,2],[6,2]), dur=PDur(3,8,[0,2]), sus=2, chop=4, rate=4, amp=0.3)

p2 >> blip([0,1,[[3,4],2]], dur=[4,3,1], drive=PWhite(0.2,0.7), oct=6, lpf=2000, room=1/2, echo=0.75, echotime=6, sus=1).penta().spread()

k1 >> klank(oct=5, lpf=200, lpr=0.5)
