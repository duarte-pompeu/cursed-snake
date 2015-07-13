#!/usr/bin/python
from lib_common import *
from snake import *

class World:
	
	def __init__(self, x1, x2, y1, y2):
		self.snake = Snake(10,10, 5)
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		
	def update(self):
		self.snake.update()

	def draw(self):
		clear_screen()
		draw_window_y(1, 5)
		draw_cur(2, 4, " use wasd to move or q to quit")
		limits_msg = " LIMITS: " + str(self.x2) + ":" + str(self.y2)
		draw_cur(2, 3, limits_msg)
		
		self.snake.draw()
