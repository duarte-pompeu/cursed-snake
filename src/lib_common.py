class Vec2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, vec2):
        """This method is destructive! <returns tears in non-functional approach>"""
        self.x += vec2.x
        self.y += vec2.y

        return Vec2(self.x, self.y)

    def getcopy(self):
        return Vec2(self.x, self.y)

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    def tostring(self):
        return "x: %d, y: %d" % (self.x, self.y)


class StaticObject(object):
    def __init__(self, x=0, y=0):
        self.position = Vec2(x, y)

    def overlaps(self, x, y):
        return self.getx() is x and self.gety() is y

    def setposition(self, x, y):
        self.position = Vec2(x, y)

    def getposition(self):
        return self.position

    def getx(self):
        return self.position.x

    def gety(self):
        return self.position.y


class DynamicObject(StaticObject):
    def __init__(self, x=0, y=0, speedx=0, speedy=0):
        StaticObject.__init__(self, x, y)
        self.speed = Vec2(speedx, speedy)

    def update(self):
        self.position.add(self.speed)

    def setspeed(self, x, y):
        self.speed = Vec2(x, y)

    def getspeed(self):
        return self.speed

    def getspeedx(self):
        return self.speed.x

    def getspeedy(self):
        return self.speed.y

    def is_moving(
        self,
    ):
        return self.getspeedy != 0 or self.getspeedx != 0

    def is_moving_up(
        self,
    ):
        return self.getspeedy() > 0

    def is_moving_left(
        self,
    ):
        return self.getspeedx() < 0

    def is_moving_down(
        self,
    ):
        return self.getspeedy() < 0

    def is_moving_right(
        self,
    ):
        return self.getspeedx() > 0
