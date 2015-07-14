#!/usr/bin/python
import random
from lib_common import *
from snake import *

class Food:
	
	def __init__(self, x,y,foodtype="*"):
		self.position = Vec2(x,y)
		self.foodtype = foodtype
		
	def draw(self):
		x = self.position.x
		y = self.position.y
		draw_cur(x,y,self.foodtype)
	
class World:
	
	def __init__(self, x1, x2, y1, y2):
		self.snake = Snake(10,10, 5)
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.turn_direction = 0
		
		self.spawn_food()
		
	def update(self):
		
		if(self.turn_direction != 0):
			x = self.turn_direction.x
			y = self.turn_direction.y
			
			self.snake.turn(x,y)
			self.turn_direction = 0
			
		
		self.snake.update()
		
		if self.snake.getX() == self.food.position.x and self.snake.getY() == self.food.position.y:
			self.spawn_food()

	def draw(self):
		#~ draw_window(self.x1+1,self.x2,self.y1,self.y2)
		
		self.snake.draw()
		self.food.draw()
		
	def spawn_food(self):
		x = random.randint(self.x1,self.x2)
		y = random.randint(6,self.y2)
		
		self.food = Food(x,y)
	
	def turn(self,x,y):
		self.turn_direction = Vec2(x,y)
	
