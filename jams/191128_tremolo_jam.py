Scale.default = "minor"

p1 >> keys(drive=1, dur=4, sus=3, amp=0.5, tremolo=3, pan=0)

~b1 >> sawbass([0, 3], dur=[1.5, 2.5], sus=0.5, lpf=600).every(2, "stutter", 2, oct=5, pan=[-1,1]).every(4, "offadd", 7)

p2 >> karp(dur=PDur(5,8), pan=[-1], amplify=var([1, 0], dur=4))

notes = P[0:7][:8].shuffle()

p3 >> piano(notes, dur=P[1/2, 1/2, 1/2, 1], pan=-1, drive=0).penta().every(4, "offadd", 2)
p4 >> piano(notes + 4, dur=P[1/2, 1/2, 1/2, 1], pan=1, drive=0).penta().every(4, "offadd", 2)

Group(p3, p4).solo()

b0 >> bass([0, 4, 3, 2, 0, 2, 3, 2], dur=P[4, 2, 1, 1])

d1 >> play("X ")

print(list(bla))

