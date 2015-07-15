#!/usr/bin/python2
from snake import *
from world import *
from libcurses import *
import time

X_LIMIT, Y_LIMIT = [0, 0]
SLEEP_TIME = 0
MSG_RESTART = "press any key to continue"
MSG_PLAY = "use wasd to move or q to quit"

def main():

    try:
        world = init_all()

        while True:
            if check_input(world) == -1:
                break

            update(world)

            if world.game_on:
                draw(world, MSG_PLAY)

                global SLEEP_TIME
                SLEEP_TIME = max(0.1, 0.35 - 0.01 * world.score)
                time.sleep(SLEEP_TIME)

            elif not world.game_on:
                draw(world, MSG_RESTART)
                nodelay(0)
                check_input(world)
                nodelay(1)
                world.restart()

    except Exception, e:
        close_curses()
        raise

    finally:
        close_curses()

def init_all():
    global X_LIMIT, Y_LIMIT
    X_LIMIT, Y_LIMIT = init_curses()
    world = World(1, min(20, X_LIMIT-2), 7, min(Y_LIMIT-1, 13))

    return world

def update(world):
    world.update()

def draw(world, instructions):
    clear_screen()
    draw_pannel(world, instructions)
    world.draw()

def draw_pannel(world, instructions):
    y = 5
    draw_window_y(1, y)
    msg = "SCORE: " + str(world.score)
    draw_cur(2, y-1, msg)
    draw_cur(2, y-2, instructions)
    dev_log = "[DEVLOG]"
    dev_log += " WINDOW LIMITS: " + str(X_LIMIT) + ":" + str(Y_LIMIT)
    dev_log += " SLEEP_TIME: " + str(SLEEP_TIME)
    draw_cur(2, y-3, dev_log)


if __name__ == "__main__":
    main()
