#!/usr/bin/python

class Vec2:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y


	def add(self, vec2):
		self.x += vec2.x
		self.y += vec2.y

	def toString(self):
		return "x: %d, y: %d" %(self.x,self.y)
