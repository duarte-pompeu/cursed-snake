#!/usr/bin/python
from snake import *

def main():
	snake = Snake(10,11)
	print snake.toString()

	snake.turn(1,0)
	snake.update()
	print snake.toString()



if __name__ == "__main__":
	main()
