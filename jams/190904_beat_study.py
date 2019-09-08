Clock.bpm = 150

d1 >> play("^  ^").every(4, "stutter", 4)

d2 >> play("X([ X][X ])O([X ][ O])", amp=0.8)

d3 >> play(" (x[xx]x)  ", amp=1)

d4 >> play("---[--]", amp=P[1.4, 0.7, 1, 0.6]*2).every(4, "bubble")
