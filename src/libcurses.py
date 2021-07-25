import curses

X_TERM_LIM = 0
Y_TERM_LIM = 0

def init_curses():
    global X_TERM_LIM, Y_TERM_LIM

    global STDSCR
    STDSCR = curses.initscr()

    curses.use_env(True)
    Y_TERM_LIM, X_TERM_LIM = STDSCR.getmaxyx()

    #~ time.sleep(1)

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    STDSCR.keypad(1)
    STDSCR.nodelay(1)

    return X_TERM_LIM, Y_TERM_LIM


def check_input(world):

    c = STDSCR.getch()

    if c == ord('w'):
        world.turn(0, 1)

    elif c == ord('a'):
        world.turn(-1, 0)

    elif c == ord('s'):
        world.turn(0, -1)

    elif c == ord('d'):
        world.turn(1, 0)

    elif c == ord('q'):
        return -1


def close_curses():
    curses.nocbreak()
    STDSCR.keypad(0)
    curses.echo()
    curses.endwin()

def clear_screen():
    STDSCR.clear()

def nodelay(n):
    STDSCR.nodelay(n)

def draw_window(x1, y1, x2, y2):
    line = "#"* (x2-x1)
    #~ col = "#\n" * (y2-y1)

    draw_cur(x1, y1, line)
    draw_cur(x1, y2, line)

    for i in range(y1, y2+1):
        draw_cur(x1, i, "#")
        draw_cur(x2, i, "#")

def draw_window_y(y1, y2):
    x1 = 0
    x2 = X_TERM_LIM

    draw_window(x1, y1, x2-1, y2)


def draw_cur(x, y, msg):
    real_x = x
    real_y = Y_TERM_LIM - y

    if real_x < 0 or real_x > X_TERM_LIM:
        return

    if real_y < 0 or real_y > Y_TERM_LIM:
        return

    try:
        STDSCR.addstr(real_y, real_x, msg)

    except:
        pass
