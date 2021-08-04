#!/usr/bin/python2
import time

from loguru import logger

from libcurses import (
    check_input,
    clear_screen,
    close_curses,
    draw_cur,
    draw_window_y,
    init_curses,
    nodelay,
)
from services.score_service import ScoreService
from utils import logging
from world import World

logging.init()

X_LIMIT, Y_LIMIT = [0, 0]
SLEEP_TIME = 0
MSG_RESTART = "press any key to continue"
MSG_PLAY = "use wasd to move or q to quit"

score_service = ScoreService()

HIGH_SCORE = score_service.get_highscore()


logger.info("Starting application...")


def update_high_score(current_score: int):
    global HIGH_SCORE

    score_service.enter_new_score(current_score)
    high_score = score_service.get_highscore()
    HIGH_SCORE = high_score


def main():

    try:
        world = init_all()

        while True:
            if check_input(world) == -1:
                break

            update(world)

            if world.game_on:
                draw(world, MSG_PLAY)

                def get_pause_time_delta(score):
                    pause_time_delta = 0.008 * min(score, 5)
                    pause_time_delta += 0.006 * min(score - 5, 5)
                    pause_time_delta += 0.004 * min(score - 10, 5)
                    pause_time_delta += 0.002 * min(score - 15, 5)
                    pause_time_delta += 0.001 * min(score - 20, 50)

                    return pause_time_delta

                global SLEEP_TIME
                pause_delta = get_pause_time_delta(world.score)
                SLEEP_TIME = max(0.035, 0.15 - pause_delta)
                time.sleep(SLEEP_TIME)

            elif not world.game_on:
                update_high_score(world.score)

                draw(world, MSG_RESTART)
                nodelay(0)
                check_input(world)
                nodelay(1)
                world.restart()

    except Exception as e:
        logger.exception(e)

    finally:
        close_curses()


def init_all():
    global X_LIMIT, Y_LIMIT
    X_LIMIT, Y_LIMIT = init_curses()
    world = World(1, min(30, X_LIMIT - 2), 7, min(Y_LIMIT - 1, 15))

    return world


def update(world: World):
    world.update()


def draw(world, instructions):
    clear_screen()
    draw_pannel(world, instructions)
    world.draw()


def draw_pannel(world, instructions):
    global HIGH_SCORE
    y = 5
    draw_window_y(1, y)
    msg = f"SCORE: {world.score} | HIGH SCORE: {HIGH_SCORE}"
    draw_cur(2, y - 1, msg)
    draw_cur(2, y - 2, instructions)
    dev_log = (
        f"[DEVLOG] WINDOW LIMITS: {X_LIMIT}:{Y_LIMIT} SLEEP_TIME: {SLEEP_TIME:.2f}"
    )
    draw_cur(2, y - 3, dev_log)


if __name__ == "__main__":
    main()
