# https://www.youtube.com/watch?v=yjfoQKu6oJU

Scale.default = "major"

bP = P[0] + [0, 0, 0, 2, 0, 0, 3, 0, 0, 3.5, 0, 3, 0, 2]

bR = P[1/2] | P[1/4].stutter(12) | P[1/2]

b1 >> dbass(bP, dur=(1/2 | P[1/4].stutter(12) | 1/2))

print(P[1/2])

print([1/2, P[1/4].stutter(12), 1/2])

print(bP)
