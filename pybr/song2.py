# Diego Moreira Guimarães
# @diegodukao
# Música com FoxDot - Python Brasil 2019

# samples, every, offadd, stutter

# dó | ré | mi | fá | sol | lá | si
# C  | D  | E  | F  | G   | A  | B

p1 >> piano(P[0:7]).every(2, "offadd", 3).every(1, "shuffle")


d1 >> play("x o ")
d2 >> play("-", dur=1/2)
