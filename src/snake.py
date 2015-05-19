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

	def toString(self):
		msg = "SNAKE size: %d\n" % self.size()
		msg += "pos: (%s) $ speed (%s)" %(self.position.toString(), self.speed.toString())


	def draw(self):
		draw_cur(self.getX(), self.getY(), ">")
		
		for piece in self.body_parts[1:]:
			draw_cur(piece.x, piece.y, "=")
		

	def getX(self):
		return self.position.x


	def getY(self):
		return self.position.y

		return msg
