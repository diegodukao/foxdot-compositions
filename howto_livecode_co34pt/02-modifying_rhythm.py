# https://theseanco.github.io/howto_co34pt_liveCode/3-3-Techniques-For-Modifying-Rhythm/

# Total random rhythm sounds unpleasant
sn >> play("o", dur=PWhite(1, 5))
hh >> play("-", dur=PWhite(0.25, 0.75), amp=PWhite(0.2, 1))
cl >> play("*", dur=PWhite(0.75, 2), amp=PWhite(0.2, 1))
tm >> play("M", dur=PWhite(1, 5))

# regular kick doesn't save it
kd >> play("x", dur=1)

# PWhite.round doesn't exist in FoxDot
# sc:
# //same example again
# (
# ~sn = Pbind(\instrument,\bplay,\buf,d["s"][0],\dur,Pwhite(1,5.0).round(1),\amp,1);
# ~h = Pbind(\instrument,\bplay,\buf,d["ch"][0],\dur,Pwhite(0.25,0.75).round(0.25),\amp,Pwhite(0.2,1));
# ~c = Pbind(\instrument,\bplay,\buf,d["c"][0],\dur,Pwhite(0.75,2).round(0.75),\amp,1);
# ~t = Pbind(\instrument,\bplay,\buf,d["t"][0],\dur,Pwhite(1,5.0).round(0.5),\amp,1);
# ~k = Pbind(\instrument,\bplay,\buf,d["k"][0],\dur,1,\amp,1);
# ~sn.play;~h.play;~c.play;~t.play;~k.play;
# )
# //added whole note fx, short, medium and long.
# (
# ~fx1 = Pbind(\instrument,\bplay,\buf,d["sfx"][0],\dur,Pwhite(1,5),\amp,1);
# ~fx2 = Pbind(\instrument,\bplay,\buf,d["fx"][0],\dur,Pwhite(1,10),\amp,1);
# ~fx3 = Pbind(\instrument,\bplay,\buf,d["lfx"][0],\dur,Pwhite(10,40),\amp,1);
# ~fx1.play;~fx2.play;~fx3.play;
# )


## LAYERING

Clock.bpm = 80

k1 >> play("x", dur=PDur(3, 8)/4, rate=[1, 1.2])
k2 >> play("x", dur=PDur(3, 8)/4, rate=[1, 1.8])

# //layering at different pitches - kicks
# (
# p.clock.tempo = 2.3;
# ~k = Pbind(\instrument,\bplay,\buf,d["k"][0],\dur,Pbjorklund2(3,8)/4,\amp,1,\rate,Pseq([1,1.2],inf));
# ~k.play;
# )
# //kicks at a different pitch. Evaluate this a few times to get different permutations
# (
# ~k2 = Pbind(\instrument,\bplay,\buf,d["k"][0],\dur,Pbjorklund2(3,8)/4,\amp,1,\rate,Pseq([1,1.8],inf)*4);
# ~k2.play;
# )
