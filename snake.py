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
	if(Y < MIN_Y):
		Y = MIN_Y +1
	if(Y > MAX_Y):
		Y = MAX_Y -1
	if(X < MIN_X):
		X = MIN_X +1
	if(X > MAX_X):
		X = MAX_X -1
		
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

def spawn_food():
	global FOOD_X
	global FOOD_Y
	FOOD_X = random.randint(MIN_X, MAX_X)
	FOOD_Y = random.randint(MIN_Y, MAX_Y)
	
	food_types = ".,@$%"
	food_type = food_types[random.randint(0,len(food_types)-1)]
	stdscr.addstr(FOOD_Y, FOOD_X, food_type)
	
def draw_score():
	stdscr.addstr(0, 32, "SCORE: " + str(SCORE))
	
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
		stdscr.addstr(Y, X-X_SPEED*SCORE, "-"*SCORE)
	if(X_SPEED < 0):
		stdscr.addstr(Y, X+1, "-"*SCORE)
		
	if(Y_SPEED < 0):
		for i in range(Y+1, Y+1+SCORE):
			stdscr.addstr(i, X, "|")
		
	if(Y_SPEED > 0):
		for i in range(Y-SCORE, Y):
			stdscr.addstr(i, X, "|")
	
	string = "x: " + str(X) + "y: " + str(Y) + "        "
	stdscr.addstr(12,1 , string)
	
def draw():
	clear_scenario()
	draw_borders()
	draw_score()
	draw_food()
	draw_snake()
		
# initscr() returns a window object representing the entire screen;
stdscr = curses.initscr()


#Usually curses applications turn off automatic echoing of keys to the screen, 
#in order to be able to read keys and only display them under certain circumstances. 
#This requires calling the noecho() function.
curses.noecho()

#Applications will also commonly need to react to keys instantly, without requiring the Enter key to be pressed;
#this is called cbreak mode, as opposed to the usual buffered input mode.
curses.cbreak()

#Terminals usually return special keys, such as the cursor keys or navigation keys such as Page Up and Home, 
#as a multibyte escape sequence. While you could write your application to expect such sequences and process them accordingly, 
#curses can do it for you, returning a special value such as curses.KEY_LEFT.
stdscr.keypad(1)

stdscr.addstr(" use wasd to move or q to quit")

X_SPEED = 0
Y_SPEED = 0
tail = "-"
head = ">"
stdscr.nodelay(1)

draw_borders()
spawn_food()
while(True):
	
	if(update() == -1):
		break
	draw()
	time.sleep(max(0.05, 0.25-(float(SCORE)/100)))
	
#Terminating a curses application is much easier than starting one. Youll need to call
curses.nocbreak(); stdscr.keypad(0); curses.echo()

#to reverse the curses-friendly terminal settings. 
#Then call the endwin() function to restore the terminal to its original operating mode.
curses.endwin()
