#!/usr/bin/python
from lib_common import *

class Piece:

	def __init__(self, x=0, y=0, speed_x=0, speed_y=0):
		self.position = Vec2(x,y)
		self.speed = Vec2(speed_x, speed_y)

	def update(self):
		self.position.add(self.speed)
	
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
	
	def __init__(self, x=0, y=0, size=0):
		head = Piece(x,y)

		self.body = list()
		self.body.append(head)
		
		for i in xrange(1, size+1):
			self.body.append(Piece(x-i, y))
			
		self.turning_points = list()
		

	def turn(self, x,y):
		self.turning_points.append(0)

		head = self.body[0]
		head.setSpeed(x,y)



	def update(self):
		body = self.body
		turns = self.turning_points

		head = body[0]
		head.update()
		
		for i in xrange(1, len(body)):
			piece = body[i]

			if i in turns:
				piece.speed = body[i-1].speed
			
			piece.update()

		for i in xrange(0, len(turns)):
			turns[i] += 1

	def size(self):
		return len(self.body)


	def draw(self):
		head_symbol = self.get_head_symbol()
		draw_cur(self.getX(), self.getY(), head_symbol)
		
		for piece in self.body[1:]:
			draw_cur(piece.getX(), piece.getY(), "=")


	def get_head_symbol(self):
		speed_x = self.getSpeedX()
		speed_y = self.getSpeedY()

		if speed_x is 0 and speed_y is 0:
			return ">"
		
		if speed_x > 0:
			return ">"

		elif speed_x < 0:
			return "<"

		elif speed_y > 0:
			return "^"

		elif speed_y < 0:
			return "V"



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
