#!/usr/bin/python
import curses
import os
import time

###########
# CURSES #
##########

X_LIM = 0
Y_LIM = 0

X_TERM_LIM = 0
Y_TERM_LIM = 0


def init_curses(x_limit, y_limit):
	global X_LIM, Y_LIM
	
	global stdscr
	stdscr = curses.initscr()

	curses.use_env(True)
	Y_LIM, X_LIM = stdscr.getmaxyx()

	print X_LIM, Y_LIM

	time.sleep(1)
	
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)
	stdscr.nodelay(1)


def check_input(snake):
	global stdscr
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
	global stdscr
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()

def clear_screen():
	stdscr.clear()

def draw_window(x1,y1,x2,y2):
	line = "#"* (x2-x1)
	col = "#\n" * (y2-y1)

	draw_cur(x1,y1, line)
	draw_cur(x1,y2, line)

	for i in xrange(y1,y2+1):
		draw_cur(x1,i, "#")
		draw_cur(x2,i, "#")

def draw_window_y(y1, y2):
	x1 = 0
	x2 = X_LIM

	draw_window(x1, y1, x2-1, y2)
		

def draw_cur(x, y, msg):
	real_x = x
	real_y = Y_LIM - y

	if real_x < 0:
		real_x = 0

	if real_x > X_LIM:
		real_x = X_LIM

	if real_y < 0:
		real_y = 0

	if real_y > Y_LIM:
		real_y = Y_LIM
	
	try:
		stdscr.addstr(real_y, real_x, msg)

	except:
		pass


##########
# OTHERS #
##########

class Vec2:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def add(self, vec2):
		self.x += vec2.x
		self.y += vec2.y

	def toString(self):
		return "x: %d, y: %d" %(self.x,self.y)



if __name__ == "__main__":
	pass
