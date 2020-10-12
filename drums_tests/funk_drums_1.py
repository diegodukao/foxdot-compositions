Clock.bpm = 100
d1 >> play("xx..x.x.", dur=[1/2, 1/2, 1, 3/4, 1/4, 1/2, 1/4, 1/4], sample=3, amp=0.8).every([28,4], "trim", 4)
d2 >> play(".o", dur=1).every([28,4], "trim", 2)
d4 >> play("..oo.o..o.o", dur=[1, 1/2,1/4,1/4, 1/4,1/4,1/2, 1/4,1/4,1/4,1/4], amp=0.2).every([28,4], "trim", 4)
d3 >> play("-", dur=1/2)
d5 >> play("#" ,dur=32)

d1 >> play("xx..x.x.", dur=[1/2, 1/2, 1, 3/4, 1/4, 1/2, 1/4, 1/4], sample=3, amp=0.8)
d2 >> play(".o", dur=1)
d4 >> play("..oo.o..o.o", dur=[1, 1/2,1/4,1/4, 1/4,1/4,1/2, 1/4,1/4,1/4,1/4], amp=0.2)
d3 >> play("-", dur=1/2)
d5.stop()
