#!/usr/bin/python
from snake import *
import time

def main():
	snake = init_game()
	init_curses(10, 10)

	while(True):
		if check_input(snake) == -1:
			break

		snake.update()
		draw(snake)
		time.sleep(0.5)

	close_curses()


def init_game():
	return Snake(20,10)

def draw(snake):
	clear_screen()
	draw_cur(2, 2, " use wasd to move or q to quit")
	
	x = snake.getX()
	y = snake.getY()

	draw_cur(x, y, ".")


if __name__ == "__main__":
	main()
