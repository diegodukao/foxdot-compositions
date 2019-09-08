Scale.default="minor"



var.chords = var([0, 3], 8)

b1 >> bass(var.chords, dur=1/4, sus=1/8) + var([0, 2, 1, 2, 3], [6, 1/4, 2, 1/4, 1/4, 2, 1/4, 1/2, 1/4, 1/4])

b1 >> bass(var.chords, dur=PDur(3,8), sus=1/8) + var([0, 2, 1, 2, 3], [6, 1/4, 2, 1/4, 1/4, 2, 1/4, 1/2, 1/4, 1/4])

~b2 >> sawbass(b1.pitch, dur=4, oct=6, cutoff=8000, sus=2, chop=16).stop()

p1 >> karp(b1.pitch, dur=PDur(5,8))


d1 >> play("[--] -", dur=1/2, amp=1.5)
d2 >> play("X ", sample=2)

d3 >> play("---[--]", dur=1/4)

d4 >> play("  O ")




#d6 >> play("[ x][X ]" + "[ x][X ]" + "[ x][X ]" + "[ X] ", amp=P[0.6, 1.6, 0.6, 1.6, 0.6, 1.6, 1.6, 1.6]/2)
