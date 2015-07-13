#!/usr/bin/python2
from lib_common import *

class Piece:

	def __init__(self, x=0, y=0, speed_x=1, speed_y=0):
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
		head = self.body[0]
		
		# dont turn to the direction you're already facing
		if head.getSpeedX() is x and head.getSpeedY() is y:
			return
			
		# or the opposite - snake doesnt go back
		if head.getSpeedX() is -x and head.getSpeedY() is -y:
			return
			
		self.turning_points.append(0)
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
		
		# tODO : pop up turns
		# its kind of tricky to do so - reduce a list size while you iterate it
			
	def size(self):
		return len(self.body)


	def draw(self):
		self.draw_head()
		
		for piece in self.body[1:]:
			self.draw_body_piece(piece)


	def draw_head(self):
		self.draw_piece(self.body[0], "^<V>")
	
	
	def draw_body_piece(self, piece):
		self.draw_piece(piece, "|-|-")
		
		
	def draw_piece(self, piece, shapes):
		speed_x = piece.getSpeedX()
		speed_y = piece.getSpeedY()

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
			
		draw_cur(piece.getX(), piece.getY(), shape)


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
