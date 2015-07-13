#!/usr/bin/python2
from snake import *
from world import *
import time

def main():
	try:
		#xlimit, ylimit = 50,50
		xlimit, ylimit = init_curses(100,30)
		
		global world
		world = World(0,xlimit,0,ylimit)

		while(True):
			if check_input(world) == -1:
				break

			world.update()
			world.draw()
			time.sleep(0.5)

	except Exception, e:
		close_curses()
		raise
		
	finally:
		close_curses()


if __name__ == "__main__":
	main()
