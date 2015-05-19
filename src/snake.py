#!/usr/bin/python
from lib_common import *

class Snake:
	
	def __init__(self, x=0, y=0, size=0):
		self.position = Vec2(x,y)
		self.speed = Vec2(0,0)

		self.body_parts = list()
		self.body_parts.append(self.position)
		
		self.turning_points = list()
		self.turning_points.append(self.position)

		for i in xrange(1, size+1):
			self.body_parts.append(Vec2(x-i, y))


	def turn(self, x,y):
		self.speed.x = x
		self.speed.y = y

	def update(self):
		for part in self.body_parts:
			part.add(self.speed)

	def size(self):
		return len(self.body_parts)


	def draw(self):
		head_symbol = self.get_head_symbol()
		draw_cur(self.getX(), self.getY(), head_symbol)
		
		for piece in self.body_parts[1:]:
			draw_cur(piece.x, piece.y, "=")

	def get_head_symbol(self):
		speed_x = self.getSpeedX()
		speed_y = self.getSpeedY()
		
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
		msg += "pos: (%s) $ speed (%s)" %(self.position.toString(), self.speed.toString())

		return msg


	def getX(self):
		return self.position.x


	def getY(self):
		return self.position.y

	def getSpeedX(self):
		return self.speed.x

	def getSpeedY(self):
		return self.speed.y

		
