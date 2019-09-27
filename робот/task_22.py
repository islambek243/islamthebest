#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
	while wall_is_beneath() == 0:
		while wall_is_on_the_right() == 0:
			fill_cell()
			move_right()
			fill_cell()
		while wall_is_on_the_left() == 0:
			move_left()
		move_down()
	while wall_is_on_the_right() == 0:
			fill_cell()
			move_right()
			fill_cell()
	while wall_is_on_the_left() == 0:
			move_left()
if __name__ == '__main__':
    run_tasks()
