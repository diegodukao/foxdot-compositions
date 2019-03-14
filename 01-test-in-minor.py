Scale.default.set("minor")

d1 >> play("--------")

d2 >> play("X(X )O X O( [XO])")

b1 >> bass(P[0:10:2], dur=[2, 1/2, 1, 1/2])
b1.every(4, "reverse")

v1 >> viola(P[0:10:2], dur=P[1,1/2,1].stutter([4,2,3]))
v1.every(4, "shuffle")
