#!/usr/bin/python
from snake import *
import curses
import time

def main():
	snake = init_game()
	init_curses()
	stdscr.addstr(" use wasd to move or q to quit")

	while(True):
		if check_input(snake) == -1:
			break

		snake.update()
		draw(snake)
		time.sleep(0.1)

	close_curses()


def init_game():
	return Snake(2,2)

def draw(snake):
	stdscr.addstr(2,2, snake.toString())


def init_curses():
	global stdscr
	stdscr = curses.initscr()
	
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)
	stdscr.nodelay(1)
	

def check_input(snake):
	c = stdscr.getch()

	if c == ord('w'):
		snake.turn(0,1)

	elif c == ord('a'):
		snake.turn(-1,0)

	elif c == ord('s'):
		snake.turn(0,-1)

	elif c == ord('d'):
		snake.turn(1,0)
		
	elif c == ord('q'):
		return -1


def close_curses():
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()


if __name__ == "__main__":
	main()
