import random
import curses

s= curses.initscr()
curses.curses_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2

snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGTH

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key




