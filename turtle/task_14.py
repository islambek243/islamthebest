import turtle as t
t.shape('turtle')
def star(n):
	for i in range(n):
		t.forward(80)
		t.left(180-180/(n))
star(5)
t.penup()
t.goto(0,-100)
t.pendown()
star(11)