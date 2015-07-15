#!/usr/bin/python2

from world import *

def main():
	print test_rand_overlap()
	print test_piece_overlap()
	print test_piece_no_overlap()
	print test_snake_overlap()
	
def test_rand_overlap():
	world = World(1, 20, 7, 13)
	snake = world.snake
	
	for i in xrange(1,1000):
		food = world.spawn_random_food()
		
		if snake.overlaps(food.getX(), food.getY()):
			return False
		
	else:
		return True
		
def test_piece_overlap():
	anyX = 1
	anyY = 1
	
	piece = Piece(anyX, anyY)
	return piece.overlaps(anyX, anyY)
	
def test_piece_no_overlap():
	anyX = 1
	anyY = 1
	
	piece = Piece(anyX+1, anyY)
	return not piece.overlaps(anyX, anyY)

def test_snake_overlap():
	anyX = 10
	anyY = 10
	anyLength = 5
	snake = Snake(0, anyX, anyY, anyLength)
	
	for i in xrange(0, anyLength):
		x = anyX-i
		y = anyY
		
		if not snake.overlaps(x,y):
			return False
			
	return True
	
def test_snake_overlaps_itself():
	anyX = 10
	anyY = 10
	anyLength = 5
	snake = Snake(0, anyX, anyY, anyLength)
	
	for piece in snake.body:
		if not snake.overlaps(piece.getX(), piece.getY()):
			return False
			
	return True
	

if __name__ == "__main__":
	main()
