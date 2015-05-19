#!/usr/bin/python
from snake import *
import time

def main():
	try:
		snake = init_game()
		init_curses(10, 10)

		while(True):
			if check_input(snake) == -1:
				break

			snake.update()
			draw(snake)
			time.sleep(0.5)

	except Exception, e:
		close_curses()
		print e

	finally:
		close_curses()


def init_game():
	return Snake(20,10, 5)

def draw(snake):
	clear_screen()
	draw_window_y(1, 5)
	draw_cur(2, 2, " use wasd to move or q to quit")
	
	snake.draw()


if __name__ == "__main__":
	main()
