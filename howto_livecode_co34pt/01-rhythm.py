# https://theseanco.github.io/howto_co34pt_liveCode/3-2-Basic-Rhythms/#preamble-how-to-construct-rhythms

kd >> play("x", dur=1, amp=0.6)
sn >> play("o", dur=2, amp=1)
hh >> play("-", dur=1/4, amp=PWhite(0.25, 1))
cl >> play("*", dur=0.75, amp=0.6)
oh >> play("=", dur=P[0.5, 1])

# why one Pseq inside another? how does it change the sound?
# sc:
#~oh = Pbind(\instrument,\bplay,\buf,d["oh"][0],\dur,Pseq([0.5,Pseq([1],inf)],inf),\amp,1);
# ~oh.play;

print(Samples)
