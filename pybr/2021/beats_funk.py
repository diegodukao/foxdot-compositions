Clock.bpm = 126

d0 >>play("o", dur=1)

# volt mix 
d1 >> play("-", dur=1/2)
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4])
d3 >> play("x", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)])
d4 >> play("o", dur=[rest(1),1])
d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2])

# planet rock
d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4])
d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.5)
d3 >> play("o", dur=[rest(1), 1])
d4 >> play("x", dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])
d5.stop()

print(Samples)

Clock.bpm=130
# Tamborzão
d1 >> play("p",sample=1, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,1/2,rest(1/2)])
d2 >> play("p",dur=[1,rest(1)])
d3 >> play("p", sample=6, dur=[rest(2),rest(1/2),1/2,1/2,1/2])
d4 >> play("V", sample=2,dur=[1, rest(3)])
d5 >> play("V", sample=2, dur=[rest(2),rest(1/2),1/2,rest(1/2),1/2], rate=-1)

print(Samples)
