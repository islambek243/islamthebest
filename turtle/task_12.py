import turtle as t
t.shape('turtle')
def circle1():
	for  i in range(180):
		t.forward(0.8)
		t.right(1)
def circle2():
	for  i in range(180):
		t.forward(0.2)
		t.right(1)
t.left(90)
for i in range(10):
	circle1()
	circle2()