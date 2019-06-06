# https://www.youtube.com/watch?v=L0AsOacEvTY

Clock.bpm=120

# fg >> space(dur=4, oct=var([4.5, 4.3]), hpf=([18000, 400]), formant=P[:0], amp=3)
fg >> space(dur=PDur(8, 8), oct=var([4.5, 4.3]), hpf=([18000, 400]), formant=P[:0], amp=3)

# gg >> dirt(dur=PDur(1, 16))
# gg >> dirt(dur=PDur(3, 8))
gg >> dirt(dur=PDur(3, 8))

# jj >> pasha(dur=8, slide=linvar([.1, 0]), oct=4)
# jj >> pasha(dur=1, slide=linvar([.1, 0]), oct=4)
jj >> pasha(dur=PDur(3, 8), slide=linvar([.1, 0]), oct=4)

hu >> blip(dur=PDur(7,8))

jk >> play("V ")
