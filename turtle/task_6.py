import turtle as t
t.shape('turtle')
n = input()
for i in range(int(n)):
	t.forward(30)
	t.right(180)
	t.forward(30)
	t.right(180)
	t.left(360/int(n))