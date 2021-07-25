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


class SimpleShapes:
    def __init__(self, up, left, down, right):
        self.up = up
        self.left = left
        self.down = down
        self.right=right

class ShapesWithCorners:
    def __init__(self, up, left, down, right, upleft, upright, downleft, downright, leftup, leftdown, rightup, rightdown):
        self.up = up
        self.left = left
        self.down = down
        self.right = right
        self.upleft = upleft
        self.upright = upright
        self.downleft = downleft
        self.downright = downright
        self.leftup = leftup
        self.leftdown = leftdown
        self.rightup = rightup
        self.rightdown = rightdown


class Piece(DynamicObject):

    def __init__(self, x=0, y=0, speed_x=1, speed_y=0):
        DynamicObject.__init__(self, x, y, speed_x, speed_y)
        self.snake_i = -1


    
    def draw(self, shapes: ShapesWithCorners, next_piece : DynamicObject  = None):
        speed_x = self.getspeedx()
        speed_y = self.getspeedy()

        is_moving = lambda piece : piece.getspeedy != 0 or piece.getspeedx != 0
        is_moving_up = lambda piece : piece.getspeedy() > 0 
        is_moving_left = lambda piece : piece.getspeedx() < 0 
        is_moving_down = lambda piece : piece.getspeedy() < 0 
        is_moving_right = lambda piece : piece.getspeedx() > 0 

        # default case, eg game start
        shape = shapes.right

        if not is_moving(self):
            shape = shapes.right

        elif is_moving_right(self):

            # default case
            shape = shapes.right

            # other cases: theres a next piece moving up or down
            if next_piece and is_moving_up(next_piece): 
                shape = shapes.rightup
            
            if next_piece and is_moving_down(next_piece):
                shape = shapes.rightdown

        elif is_moving_left(self):
            # default case
            shape = shapes.left

            # other cases: theres a next piece moving up or down
            if next_piece and is_moving_up(next_piece): 
                shape = shapes.leftup
            
            if next_piece and is_moving_down(next_piece):
                shape = shapes.leftdown

        elif is_moving_up(self):
            # default case
            shape = shapes.up

            # other cases: theres a next piece moving left or right
            if next_piece and is_moving_left(next_piece): 
                shape = shapes.upleft
            
            if next_piece and is_moving_right(next_piece):
                shape = shapes.upright

        elif is_moving_down(self):
            # default case
            shape = shapes.down

            # other cases: theres a next piece moving left or right
            if next_piece and is_moving_left(next_piece): 
                shape = shapes.downleft
            
            if next_piece and is_moving_right(next_piece):
                shape = shapes.downright

        draw_cur(self.getx(), self.gety(), shape)

    
    
