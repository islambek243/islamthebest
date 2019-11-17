from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
colors = ['red','orange','yellow','green','blue'] # variants of colors

class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        if ((self.vy < 0) and (self.y >= 600 - self.r)):
            self.vy = -0.8 * self.vy 
        self.vy -= 2
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        
    def hittest(self, obj):
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** (1/2) <= (self.r + obj.r):
            return True

        return False
    def hit1(self):
        self.x = -1000
        self.y = 1000
        self.vx = 0
        self.vy = 0
        canv.coords(self.id, -1000, -1000, -1000, -1000)



class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)
    
    def fire2_start(self, event):
        global kek
        kek = 1
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

points = 0
c = canv.create_text(30,30,text = points,font = '28')
class target():
    def __init__(self):
        self.id = canv.create_oval(0,0,0,0)
        # self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(500, 750)
        y = self.y = rnd(200, 550)
        r = self.r = rnd(2, 50)
        self.vx = rnd(1, 5)
        self.vy = rnd(1, 5)
        color = self.color = choice(colors)
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self):
        """Попадание шарика в цель."""
        global points, c
        self.x = -50
        self.y = -50
        self.vx = 0
        self.vy = 0
        canv.coords(self.id, -50, -50, -50, -50)
        points += 1
        canv.itemconfig(c, text=points)
    def move(self):
        if ((self.vy < 0) and (self.y >= 600 - self.r)) or ((self.vy > 0) and (self.y <= self.r)):
            self.vy = -self.vy 
        if ((self.vx < 0) and (self.x <= 400 + self.r)) or ((self.vx > 0) and (self.x >= 800 - self.r)):
            self.vx = -self.vx
        
        self.x += self.vx
        self.y -= self.vy
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

 


screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
kek = 1
targets = []
for i in range(3):
    newtarget = target()
    targets += [newtarget]
def new_game(event=''):
    global gun, screen1, balls, bullet, kek, targets
    for i in range(3):
        targets[i].new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = 0.03
    live = 3
    while live > 0:
        if kek == 1:
            canv.itemconfig(screen1, text='')
        for b in balls:
            b.move()
            for t1 in targets:
                if b.hittest(t1):
                    live -= 1
                    kek = 0
                    t1.hit()
                    b.hit1()
        for t1 in targets:
            t1.move()
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
    for b in balls:
        b.hit1()
    canv.delete(gun)
    root.after(10, new_game)


new_game()

tk.mainloop()
