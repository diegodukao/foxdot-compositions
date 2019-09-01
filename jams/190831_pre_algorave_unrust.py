# heavily based on reference 09-qirky-driving_force.py

Scale.default = "minor"

b1 >> fuzz([0, 2, 3, 5], dur=1/2, amp=0.8,  lpf=linvar([100, 1000], 12), lpr=0.2, oct=3).every(16, "shuffle").every(8, "bubble")

p1 >> bass([0, 6, 4, 2, 2, 4], dur=[1, 1, 1, 1/4, 1/4, 1/2], sus=1/4).every(12, "shuffle")

p2 >> karp([0, 2, 3, 7, 9], dur=[1/2, 1, 1/2, 1, 1, 1/2]).every(12, "shuffle").every(7, "bubble")

d1 >> play("XXoX")

d2 >> play("[--]", amp=[1.3, 0.5, 0.5, 0.5], hpf=linvar([6000, 10000], 8), hpr=0.4, spin=4, dur=1/2)


p1.every(2, "stutter", 4)

b1.every(8, "rotate") 
