from tkinter import *
from random import randrange as rnd, choice
import time
import math
root = Tk()
root.overrideredirect(1)
root.state('zoomed') #big window
global a, s, l, n, f, q, w, r
q = 0 #pushes on circles
w = -1 #pushes on squares
a = [] #list of objects
p = ['circle', 'square'] #variants of objects
r = open('winners.txt', 'a') #record file
def click_button(): #record button function
	r.write(str(q) + ' ' + str(w) + '\n')
	r.close()
btn = Button(text="save record", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button) #record button
btn.pack()
Button(root, text = "Quit", command = root.destroy, background = "#555", foreground = "#ccc").pack() #quit button
canv = Canvas(root,bg = 'white')
canv.pack(fill = BOTH,expand = 1)
colors = ['red','orange','yellow','green','blue'] #variants of colors
s = root.winfo_screenwidth() #sides if window
l = root.winfo_screenheight() #sides if window
d = dict(x = rnd(100, s - 100), y = rnd(100, l - 140), r = rnd(30, 50), c = choice(colors), a = rnd(0, 360), f = p[0]) #first object that is circle
a.append(d) #add object to list
n = 0
def move_ball(): #move all objects function
	global s, l, n, a
	canv.delete(ALL)
	for i in range(n + 1):
		g = min(a[i]['x'], a[i]['y'], s - a[i]['x'], l - 40 - a[i]['y']) # min of distance to the sides of window
		if g < a[i]['r']: # chek for critical distanse
			if g == a[i]['x']:
				a[i]['a'] = rnd(0, 180) + 270
			elif g == a[i]['y']:
				a[i]['a'] = rnd(0, 180) + 180
			elif g == s - a[i]['x']:
				a[i]['a'] = rnd(0, 180) + 90
			elif g == l - 40 - a[i]['y']:
				a[i]['a'] = rnd(0, 180)
		if a[i]['f'] == 'square':
			a[i]['a'] += 0.1 * (rnd(0, 30) - 10) * rnd(0, 3)
		a[i]['x'] += 4 * math.cos(math.pi * a[i]['a'] / 180) #changing coordinates
		a[i]['y'] -= 4 * math.sin(math.pi * a[i]['a'] / 180) #changing coordinates
		if a[i]['f'] == 'circle': # painting object circle
			canv.create_oval(a[i]['x'] - a[i]['r'], a[i]['y'] - a[i]['r'], a[i]['x'] + a[i]['r'], a[i]['y'] + a[i]['r'], fill = a[i]['c'], width = 0)
		else: # painting object square
			canv.create_rectangle(a[i]['x'] - a[i]['r'],a[i]['y'] - a[i]['r'],a[i]['x'] + a[i]['r'],a[i]['y']+a[i]['r'], fill = a[i]['c'], outline = a[i]['c'])
	root.after(5, move_ball)
label = Label(text = str(q), fg = "#eee", bg = "#333") # printing points
label.pack()
def click(event): # chek clicking
	global a, s, l, n, q, w
	t1 = 0 # chek clicking on circles
	t2 = 0 # chek clicking on squares
	for i in range(n + 1):
		if a[i]['f'] == 'circle':
			if ((a[i]['x'] - event.x) ** 2 + (a[i]['y'] - event.y) ** 2) < a[i]['r'] ** 2:
				t1 = 1
		else:
			if ((a[i]['x'] - event.x) ** 2 < a[i]['r'] ** 2) and ((a[i]['y'] - event.y) ** 2 < a[i]['r'] ** 2):
				t2 = 1
	if t1 + t2 >= 1:
		n += 1 #number of clicks
		d = dict(x = rnd(100, s - 100), y = rnd(100, l - 140), r = rnd(30, 50), c = choice(colors), a = rnd(0, 360), f = p[rnd(0,2)]) #creating of new object
		a.append(d) #adding new object to list
		if t1 == 1:
			q += 1 # number of clicking on circles
		elif t2 == 1:
			w += 1 # number of clicking on squares
		if w == -1:
			label['text'] = str(q) # print result
		else:
			label['text'] = str(q) + ' ' + str(w) # print result
move_ball()
canv.bind('<Button-1>', click)
mainloop()