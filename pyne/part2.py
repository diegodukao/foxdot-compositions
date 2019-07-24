"""
    @diegodukao

    dó | ré | mi | fá | sol | lá | si
    C  | D  | E  | F  |  G  | A  | B

    escala de C menor
    C  | D  | Eb | F  |  G  | Ab | Bb
"""

Scale.default = "minor"
Root.default = "C"
Clock.bpm = 120

p1 >> keys([0, 4, 6, 3, 2, 1], dur=[4, 4, 4, 2, 1, 1])

p2 >> keys(p1.pitch + (0, 2, 4, 6), dur=p1.dur, amp=0.6)

p3 >> sawbass(p1.pitch + [0, 2, 4, 6], amp=0.7, dur=[1, 1/2, 1/4, 1/4, 1/4, 1/2, 1/4], sus=1/4, lpf=2000)

p4 >> prophet(p1.pitch + P[0:8], dur=1/4, amp=0.3, drive=0.2).penta().shuffle()

d1 >> play("X O ")
d2 >> play("----", dur=1/4)

d1.stop()
d2.stop()

p2.stop()

























# p1 >> keys([0, 4, 6, 3, 2, 1], dur=[4, 4, 4, 2, 1, 1])
#
# p2 >> keys(p1.pitch + (0, 2, 4), dur=p1.dur)
#
# p3 >> sawbass(p1.pitch + P[0, 2, 4, 6], dur=[1/2, 1, 1/4, 1/4, 1/4, 1/2, 1/4],
#               sus=1/4, lpf=2000)
#
# p4 >> prophet(p1.pitch + P[0:8], dur=PDur(3, 8), drive=0.2, amp=0.4).shuffle().penta()
#
# d1 >> play('X O( [ O])')
# d2 >> play('----', dur=1/4)
# d3 >> play('#', dur=32, amp=3)
