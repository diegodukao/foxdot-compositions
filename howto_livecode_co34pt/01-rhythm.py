# https://theseanco.github.io/howto_co34pt_liveCode/3-2-Basic-Rhythms/#preamble-how-to-construct-rhythms

kd >> play("x", dur=1)

sn >> play("o", dur=2)

hh >> play("-", dur=1/4, amp=PWhite(0.25, 1))

cl >> play("*", dur=0.75, amp=0.6)

# not working
# oh >> play("=", dur=Pseq([0.5, Pseq([1], inf)], inf))
# sc:
#~oh = Pbind(\instrument,\bplay,\buf,d["oh"][0],\dur,Pseq([0.5,Pseq([1],inf)],inf),\amp,1);
# ~oh.play;

print(Samples)
