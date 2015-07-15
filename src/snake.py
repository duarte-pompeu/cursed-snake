#!/usr/bin/python2
from collections import deque

from lib_common import *
from libcurses import *
from gameobjects import *

class Snake(DynamicObject):

    def __init__(self, world, x=0, y=0, size=0):
        DynamicObject.__init__(self, x, y)
        self.world = world

        head = Piece(x, y)

        self.body = list()
        self.body.append(head)

        for i in xrange(1, size):
            self.body.append(Piece(x-i, y))

        self.turning_points = deque()
        self.food = deque()


    def turn(self, x, y):
        head = self.body[0]

        # dont turn to the direction you're already facing
        if head.getspeedx() is x and head.getspeedy() is y:
            return

        # or the opposite - snake doesnt go back
        if head.getspeedx() is -x and head.getspeedy() is -y:
            return

        head.setspeed(x, y)
        self.turning_points.appendleft(Turn(self.getspeedx(), self.getspeedy()))


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
                    piece.speed = turn.speed.getcopy()

            piece.update()

        for turn in turns:
            turn.index += 1

        if turns and turns[-1].index is len(body):
            turns.pop()

        for i in xrange(0, len(food)):
            f = food[i]
            f.snake_i += 1

            if f.snake_i is len(body):
                food.pop()
                self.grow(f)

        self.check_self_collision()


    def grow(self, food):
        x = food.position.x
        y = food.position.y

        new_piece = Piece(x, y)
        new_piece.speed = self.body[-1].speed.getcopy()

        self.body.append(new_piece)


    def check_self_collision(self):
        body = self.body

        for i in xrange(1, len(body)):
            piece = body[i]

            if self.getx() is piece.position.x and self.gety() is piece.position.y:
                self.world.game_over()
                break


    def overlaps(self, x, y):
        for piece in self.body:
            if piece.overlaps(x, y):
                return True

        return False


    def size(self):
        return len(self.body)


    def eat(self, food):
        food.snake_i = 0
        self.food.appendleft(food)


    def draw(self):
        if any(food.snake_i is 0 for food in self.food):
            self.draw_head_eating()

        else: self.draw_head()

        for i in xrange(1, len(self.body)):
            piece = self.body[i]

            for food in self.food:
                food_pos = food.snake_i

                if food_pos is i:
                    piece.draw(""""="=""")
                    break

            else:
                piece.draw()


    def draw_head(self):
        self.body[0].draw("^<V>")


    def draw_head_eating(self):
        self.body[0].draw("V>^<")


    def tostring(self):
        msg = "SNAKE size: %d\n" % self.size()
        msg += "pos: (%s) $ speed (%s)" %(self.getposition().tostring(), self.getspeed().tostring())

        return msg


    def getx(self):
        return self.body[0].getx()

    def gety(self):
        return self.body[0].gety()

    def getspeedx(self):
        return self.body[0].getspeedx()

    def getspeedy(self):
        return self.body[0].getspeedy()

    def setspeed(self, x, y):
        self.body[0].speed = Vec2(x, y)

    def getposition(self):
        return self.body[0].position

    def getspeed(self):
        return self.body[0].speed

    def getlength(self):
        return len(self.body)
