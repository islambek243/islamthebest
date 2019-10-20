from tkinter import *
from random import randrange as rnd, choice
import time
import math
root = Tk()
root.overrideredirect(1)
root.state('zoomed') # big window
global a, s, l, n, r, z, m
a = [] #list of objects
Button(root, text = "Quit", command = root.destroy, background = "#555", foreground = "#ccc").pack() # quit button
canv = Canvas(root,bg = 'white')
canv.pack(fill = BOTH,expand = 1)
colors = ['red','orange','yellow','green','blue'] # variants of colors
s = root.winfo_screenwidth() # sides if window
l = root.winfo_screenheight() # sides if window
d = dict(x = rnd(100, s - 100), y = rnd(100, l - 140), r = rnd(20, 60), c = choice(colors), vx = rnd(-5, 5), vy = rnd(-5, 5), fx = 0, fy = 0) # first object
a.append(d) # add object to list
n = 0
def move_ball(): # move all objects function
	global s, l, n, a, z, m
	z = 0
	canv.delete(ALL)
	for i in range(n + 1):
		z += (a[i]['vx'] ** 2 + a[i]['vy'] ** 2) * (a[i]['r'] ** 2)
		g = min(a[i]['x'], a[i]['y'], s - a[i]['x'], l - 40 - a[i]['y']) # min of distance to the sides of window
		a[i]['fx'] = 0
		a[i]['fy'] = 0
		for j in range(n + 1):
			if i == j:
				continue
			if ((a[i]['x'] - a[j]['x']) ** 2 + (a[i]['y'] - a[j]['y']) ** 2) < (a[i]['r'] + a[j]['r']) ** 2:
				u = 2 * (10 ** 10)/((a[i]['x'] - a[j]['x']) ** 2 + (a[i]['y'] - a[j]['y']) ** 2) # forse
				a[i]['fx'] += -0.5 * a[i]['vx'] * math.fabs(a[i]['vx']) - 0.005 * u / (a[i]['r'] ** 2) * ((a[j]['x'] - a[i]['x'])/math.sqrt((a[i]['x'] - a[j]['x']) ** 2 + (a[i]['y'] - a[j]['y']) ** 2))
				a[i]['fy'] += -0.5 * a[i]['vy'] * math.fabs(a[i]['vy']) - 0.005 * u / (a[i]['r'] ** 2) * ((a[j]['y'] - a[i]['y'])/math.sqrt((a[i]['x'] - a[j]['x']) ** 2 + (a[i]['y'] - a[j]['y']) ** 2))
				canv.create_line(a[i]['x'], a[i]['y'], a[i]['x'] - 200 * ((a[j]['x'] - a[i]['x'])/math.sqrt((a[i]['x'] - a[j]['x']) ** 2 + (a[i]['y'] - a[j]['y']) ** 2)), a[i]['y'] - 200 * ((a[j]['y'] - a[i]['y'])/math.sqrt((a[i]['x'] - a[j]['x']) ** 2 + (a[i]['y'] - a[j]['y']) ** 2)))
				canv.create_line(a[i]['x'], a[i]['y'], a[j]['x'], a[j]['y'])
		if g < a[i]['r']: # chek for critical distanse to wall
			if (g == a[i]['x'] and a[i]['vx'] < 0) or (g == s - a[i]['x'] and a[i]['vx'] > 0):
				a[i]['vx'] = -a[i]['vx']
			elif (g == a[i]['y'] and a[i]['vy'] < 0) or (g == l - 40 - a[i]['y'] and a[i]['vy'] > 0):
				a[i]['vy'] = -a[i]['vy']
	for i in range(n + 1):
		a[i]['x'] += a[i]['vx'] * 0.3 #changing coordinates
		a[i]['y'] += a[i]['vy'] * 0.3 #changing coordinates
		a[i]['vx'] += a[i]['fx'] * 0.1 #changing velocity
		a[i]['vy'] += a[i]['fy'] * 0.1 #changing velocity
		canv.create_oval(a[i]['x'] - a[i]['r'], a[i]['y'] - a[i]['r'], a[i]['x'] + a[i]['r'], a[i]['y'] + a[i]['r'], fill = a[i]['c'], width = 0)
	m = z / (100 * (n + 1))
	root.after(2, move_ball)
label = Label(text = 'нажимайте на шарики чтобы появлялись новые', fg = "#eee", bg = "#333") # printing points
label.pack()
def click(event): # chek clicking
	global a, s, l, n, m
	t = 0
	for i in range(n + 1):
		if ((a[i]['x'] - event.x) ** 2 + (a[i]['y'] - event.y) ** 2) < a[i]['r'] ** 2:
			t = 1
	if t == 1:
		n += 1 #number of clicks
		d = dict(x = rnd(100, s - 100), y = rnd(100, l - 140), r = rnd(20, 60), c = choice(colors), vx = rnd(-5, 5), vy = rnd(-5, 5), fx = 0, fy = 0) # creating of new object
		a.append(d) #adding new object to list
	label['text'] = str(m) + ' Кельвин' # print result
move_ball()
canv.bind('<Button-1>', click)
mainloop()