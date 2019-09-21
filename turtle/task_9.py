import turtle as t
import math
def triangle(i):
	for j in range(i + 3):
		t.forward((10 + 10*i)*math.sqrt(2 * (1 - math.cos(math.radians(360 / (3 + i))))))
		t.left(360/(3 + i))
t.shape('turtle')
for i in range(10):
	t.penup()
	t.forward(10)
	t.pendown()
	t.left(90 + 180 / (i + 3))
	triangle(i)
	t.right(90 + 180 / (i + 3))
