from graph import *
import math
def kepler1(x, y, a, b):
	moveTo(x - 0.5 * b * math.cos(a), y - 0.5 * b * math.sin(a))
	x0 = - 0.5 * b * math.cos(a)
	y0 = 0;
	for i in range(int(b * math.cos(a))):
		x0 = i - 0.5 * b * math.cos(a)
		y0 = 0.5 * math.sqrt(0.25 * b * b - x0 * x0)
		line(x + x0 * math.cos(a) + y0 * math.sin(a), y + x0 * math.sin(a) - y0 * math.cos(a), x + x0 * math.cos(a) - y0 * math.sin(a), y + x0 * math.sin(a) + y0 * math.cos(a))
def kepler2(x, y, a, b):
	moveTo(x - 0.5 * b * math.cos(a), y - 0.5 * b * math.sin(a))
	x0 = - 0.5 * b * math.cos(a)
	y0 = 0;
	for i in range(int(b * math.cos(a))):
		x0 = i - 0.5 * b * math.cos(a)
		y0 = 0.5 * math.sqrt(0.25 * b * b - x0 * x0)
		point(x + x0 * math.cos(a) + y0 * math.sin(a), y + x0 * math.sin(a) - y0 * math.cos(a))
		point(x + x0 * math.cos(a) - y0 * math.sin(a), y + x0 * math.sin(a) + y0 * math.cos(a))
def flower(x, y, a, b):
	penColor("white")
	kepler1(x + math.sin(a) * b / 5 - math.cos(a) * b / 5, y - math.cos(a) * b / 5 - math.sin(a) * b / 5, a, b)
	penColor("black")
	kepler2(x + math.sin(a) * b / 5 - math.cos(a) * b / 5, y - math.cos(a) * b / 5 - math.sin(a) * b / 5, a, b)
	penColor("white")
	kepler1(x + math.sin(a) * 0.08 * b - math.cos(a) * 0.6 * b, y - math.cos(a) * 0.08 * b - math.sin(a) * 0.6 * b, a, b)
	penColor("black")
	kepler2(x + math.sin(a) * 0.08 * b - math.cos(a) * 0.6 * b, y - math.cos(a) * 0.08 * b - math.sin(a) * 0.6 * b, a, b)
	penColor("white")
	kepler1(x + math.sin(a) * 0.12 * b + math.cos(a) * 0.4 * b, y - math.cos(a) * 0.12 * b + math.sin(a) * 0.4 * b, a, b)
	penColor("black")
	kepler2(x + math.sin(a) * 0.12 * b + math.cos(a) * 0.4 * b, y - math.cos(a) * 0.12 * b + math.sin(a) * 0.4 * b, a, b)
	penColor("yellow")
	kepler1(x, y, a, b)
	penColor("black")
	kepler2(x, y, a, b)
	penColor("white")
	kepler1(x + math.cos(a) * 0.7 * b, y + math.sin(a) * b, a, b)
	penColor("black")
	kepler2(x + math.cos(a) * 0.7 * b, y + math.sin(a) * b, a, b)
	penColor("white")
	kepler1(x - math.sin(a) * 0.15 * b - math.cos(a) * 0.8 * b, y + math.cos(a) * 0.15 * b + math.sin(a) * 0.8 * b, a, b)
	penColor("black")
	kepler2(x - math.sin(a) * 0.15 * b - math.cos(a) * 0.8 * b, y + math.cos(a) * 0.15 * b + math.sin(a) * 0.8 * b, a, b)
	penColor("white")
	kepler1(x - math.sin(a) * 0.3 * b - math.cos(a) * 0.3 * b, y + math.cos(a) * 0.3 * b + math.sin(a) * 0.3 * b, a, b)
	penColor("black")
	kepler2(x - math.sin(a) * 0.3 * b - math.cos(a) * 0.3 * b, y + math.cos(a) * 0.3 * b + math.sin(a) * 0.3 * b, a, b)
	penColor("white")
	kepler1(x - math.sin(a) * 0.25 * b + math.cos(a) * 0.3 * b, y + math.cos(a) * 0.25 * b - math.sin(a) * 0.3 * b, a, b)
	penColor("black")
	kepler2(x - math.sin(a) * 0.25 * b + math.cos(a) * 0.3 * b, y + math.cos(a) * 0.25 * b - math.sin(a) * 0.3 * b, a, b)

def green(x, y, r, l):
	brushColor(119,212,61)
	penColor(119,212,61)
	circle(x, y, r)
	if l == 1:
		flower(x + 3 * (r / 66), y - 39 * (r / 66), 0, 15 * (r / 66))
		flower(x - 35 * (r / 66), y - 30 * (r / 66), -0.1, 13 * (r / 66))
		flower(x + 33 * (r / 66), y - 17 * (r / 66), 0, 20 * (r / 66))
		flower(x - 30 * (r / 66), y - 7 * (r / 66), 0, 15 * (r / 66))
		flower(x - 3 * (r / 66), y + 17 * (r / 66), 0, 18 * (r / 66))
		flower(x + 42 * (r / 66), y + 15 * (r / 66), 0, 15 * (r / 66))
		brushColor("black")
		polygon([(0,0),(75,0),(75,500),(0,500)])
		polygon([(425,0),(500,0),(500,500),(425,500)])
	if l == 2:
		flower(x - 3 * (r / 66), y - 39 * (r / 66), 0, 15 * (r / 66))
		flower(x + 35 * (r / 66), y - 30 * (r / 66), -0.1, 13 * (r / 66))
		flower(x - 33 * (r / 66), y - 17 * (r / 66), 0, 20 * (r / 66))
		flower(x + 30 * (r / 66), y - 7 * (r / 66), 0, 15 * (r / 66))
		flower(x + 3 * (r / 66), y + 17 * (r / 66), 0, 18 * (r / 66))
		flower(x - 42 * (r / 66), y + 15 * (r / 66), 0, 15 * (r / 66))
		brushColor("black")
		polygon([(0,0),(75,0),(75,500),(0,500)])
		polygon([(425,0),(500,0),(500,500),(425,500)])
	
def lama(x, y, b, l):
	brushColor("white")
	penColor("white")
	changeCoords(circle(0, 0, 14), [(x - b / 2, y - b / 4), (x + b / 2, y + b / 4)])
	if l == 1: 
		changeCoords(circle(0, 0, 14), [(x - 0.32 * b, y - b / 6), (x - 0.15 * b, y + 0.4 * b)]) 
		changeCoords(circle(0, 0, 14), [(x - 0.32 * b, y + 0.4 * b), (x - 0.14 * b, y + 0.8 * b)]) 
		changeCoords(circle(0, 0, 14), [(x - 0.24 * b, y + 0.8 * b), (x - 0.05 * b, y + 0.9 * b)]) 
		
		changeCoords(circle(0, 0, 14), [(x + 0.25 * b, y - b / 6), (x + 0.43 * b, y + 0.4 * b)]) 
		changeCoords(circle(0, 0, 14), [(x + 0.25 * b, y + 0.4 * b), (x + 0.43 * b, y + 0.8 * b)]) 
		changeCoords(circle(0, 0, 14), [(x + 0.33 * b, y + 0.8 * b), (x + 0.5 * b, y + 0.9 * b)]) 
		
		changeCoords(circle(0, 0, 14), [(x - 0.48 * b, y - b / 8), (x - 0.33 * b, y + 0.4 * b)]) 
		changeCoords(circle(0, 0, 14), [(x - 0.48 * b, y + 0.4 * b), (x - 0.33 * b, y + 0.7 * b)]) 
		changeCoords(circle(0, 0, 14), [(x - 0.4 * b, y + 0.7 * b), (x - 0.23 * b, y + 0.8 * b)]) 
		
		changeCoords(circle(0, 0, 14), [(x + 0.09 * b, y - b / 8), (x + 0.24 * b, y + 0.4 * b)]) 
		changeCoords(circle(0, 0, 14), [(x + 0.09 * b, y + 0.4 * b), (x + 0.24 * b, y + 0.7 * b)]) 
		changeCoords(circle(0, 0, 14), [(x + 0.13 * b, y + 0.7 * b), (x + 0.3 * b, y + 0.8 * b)]) 
		
		changeCoords(circle(0, 0, 14), [(x + 0.3 * b, y - 0.1 * b), (x + 0.55 * b, y - 0.85 * b)])

		changeCoords(circle(0, 0, 14), [(x + 0.31 * b, y - 0.82 * b), (x + 0.7 * b, y - 1.02 * b)])
		
		polygon([(x + 0.31 * b, y - 0.97 * b), (x + 0.29 * b, y - 1 * b), (x + 0.27 * b, y - 1.04 * b), (x + 0.26 * b, y - 1.09 * b), (x + 0.25 * b, y - 1.2 * b), (x + 0.31 * b, y - 1.06 * b), (x + 0.38 * b, y - 0.98 * b)])
		polygon([(x + 0.39 * b, y - 0.97 * b), (x + 0.37 * b, y - 1 * b), (x + 0.35 * b, y - 1.04 * b), (x + 0.34 * b, y - 1.09 * b), (x + 0.33 * b, y - 1.2 * b), (x + 0.39 * b, y - 1.06 * b), (x + 0.46 * b, y - 0.98 * b)])
		brushColor("violet")
		circle(x + 0.47 * b, y - 0.94 * b, 0.07 * b)
		brushColor("black")
		penColor("violet")
		circle(x + 0.5 * b, y - 0.94 * b, 0.03 * b)
		penColor("white")
		kepler1(x + 0.46 * b, y - 0.96 * b, 0.5, 0.08 * b)
	if l == 2:
		changeCoords(circle(0, 0, 14), [(x + 0.32 * b, y - b / 6), (x + 0.15 * b, y + 0.4 * b)]) 
		changeCoords(circle(0, 0, 14), [(x + 0.32 * b, y + 0.4 * b), (x + 0.14 * b, y + 0.8 * b)]) 
		changeCoords(circle(0, 0, 14), [(x + 0.24 * b, y + 0.8 * b), (x + 0.05 * b, y + 0.9 * b)]) 
		
		changeCoords(circle(0, 0, 14), [(x - 0.25 * b, y - b / 6), (x - 0.43 * b, y + 0.4 * b)]) 
		changeCoords(circle(0, 0, 14), [(x - 0.25 * b, y + 0.4 * b), (x - 0.43 * b, y + 0.8 * b)]) 
		changeCoords(circle(0, 0, 14), [(x - 0.33 * b, y + 0.8 * b), (x - 0.5 * b, y + 0.9 * b)]) 
		
		changeCoords(circle(0, 0, 14), [(x + 0.48 * b, y - b / 8), (x + 0.33 * b, y + 0.4 * b)]) 
		changeCoords(circle(0, 0, 14), [(x + 0.48 * b, y + 0.4 * b), (x + 0.33 * b, y + 0.7 * b)]) 
		changeCoords(circle(0, 0, 14), [(x + 0.4 * b, y + 0.7 * b), (x + 0.23 * b, y + 0.8 * b)]) 
		
		changeCoords(circle(0, 0, 14), [(x - 0.09 * b, y - b / 8), (x - 0.24 * b, y + 0.4 * b)]) 
		changeCoords(circle(0, 0, 14), [(x - 0.09 * b, y + 0.4 * b), (x - 0.24 * b, y + 0.7 * b)]) 
		changeCoords(circle(0, 0, 14), [(x - 0.13 * b, y + 0.7 * b), (x - 0.3 * b, y + 0.8 * b)]) 
		
		changeCoords(circle(0, 0, 14), [(x - 0.3 * b, y - 0.1 * b), (x - 0.55 * b, y - 0.85 * b)])

		changeCoords(circle(0, 0, 14), [(x - 0.31 * b, y - 0.82 * b), (x - 0.7 * b, y - 1.02 * b)])
		
		polygon([(x - 0.31 * b, y - 0.97 * b), (x - 0.29 * b, y - 1 * b), (x - 0.27 * b, y - 1.04 * b), (x - 0.26 * b, y - 1.09 * b), (x - 0.25 * b, y - 1.2 * b), (x - 0.31 * b, y - 1.06 * b), (x - 0.38 * b, y - 0.98 * b)])
		polygon([(x - 0.39 * b, y - 0.97 * b), (x - 0.37 * b, y - 1 * b), (x - 0.35 * b, y - 1.04 * b), (x - 0.34 * b, y - 1.09 * b), (x - 0.33 * b, y - 1.2 * b), (x - 0.39 * b, y - 1.06 * b), (x - 0.46 * b, y - 0.98 * b)])
		brushColor("violet")
		circle(x - 0.47 * b, y - 0.94 * b, 0.07 * b)
		brushColor("black")
		penColor("violet")
		circle(x - 0.5 * b, y - 0.94 * b, 0.03 * b)
		penColor("white")
		kepler1(x - 0.46 * b, y - 0.96 * b, -0.5, 0.08 * b)
	
		
brushColor("black")
polygon([(0,0),(500,0),(500,500),(0,500),(0,0)])
brushColor("white")
polygon([(75,0),(425,0),(425,500),(75,500),(75,0)])
brushColor(143,242,241)
polygon([(75,0),(425,0),(425,20),(365,80),(345,60),(280,200),(200,60),(150,120),(120,40),(75,160)])
brushColor(182,191,191)
polygon([(425,20),(365,80),(345,60),(280,200),(200,60),(150,120),(120,40),(75,160),(75,500),(425,500)])
brushColor(185,237,152)
polygon([(75,260),(91,252),(107,248),(119,248),(147,240),(255,240),(257,242),(261,242),(265,247),(265,255),(267,257),(267,281),(279,285),(425,285),(425,500),(75,500)])
brushColor(119,212,61)
green(372,420, 66, 1)


lama(160, 328, 80, 1)
run()