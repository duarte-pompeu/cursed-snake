#!/usr/bin/python
import curses
import time
import random

MIN_X = 2
MAX_X = 39
MIN_Y = 2
MAX_Y = 10
SCORE = 0
FOOD_X = 0
FOOD_Y = 0
ANGLE = 0
X = 5
Y = 5
X_SPEED = 0
Y_SPEED = 0

def spawn_food():
	global FOOD_X, FOOD_Y

	FOOD_X = random.randint(MIN_X, MAX_X)
	FOOD_Y = random.randint(MIN_Y, MAX_Y)
	
	food_types = ".,@$%"
	food_type = food_types[random.randint(0,len(food_types)-1)]
	stdscr.addstr(FOOD_Y, FOOD_X, food_type)

def init_game():
	global SCORE, FOOD_X, FOOD_Y, ANGLE, X, Y, X_SPEED, Y_SPEED
	SCORE = 0
	FOOD_X = 0
	FOOD_Y = 0
	ANGLE = 0
	X = 5
	Y = 5
	X_SPEED = 0
	Y_SPEED = 0
	
	spawn_food()
	
def clear_scenario():
	xlen = MAX_X - MIN_X +1
	for i in range(MIN_Y, MAX_Y+1):
		stdscr.addstr(i, MIN_X, " " * xlen)

def update():
	global X, Y, X_SPEED, Y_SPEED, SCORE, HEAD, ANGLE
	
	c = stdscr.getch()
	if (c == ord('w')):
		X_SPEED = 0
		Y_SPEED = -1
		ANGLE = 1
		
	if (c == ord('s')):
		X_SPEED = 0
		Y_SPEED = 1
		ANGLE = 3
		
	if (c == ord('a')):
		Y_SPEED = 0
		X_SPEED = -1
		ANGLE = 2
		
	if (c == ord('d')):
		Y_SPEED = 0
		X_SPEED = 1
		ANGLE = 0
		
	if (c == ord('q')):
		return -1
	
	X+= X_SPEED
	Y+= Y_SPEED
	if(Y < MIN_Y or Y > MAX_Y or X < MIN_X or X > MAX_X):
		return 0
		
	if(X == FOOD_X and Y == FOOD_Y):
		SCORE += 1
		spawn_food()
			
def draw_borders():
	border = "#"
	stdscr.addstr(1,1, border*40)
	stdscr.addstr(11,1, border*40)
	
	for i in range(1,11):
		stdscr.addstr(i, 1, border)
		stdscr.addstr(i, 40, border)
		
def draw_score():
	stdscr.addstr(0, 32, "SCORE: " + str(SCORE) + "  ")
	
def draw_food():
	stdscr.addstr(FOOD_Y, FOOD_X, ".")
	string = "x: " + str(FOOD_X) + "y: " + str(FOOD_Y) + "s        "
	stdscr.addstr(12, 20, string)

def draw_snake():
	#head
	head = ">^<v"[ANGLE]
	stdscr.addstr(Y,X, head)
	
	#tail
	if(X_SPEED > 0):
		for i in range(X-SCORE, X ):
			if(i >= MIN_X and i <= MAX_X):
				stdscr.addstr(Y, i, "-")
		
	if(X_SPEED < 0):
		for i in range(X+1, X+1+SCORE):
			if(i >= MIN_X and i <= MAX_X):
				stdscr.addstr(Y, i, "-")
		
	if(Y_SPEED < 0):
		for i in range(Y+1, Y+1+SCORE):
			if(i >= MIN_Y and i <= MAX_Y):
				stdscr.addstr(i, X, "|")
		
	if(Y_SPEED > 0):
		for i in range(Y-SCORE, Y):
			if(i >= MIN_Y and i <= MAX_Y):
				stdscr.addstr(i, X, "|")
	
	# head coords
	string = "x: " + str(X) + "y: " + str(Y) + "        "
	stdscr.addstr(12,1 , string)
	
def draw():
	clear_scenario()
	draw_borders()
	draw_score()
	draw_food()
	draw_snake()
		
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.nodelay(1)

stdscr.addstr(" use wasd to move or q to quit")

init_game()

while(True):
	u = update()
	if(u == -1):
		break
	if(u == 0):
		init_game()
		
	draw()
	time.sleep(max(0.05, 0.2-(float(SCORE)/100)))

curses.nocbreak(); stdscr.keypad(0); curses.echo(); curses.endwin()
