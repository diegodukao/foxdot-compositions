Scale.default = "minor"
Root.default = 4


print(Samples)

d1 >> play('[--]', amp=2).every(1, 'bubble').stop()

d2 >> play('m m ', amp=2).every(16, 'bubble').shuffle().stop()

d4 >> play('^ ^ ', amp=2)

d5 >> play('m' * 8, dur=1/8, amp=2).stop()

d3 >> play(' - -', amp=2.5)

a1 >> star(([16, 14, 12] * 3 + [40, 38, 36]) * 3 + [48, 38, 36], dur=1/8, amp=2)

k9 >> keys([5, 3, 2, 1], dur=1/4, amp=2.5)

r7 >> play("@   @   ")

r7 >> play(" C D C D").every(8, 'shuffle').stop()


j1 >> jbass([8, 2, 0], sus=4).stop()

a1.stop()

d1.stop()
d2.stop()
d3.stop()
d4.stop()

n1 >> noise(17, dur=4, amp=0.)


# ['loop', 'stretch', 'play1', 'play2', 'audioin', 'noise', 'dab', 'varsaw', 'lazer', 'growl', 'bass', 'dirt', 'crunch', 'rave', 'scatter', 'charm', 'bell', 'gong', 'soprano', 'dub', 'viola', 'scratch', 'klank', 'feel', 'glass', 'soft', 'quin', 'pluck', 'spark', 'blip', 'ripple', 'creep', 'orient', 'zap', 'marimba', 'fuzz', 'bug', 'pulse', 'saw', 'snick', 'twang', 'karp', 'arpy', 'nylon', 'donk', 'squish', 'swell', 'razz', 'sitar', 'star', 'jbass', 'piano', 'sawbass', 'prophet', 'pads', 'pasha', 'ambi', 'space', 'keys', 'dbass', 'sinepad']


p1 >> play("x x x ", dur=PSum(3, 2), delay=[1/4], echo=var(0.04, 0.5), amp=0.4, pan=(-1, 1, -1, 1, -1), room=99999, chop=var(PRand(10) * 0.1) , bits=PRange(4, 24))

p9 >> pluck([P(6)], dur=PSum(3, 2), amp=1.5, delay=1/2).stop()

p8 >> pluck([(0, 2, 3), [1, 8]], dur=1/2, amp=1.3, chop=var(100)).every(2, "stutter").stop()

p7 >> play("!", dur=PSum(3, 2), delay=[1/2, 1/4], amp=[1.2, 0.8, 1, 0.9], room=1, echo=var(1, 2), chop=[1/2]).stop()

p6 >> pluck([P(6), 3, P([1, 4, 8]), (-3, 0, 1), (0, 3, 7), (0, -3, -7)], dur=[2], delay=[1/2, 1/4], amp=2.3)

r1 >> jbass([0,0,0,0,4,4,2,2], sus=1).every(4, 'bubble')

r8 >> jbass([0,0,0,-1,0,6,6,2,2,1], sus=1/2, dur=[1, 1, 3/4, 1/4, 1, 1, 1, 1, 1/4, 3/4])

r2 >> fuzz([0,0,0,0,2,2,2,2], vib=8, dur=1/4, slide=0.5, bend=0.5)

r3 >> donk([0,0,0,0,2,2,2,2]).every(8, 'shuffle')

r4 >> dub([0,2,0,4], sus=1/8, amp=0.6, bits=8).every(16, 'shuffle').stop()

r5 >> play('x o [x o ]', drive=16, amp=0.5, room=2)
r5 >> play('----', drive=16, amp=0.5)

r6 >> pluck(dur=4, slide=1, slidedelay=0.5)





print(SynthDefs)

b2 >> swell(oct=2, dur=2, pan=[2, 3], amp=1.5)

s1 >> varsaw(p1.follow(), amp=0.7).every(8, "stutter", dur=2).stop()

s2 >> crunch(dur=[1/2, 1/2, 1, 2, 1/2], oct=2).stop()

s3 >> keys(dur=[8, 2 , 2, 4]).stop()

s4 >> pluck(dur=[1/2, 1/4, 2, 1]).stop()

s5 >> saw(dur=1/4, oct=3)

s6 >> ripple(amp=PSine(16), dur=1/2)

s7 >> play(' [--] ', dur=1/2)

s8 >> sitar(amp=[1, 0.7], sus=2, pan=PDur(2, 4), dur=[1/2, 1]).every(4, "bubble").stop()

s9 >> swell(dur=8, amp=1.1)
