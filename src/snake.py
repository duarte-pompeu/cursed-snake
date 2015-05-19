#!/usr/bin/python
from lib_common import *

class Snake:
	
	def __init__(self, x=0, y=0):
		self.position = Vec2(x,y)
		self.speed = Vec2(0,0)

		self.body_parts = list()
		self.body_parts.append(self.position)
		
		self.turning_points = list()
		self.turning_points.append(self.position)


	def turn(self, x,y):
		self.speed.x = x
		self.speed.y = y

	def update(self):
		self.position.add(self.speed)

	def size(self):
		return len(self.body_parts)

	def toString(self):
		msg = "SNAKE size: %d\n" % self.size()
		msg += "pos: (%s) $ speed (%s)" %(self.position.toString(), self.speed.toString())

		return msg
