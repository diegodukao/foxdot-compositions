# https://github.com/Qirky/ten-lines-or-less/blob/master/crazed_baboon.py

b1 >> fuzz([0, 2, 3, 5, 7, 9], dur=[1/2, 1, 1/4, 1/4, 1, 1, 1/2])
k1 >> play("x ").every(4, "amen")
h1 >> play("- - -- -- [--]  ", amp=1.4)
s1 >> play("     o     o oo     [oo]", amp=0.8)
b2 >> bass([0, 12, 7, 9], dur=[1, 1, 1/2, 1, 1/2], oct=3, dist=0.3, amp=0.7).every(8, "shuffle")
Clock.every(16, lambda: b1.shuffle())
Clock.every(12, lambda: s1.shuffle())
