Scale.default = "minor"
Clock.bpm = 150


d1 >> play("X O( [ X])")
d2 >> play("----", dur=1/2)
d3 >> play("[^^]  ( [~~]) ")
d4 >> play("x")
d5 >> play("!       ")
d6 >> play("     2  ")
d7 >> play("      [xx] X o")


print(SynthDefs)