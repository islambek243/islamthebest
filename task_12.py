#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
	while wall_is_on_the_right() == False:
		if wall_is_above() == 0 and wall_is_beneath() == 1:
			fill_cell()
		move_right()
		if wall_is_above() == 0 and wall_is_beneath() == 1:
			fill_cell()



if __name__ == '__main__':
    run_tasks()