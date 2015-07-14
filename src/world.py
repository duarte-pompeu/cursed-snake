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
		
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		
		self.restart()
		
		
		
		
	def restart(self):
		self.snake = Snake(self,10,10, 5)
		self.turn_direction = 0
		self.spawn_food()
		
		
	def update(self):
		snake = self.snake
		food = self.food
		
		if(self.turn_direction != 0):
			x = self.turn_direction.x
			y = self.turn_direction.y
			
			self.snake.turn(x,y)
			self.turn_direction = 0
			
		
		snake.update()
		
		if snake.getY() < self.y1 or snake.getY() > self.y2 or snake.getX() < self.x1 or snake.getX() > self.x2:
			self.game_over()
		
		if snake.getX() == food.position.x and snake.getY() == food.position.y:
			self.score()

	def score(self):
		self.spawn_food()
		
	def game_over(self):
		self.restart()
	
	def draw(self):
		draw_window(self.x1-1,self.y1-1,self.x2+1,self.y2+1)
		
		self.snake.draw()
		self.food.draw()
		
	def spawn_food(self):
		x = random.randint(self.x1+1,self.x2-1)
		y = random.randint(self.y1+1,self.y2-1)
		
		self.food = Food(x,y)
	
	def turn(self,x,y):
		self.turn_direction = Vec2(x,y)
	
