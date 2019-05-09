
Clock.bpm = 100

Scale.default = "minor"
Root.default = "g"

# there's no way to set a default octave
# none of these work
Scale.default.oct = 4
Root.default.oct = 4
Root.oct = 4

b1 >> bass([0, 2, 4], dur=[1, 1/2, 1/2], oct=4)

# d1 >> play("xxx", dur=[1, 1/2, 1/2])


