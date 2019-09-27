#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	a = 0
	while wall_is_beneath() == 0:
		while wall_is_on_the_right() == 0:
			move_right()
			if wall_is_on_the_right() == 0 and a <= 11:
				fill_cell()
		while wall_is_on_the_left() == 0:
			move_left()
		move_down()
		a = a + 1
	move_up()
	move_right()

if __name__ == '__main__':
    run_tasks()
