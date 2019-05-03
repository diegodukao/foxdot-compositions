Clock.bpm = 140

p1 >> pads(P[0,4,6,6,1] + (0,2,4), dur=[4,4,4,2,2], oct=4, scale=Scale.dorian, root=4)

p2 >> blip(p1.pitch[0] + P[0,5,2,6], dur=[1/2,1,1/2,rest(2)])

print(p1.pitch[0] + P[0,2,4,4])

d1 >> play('X ')

d2 >> play(' o( [ o])')

d3 >> play('--(-[--])-')
