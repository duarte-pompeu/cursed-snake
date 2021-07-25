from lib_common import *
from libcurses import *

class Turn(object):
    def __init__(self, speedX=0, speedY=0, index=0):
        self.speed = Vec2(speedX, speedY)
        self.index = index


class Food(StaticObject):

    def __init__(self, x, y, foodtype="*"):
        StaticObject.__init__(self, x, y)
        self.foodtype = foodtype

    def draw(self):
        x = self.position.x
        y = self.position.y
        draw_cur(x, y, self.foodtype)


class Piece(DynamicObject):

    def __init__(self, x=0, y=0, speed_x=1, speed_y=0):
        DynamicObject.__init__(self, x, y, speed_x, speed_y)
        self.snake_i = -1

    def draw(self, shapes="|-|-"):
        speed_x = self.getspeedx()
        speed_y = self.getspeedy()

        if speed_x == 0 and speed_y == 0:
            shape = shapes[3]

        elif speed_x > 0:
            shape = shapes[3]

        elif speed_x < 0:
            shape = shapes[1]

        elif speed_y > 0:
            shape = shapes[0]

        elif speed_y < 0:
            shape = shapes[2]

        draw_cur(self.getx(), self.gety(), shape)
