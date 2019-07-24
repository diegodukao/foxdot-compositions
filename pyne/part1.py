"""
    PyNE 2019
    FoxDot: Música com Python
    Diego Moreira Guimarães
    @diegodukao

    dó | ré | mi | fá | sol | lá | si
    C  | D  | E  | F  |  G  | A  | B

    escala de C maior
    C  | D  | E  | F  |  G  | A  | B

    escala de G maior
    G  | A  | B  | C  | D  | E  | F#
"""

Scale.default = "major"
Root.default = "G"
Clock.bpm = 120

p1 >> keys([0, -1], dur=4)

p2 >> keys(p1.pitch + (0, 2, 4), dur=p1.dur, amp=0.8)

p3 >> sawbass(p1.pitch + [0, 2, 4, 6], sus=1/4).shuffle().every(4, "offadd", 4)

p4 >> viola(p1.pitch + P[0, 8], dur=1/4).penta().shuffle()

p1 >> keys([1, -3], dur=4)

d1 >> play("X O( [ X])")
d2 >> play("----", dur=1/4)

d1 >> play("X ")

d1.stop()
d2.stop()




















# p1 >> keys([0, -2], dur=8)
#
# p2 >> keys(p1.pitch, dur=p1.dur) + (0, 2, 4)
#
# p3 >> sawbass(p1.pitch + P[0, 2, 4, 6], sus=1/4, dur=1).shuffle().every(3, "offadd", 4)
#
# p4 >> viola(p1.pitch + P[0:8], dur=1/4).shuffle().penta()
#
# p1 >> keys([1, -3], dur=8)
#
# d1 >> play("X O ")
# d3 >> play("   ( [ X])")
# d2 >> play("---(-[--])", dur=1/4)
#
# d1.stop()
# d2.stop()
# d3.stop()
#
# p1.stop()
# p2.stop()
# p3.stop()
# p4.stop()
