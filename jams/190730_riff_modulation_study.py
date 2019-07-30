Root.default = "C"

Root.default = "D"

# p1 >> piano(P[0:14].sample(10), oct=4, dur=[1, 1/2, 1, 1/2, 1]).penta().shuffle()
# p1 >> piano(P[0:7].sample(5), oct=4, dur=[1, 1/2, 1, 1/2, 1]).penta().shuffle()
p1 >> piano([6, 0, 4, 5, 1], oct=4, dur=[1, 1/2, 1, 1/2, 1]).penta()

#p2 >> bass([0, 4, 5, 1, 6] ,dur=[1, 1/2, 1, 1/2, 1], sus=1/2)
p2 >> bass([6, 0, 4, 5, 1], dur=[1, 1/2, 1, 1/2, 1], sus=1/2, oct=5, lpf=200).penta()

print(p1.pitch)
print(p2.pitch)

p1.stop()

p2.stop()
