#!/usr/bin/python2
from snake import *
from world import *
import time

X_LIMIT, Y_LIMIT = 0,0

def main():
	global X_LIMIT, Y_LIMIT
	try:
		X_LIMIT, Y_LIMIT = init_curses(50,50)
		
		global world
		world = World(1,X_LIMIT-2,7,Y_LIMIT-1)
		world.spawn_food_test()

		while(True):
			if check_input(world) == -1:
				break

			update()
			draw()
			time.sleep(0.1)

	except Exception, e:
		close_curses()
		raise
		
	finally:
		close_curses()
		
def update():
	world.update()
	
def draw():
	clear_screen()
	draw_pannel()
	world.draw()
	
def draw_pannel():
	y = 5
	draw_window_y(1, y)
	msg = "SCORE: " + str(world.score)
	draw_cur(2, y-1, msg)
	draw_cur(2, y-2, "use wasd to move or q to quit")
	limits_msg = "WINDOW LIMITS: " + str(X_LIMIT) + ":" + str(Y_LIMIT)
	draw_cur(2, y-3, limits_msg)


if __name__ == "__main__":
	main()
