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

    for _ in xrange(1, 1000):
        food = world.spawn_random_food()

        if snake.overlaps(food.getx(), food.gety()):
            return False

    return True

def test_piece_overlap():
    any_x = 1
    any_y = 1

    piece = Piece(any_x, any_y)
    return piece.overlaps(any_x, any_y)

def test_piece_no_overlap():
    any_x = 1
    any_y = 1

    piece = Piece(any_x+1, any_y)
    return not piece.overlaps(any_x, any_y)

def test_snake_overlap():
    any_x = 10
    any_y = 10
    any_length = 5
    snake = Snake(0, any_x, any_y, any_length)

    for i in xrange(0, any_length):
        x = any_x-i
        y = any_y

        if not snake.overlaps(x, y):
            return False

    return True

def test_snake_overlaps_itself():
    any_x = 10
    any_y = 10
    any_length = 5
    snake = Snake(0, any_x, any_y, any_length)

    for piece in snake.body:
        if not snake.overlaps(piece.getx(), piece.gety()):
            return False

    return True


if __name__ == "__main__":
    main()
