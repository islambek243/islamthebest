#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
	for i in range(0,14):
		for j in range(0,15):
			a = wall_is_on_the_right()
			b = wall_is_on_the_left()
			c = wall_is_above()
			d = wall_is_beneath()
			if (i - j) >= 0 and (a + b + c + d) == 0:
				fill_cell()
			if j < 14:
				move_right()
		for j in range(0,14):
			move_left()
		move_down()
	move_right()

			


if __name__ == '__main__':
    run_tasks()
