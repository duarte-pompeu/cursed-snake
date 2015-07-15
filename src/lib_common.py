#!/usr/bin/python2

class Vec2(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, vec2):
        self.x += vec2.x
        self.y += vec2.y


    def getcopy(self):
        return Vec2(self.x, self.y)

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    def tostring(self):
        return "x: %d, y: %d" %(self.x, self.y)

class Turn(object):
    def __init__(self, speedX=0, speedY=0, index=0):
        self.speed = Vec2(speedX, speedY)
        self.index = index
