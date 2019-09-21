import turtle as t
t.shape('turtle')
for i in range(10):
	t.forward(10+4*i)
	t.left(90)
	t.forward(10+4*i)
	t.left(90)
	t.forward(10+4*i)
	t.left(90)
	t.forward(10+4*i+2)
	t.right(90)
	t.forward(2)
	t.right(180)