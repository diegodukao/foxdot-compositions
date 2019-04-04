x1 >> blip([0, 5, 2, 3], dur=[1, 1/2, 1, 1/2, 1/2]).every(3, "offadd", 4).every(2, "stutter", 4, dur=3, oct=6)


x1 >> blip([0, 5, 2, 3], dur=[1, 1/2, 1, 1/2, 1/2]).every(3, "offadd", 4).every(2, "stutter", 4, dur=3, oct=6).every(8, "reverse")
