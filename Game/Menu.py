import os
import subprocess
import sys

from Game import Snake, ReportSnake
import curses
import time

from Game import Bulk
from Game.CircularDoublyLinkedList import CircularDoublyLinkedList
from Game.Doublylinkedlist import Node

menu = ['Bulk', 'Players', 'Play', 'Reports', 'Scores', 'Exit']


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    global cdl, n
    cdl = CircularDoublyLinkedList()
    n = None
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            stdscr.getch()
            # Bulk
            if current_row == 0:
                clear = lambda: os.system('cls')
                clear()
                sys.stdout.flush()
                print('file:')
                g = input()
                cdl = Bulk.users(g)
            # Players
            if current_row == 1:
                n = cdl.first
                print_center(stdscr, "<<    " + n.item[0] + "    >>")
                while 1:
                    key = stdscr.getch()
                    if key == curses.KEY_RIGHT:
                        n = n.next
                        print_center(stdscr, "<<    " + n.item[0] + "   >>")
                    elif key == curses.KEY_LEFT:
                        n = n.prev
                        print_center(stdscr, "<<    " + n.item[0] + "   >>")
                    elif key == curses.KEY_ENTER or key in [10, 13]:
                        break
            # Play
            if current_row == 2:
                if n is None:
                    clear = lambda: os.system('cls')
                    clear()
                    sys.stdout.flush()
                    print('user:')
                    g = input()
                    matrix = [g, 0]
                    node = Node(matrix)
                    cdl.insert_at_end(node)
                    n = node
                    Snake.gamer(stdscr)
                else:
                    Snake.gamer(stdscr)
            if current_row == 3:
                while 1:
                    try:
                        print_center(stdscr, "F2: Stack, F3: List Double,  F4: Circular, F5: Simple ")
                        key = stdscr.getch()
                        if key == curses.KEY_F2:
                            subprocess.Popen('stack.gv.pdf', shell=True)
                            break
                        elif key == curses.KEY_F3:
                            subprocess.Popen('snake.gv.pdf', shell=True)
                            break
                        elif key == curses.KEY_F4:
                            ReportSnake.graphcircular(cdl)
                            break
                    except:
                        break
            # if user selected last row, exit the program
            if current_row == len(menu) - 1:
                break

        print_menu(stdscr, current_row)


curses.wrapper(main)
