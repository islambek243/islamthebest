import turtle as t
import math
t.shape('turtle')
f1 = 1
f2 = 0
r = 5
dr = 0
df2 = 0
df1 = 0
t.speed(100)
for i in range(5000):
	t.forward(2)
	dr = 2 * math.cos(math.radians(f1-f2))
	df2 = math.degrees(2 * math.sin(math.radians(f1-f2))/r)
	df1 = 7.9*math.degrees(math.atan(r+dr)-math.atan(r))+df2
	r += dr
	f1 += df1
	f2 += df2
	t.left(df1)

