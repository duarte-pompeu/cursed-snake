#!/usr/bin/python
import random
from collections import deque

from gameobjects import *
from lib_common import *
from libcurses import *
from snake import *

class World(object):

    def __init__(self, x1, x2, y1, y2):

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.high_score = 0

        self.restart()

    def restart(self):
        self.snake = Snake(self, 10, 10, 5)
        self.turn_direction = 0
        self.foods = deque()
        self.spawn_random_food()
        self.score = 0
        self.game_on = True


    def update(self):
        snake = self.snake

        if self.turn_direction != 0:
            x = self.turn_direction.x
            y = self.turn_direction.y

            self.snake.turn(x, y)
            self.turn_direction = 0


        snake.update()

        if snake.gety() < self.y1 or snake.gety() > self.y2 or snake.getx() < self.x1 or snake.getx() > self.x2:
            self.game_over()

        for food in self.foods:
            if snake.getx() == food.position.x and snake.gety() == food.position.y:
                self.score_up(food)
                # without break, exception is raised due to deque size changing mid-loop
                break

    def score_up(self, food):
        self.foods.remove(food)
        self.snake.eat(food)
        self.score += 1
        self.high_score = max(self.score, self.high_score)
        self.spawn_random_food()

    def game_over(self):
        self.game_on = False

    def draw(self):
        draw_window(self.x1-1, self.y1-1, self.x2+1, self.y2+1)

        self.snake.draw()

        for food in self.foods:
            food.draw()

    def spawn_random_food(self):
        while True:
            x = random.randint(self.x1+1, self.x2-1)
            y = random.randint(self.y1+1, self.y2-1)

            if not self.snake.overlaps(x, y):
                break


        return self.spawn_food(x, y)

    def spawn_food(self, x, y):
        food = Food(x, y)
        self.foods.appendleft(food)
        return food

    def turn(self,x,y):
        self.turn_direction = Vec2(x, y)

    def spawn_food_test(self):
		#generates lots of food in front of the snake
        self.spawn_food(15, 10)
        self.spawn_food(16, 10)
        self.spawn_food(17, 10)
        self.spawn_food(18, 10)
        self.spawn_food(19, 10)
        self.spawn_food(20, 10)

