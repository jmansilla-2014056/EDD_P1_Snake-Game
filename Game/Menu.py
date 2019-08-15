import os
import subprocess
import sys

from Game import Snake, ReportSnake, LinkedList
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
    global cdl, n, linkelist, getLists
    cdl = CircularDoublyLinkedList()
    linkelist = LinkedList.linked_list()
    n = None
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        try:
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == 0:
                    print_center(stdscr, "Enter a File")
                elif current_row == 2 and n is None:
                    print_center(stdscr, "Enter a name")
                elif current_row == 4:
                    scores = []
                    m = linkelist.head
                    stdscr.clear()
                    count = 0
                    while m is not None:
                        count += 1
                        stdscr.addstr(count, 0, str(m.data[0]) + ":" + str(m.data[1]))
                        m = m.next
                    stdscr.refresh()
                else:
                    print_center(stdscr, "You selected '{}'".format(menu[current_row]))
                stdscr.getch()
                # Bulk
                if current_row == 0:
                    clear = lambda: os.system('cls')
                    clear()
                    sys.stdout.flush()
                    g = input()
                    cdl = Bulk.users(g)
                    if n is not None:
                        cdl.insert_at_beg(n)
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
                        g = input()
                        matrix = [g, 0]
                        node = Node(matrix)
                        cdl.insert_at_end(node)
                        n = node
                        getLists = Snake.gamer(stdscr)
                        linkelist.add_at_front([n.item[0], getLists[0]])
                    else:
                        getLists = Snake.gamer(stdscr)
                        linkelist.add_at_front([n.item[0], getLists[0]])
                if current_row == 3:
                    while 1:
                        try:
                            print_center(stdscr, "F2: Stack, F3: List Double,  F4: Circular, F5: Simple ")
                            key = stdscr.getch()
                            if key == curses.KEY_F2:
                                ReportSnake.graphstack(getLists[1])
                                break
                            elif key == curses.KEY_F3:
                                ReportSnake.graphdoubly(getLists[2])
                                break
                            elif key == curses.KEY_F4:
                                ReportSnake.graphcircular(cdl)
                                break
                            elif key == curses.KEY_F5:
                                ReportSnake.graphsimple(linkelist)
                                break
                        except:
                            print_center(stdscr, 'Error whit this selection')
                            key = stdscr.getch()
                            break
                # if user selected last row, exit the program
                if current_row == len(menu) - 1:
                    break

            print_menu(stdscr, current_row)
        except:
            print_center(stdscr, 'Error')
            key = stdscr.getch()
            continue


curses.wrapper(main)
