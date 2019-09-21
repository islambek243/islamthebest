import turtle as t
t.shape('turtle')
def circle1(r):
	for  i in range(360):
		t.forward(r)
		t.left(1)
def circle2(r):
	for  i in range(360):
		t.forward(r)
		t.right(1)
t.left(90)
for i in range(5):
	circle1(i/10 + 1)
	circle2(i/10 + 1)