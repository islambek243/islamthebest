import turtle as t
t.shape('turtle')
def circle():
	for  i in range(360):
		t.forward(1)
		t.left(1)
for j in range(6):
	circle()
	t.left(360/6)