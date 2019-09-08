Scale.default="minor"


var.chords = var([0, 3], 8)

# p1 >> gong(P[var.chords,4,6,7][:6], dur=PDur(3,8)*2)

# print(P[0,4,6,7][:6])
# print(PDur(3,8)*2)

p0 >> piano(var.chords + var([(0, 2), (2, 4, 8)]), dur=[1, 1/2], amp=1)

p1 >> karp(P[var.chords, 2, 3, 6, 3, 4][:8], dur=PDur(8, 10)).every(16, "shuffle")

b1 >> bass(var.chords + var([0, -1, -4], [12, 2, 2]), dur=PDur(5, 8), amp=1)


d1 >> play("[--] -", dur=1/2, amp=1.5).stop()
d2 >> play("X ", sample=2)
d3 >> play("---[--]", dur=1/4)
d4 >> play("  O ")




#d6 >> play("[ x][X ]" + "[ x][X ]" + "[ x][X ]" + "[ X] ", amp=P[0.6, 1.6, 0.6, 1.6, 0.6, 1.6, 1.6, 1.6]/2)
