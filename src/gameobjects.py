from lib_common import DynamicObject, StaticObject, Vec2
from libcurses import draw_cur


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
        self.right = right


class ShapesWithCorners:
    def __init__(
        self,
        up,
        left,
        down,
        right,
        upleft,
        upright,
        downleft,
        downright,
        leftup,
        leftdown,
        rightup,
        rightdown,
    ):
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

    def draw(self, shapes: ShapesWithCorners, next_piece: DynamicObject = None):

        # default case, eg game start
        shape = shapes.right

        if not self.is_moving():
            shape = shapes.right

        elif self.is_moving_right():

            # default case
            shape = shapes.right

            # other cases: theres a next piece moving up or down
            if next_piece and next_piece.is_moving_up():
                shape = shapes.rightup

            if next_piece and next_piece.is_moving_down():
                shape = shapes.rightdown

        elif self.is_moving_left():
            # default case
            shape = shapes.left

            # other cases: theres a next piece moving up or down
            if next_piece and next_piece.is_moving_up():
                shape = shapes.leftup

            if next_piece and next_piece.is_moving_down():
                shape = shapes.leftdown

        elif self.is_moving_up():
            # default case
            shape = shapes.up

            # other cases: theres a next piece moving left or right
            if next_piece and next_piece.is_moving_left():
                shape = shapes.upleft

            if next_piece and next_piece.is_moving_right():
                shape = shapes.upright

        elif self.is_moving_down():
            # default case
            shape = shapes.down

            # other cases: theres a next piece moving left or right
            if next_piece and next_piece.is_moving_left():
                shape = shapes.downleft

            if next_piece and next_piece.is_moving_right():
                shape = shapes.downright

        draw_cur(self.getx(), self.gety(), shape)
