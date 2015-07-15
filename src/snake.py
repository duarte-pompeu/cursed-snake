#!/usr/bin/python2
from collections import deque
from lib_common import *

class Piece:

	def __init__(self, x=0, y=0, speed_x=1, speed_y=0):
		self.position = Vec2(x,y)
		self.speed = Vec2(speed_x, speed_y)
		self.snake_i = -1
		
	def draw(self, shapes="|-|-"):
		speed_x = self.getSpeedX()
		speed_y = self.getSpeedY()

		if speed_x is 0 and speed_y is 0:
			shape = shapes[3]
		
		elif speed_x > 0:
			shape = shapes[3]

		elif speed_x < 0:
			shape = shapes[1]

		elif speed_y > 0:
			shape = shapes[0]

		elif speed_y < 0:
			shape = shapes[2]
			
		draw_cur(self.getX(), self.getY(), shape)

	def update(self):
		self.position.add(self.speed)
		
	def overlaps(self, x, y):
		return self.getX() is x and self.getY() is y
	
	def getX(self):
		return self.position.x

	def getY(self):
		return self.position.y

	def getSpeedX(self):
		return self.speed.x

	def getSpeedY(self):
		return self.speed.y

	def setSpeed(self, x, y):
		self.speed = Vec2(x,y)
	

	
class Snake:
	
	def __init__(self, world, x=0, y=0, size=0):
		self.world = world
		
		head = Piece(x,y)

		self.body = list()
		self.body.append(head)
		
		for i in xrange(1, size+1):
			self.body.append(Piece(x-i, y))
			
		self.turning_points = deque()
		self.food = deque()
		

	def turn(self, x,y):
		head = self.body[0]
		
		# dont turn to the direction you're already facing
		if head.getSpeedX() is x and head.getSpeedY() is y:
			return
			
		# or the opposite - snake doesnt go back
		if head.getSpeedX() is -x and head.getSpeedY() is -y:
			return
			
		head.setSpeed(x,y)
		self.turning_points.appendleft(Turn(self.getSpeedX(), self.getSpeedY()))


	def update(self):
		body = self.body
		turns = self.turning_points
		food = self.food

		head = body[0]
		head.update()
		
		for i in xrange(1, len(body)):
			piece = body[i]

			for turn in turns:
				if turn.index == i: 
					piece.speed = turn.speed.getCopy()
			
			piece.update()

		for turn in turns:
			turn.index += 1
		
		if turns and turns[-1].index == len(body):
			turns.pop()
		# TODO : pop up turns and food
		# its kind of tricky to do so - reduce a list size while you iterate it
			
		for i in xrange(0, len(food)):
			f = food[i]
			f.snake_i += 1
			
			if f.snake_i == len(body):
				food.pop()
				self.grow(f)
				
			
		self.check_self_collision()
	
	def grow(self, food):
		x = food.position.x
		y = food.position.y
		
		new_piece = Piece(x,y)
		new_piece.speed = self.body[-1].speed.getCopy()
		
		self.body.append(new_piece)

	def check_self_collision(self):
		body = self.body
		
		for i in xrange(1, len(body)):
			piece = body[i]
			
			if self.getX() is piece.position.x and self.getY() is piece.position.y:
				self.world.game_over()
				break
				
	def overlaps(self, x, y):
		for piece in self.body:
			if piece.overlaps(x,y):
				return True
				
		else:
			return False
				
	def size(self):
		return len(self.body)
		
	def eat(self, food):
		food.snake_i = 0
		self.food.appendleft(food)


	def draw(self):
		if any (food.snake_i == 0 for food in self.food):
			self.draw_head_eating()
		
		else: self.draw_head()
		
		for i in xrange(1,len(self.body)):
			piece = self.body[i]
			
			for food in self.food:
				food_pos = food.snake_i
				
				if food_pos == i:
					piece.draw(""""="=""")
					break
			
			else:
				piece.draw()


	def draw_head(self):
		self.body[0].draw("^<V>")

	def draw_head_eating(self):
		self.body[0].draw("V>^<")

	def toString(self):
		msg = "SNAKE size: %d\n" % self.size()
		msg += "pos: (%s) $ speed (%s)" %(self.getPosition().toString(), self.getSpeed().toString())

		return msg


	def getX(self):
		return self.body[0].getX()
		
	def getY(self):
		return self.body[0].getY()

	def getSpeedX(self):
		return self.body[0].getSpeedX()

	def getSpeedY(self):
		return self.body[0].getSpeedY()

	def setSpeed(self, x, y):
		self.body[0].setSpeed(x,y)

	def getPosition(self):
		return self.body[0].position

	def getSpeed(self):
		return self.body[0].speed
		
	def getLength(self):
		return len(self.body)
