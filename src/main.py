#!/usr/bin/python2
from snake import *
from world import *
import time

X_LIMIT, Y_LIMIT = 0,0
SLEEP_TIME = 0

def main():
	global X_LIMIT, Y_LIMIT
	try:
		X_LIMIT, Y_LIMIT = init_curses(50,50)
		
		global world
		world = World(1,min(20, X_LIMIT-2),7,min(Y_LIMIT-1, 13))

		while(True):
			if check_input(world) == -1:
				break

			update()
			draw()
			global SLEEP_TIME
			
			SLEEP_TIME = max (0.1, 0.35 - 0.01 * world.score)
			time.sleep(SLEEP_TIME)

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
	dev_log = "[DEVLOG]"
	dev_log += " WINDOW LIMITS: " + str(X_LIMIT) + ":" + str(Y_LIMIT)
	dev_log += " SLEEP_TIME: " + str(SLEEP_TIME)
	draw_cur(2, y-3, dev_log)


if __name__ == "__main__":
	main()
