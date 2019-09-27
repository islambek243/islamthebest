#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
	while wall_is_on_the_right() == 0:
		move_right()
		if wall_is_above() == 0:
			while wall_is_above() == 0:
				move_up()
				fill_cell()
			while wall_is_beneath() == 0:
				fill_cell()
				move_down()
	while wall_is_beneath() == 1:
		move_left()
if __name__ == '__main__':
    run_tasks()
