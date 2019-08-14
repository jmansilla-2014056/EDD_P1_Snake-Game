import curses
import random
import time
from curses import textpad

from Game import ReportSnake
from Game.Doublylinkedlist import DoublyLinkedList, Node
from Game.Stack import Stack


def create_food(dl, box):
    """Simple function to find coordinates of food which is inside box and not on snake body"""
    food = None
    while food is None:
        food = [random.randint(box[0][0] + 1, box[1][0] - 1),
                random.randint(box[0][1] + 1, box[1][1] - 1)]

        n = dl.start_node
        while n is not None:
            if food == n.item:
                food = None
                break
            n = n.prev

    return food


def create_poison(dl, box):
    """Simple function to find coordinates of food which is inside box and not on snake body"""
    poison = None
    while poison is None:
        poison = [random.randint(box[0][0] + 1, box[1][0] - 1),
                  random.randint(box[0][1] + 1, box[1][1] - 1)]
        n = dl.start_node
        while n is not None:
            if poison == n.item:
                poison = None
                break
            n = n.prev
    return poison


def gamer(stdscr):
    # initial settings
    global new_head
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(0)

    # create a game box
    sh = 30

    sw = 45
    box = [[3, 3], [sh - 3, sw - 3]]  # [[ul_y, ul_x], [dr_y, dr_x]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stack = Stack()

    linked_list = DoublyLinkedList()
    linked_list.insert_in_emptylist([sh // 2, sw // 2 + 1])
    linked_list.insert_at_start([sh // 2, sw // 2])
    linked_list.insert_at_start([sh // 2, sw // 2 - 1])

    # create snake and set initial direction
    direction = curses.KEY_LEFT

    # draw snake
    # for y, x in snake:
    #    stdscr.addstr(y, x, '#')

    n = linked_list.start_node
    while n is not None:
        stdscr.addstr(n.item[0], n.item[1], '#')
        n = n.prev

    # create food
    food = create_food(linked_list, box)
    stdscr.addstr(food[0], food[1], '+')
    poison = create_poison(linked_list, box)
    stdscr.addstr(poison[0], poison[1], '*')

    # print score
    score = 0
    level = 1
    score_text = "Score: {}".format(score)
    stdscr.addstr(1, sw // 2 - len(score_text) // 2, score_text)
    level_text = "Level: {}".format(level)
    stdscr.addstr(2, sw // 2 - len(level_text) // 2, level_text)

    while 1:
        # non-blocking input
        key = stdscr.getch()

        # set direction if user pressed any arrow key
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
            direction = key

        # find next position of snake head
        snake = []
        n = linked_list.start_node
        while n is not None:
            snake.insert(len(snake), n.item)
            n = n.prev
        head = linked_list.start_node.item
        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
            time.sleep(0.1 / level)
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
            time.sleep((0.1 / level))
        elif direction == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
            time.sleep(2 / (level * 8))
        elif direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
            time.sleep(2 / (level * 9))

        # insert and print new head time.sleep(0.5)
        stdscr.addstr(new_head[0], new_head[1], '#')
        # snake.insert(0, new_head)
        linked_list.insert_at_start(new_head)
        snake.insert(0, new_head)

        # if sanke head is on food
        if linked_list.start_node.item == food:
            stack.push(food)
            # update score
            score += 1
            score_text = "Score: {}".format(score)
            stdscr.addstr(1, sw // 2 - len(score_text) // 2, score_text)

            # create new food
            food = create_food(linked_list, box)
            stdscr.addstr(food[0], food[1], '+')

            # increase speed of game
            level = 1 + int(score / 15)
            level_text = "Level: {}".format(level)
            stdscr.addstr(2, sw // 2 - len(level_text) // 2, level_text)
            curses.curs_set(0)
            stdscr.nodelay(1)
            # stdscr.timeout(100 - level*25)
        elif linked_list.start_node.item == poison:
            # update score
            score -= 1
            score_text = "Score: {}".format(score)
            stdscr.addstr(1, sw // 2 - len(score_text) // 2, score_text)

            temp = snake[len(snake) - 1]

            stdscr.addstr(temp[0], temp[1], '/')
            snake.pop(len(snake) - 1)
            linked_list.delete_at_end()

            # create new poison
            poison = create_poison(linked_list, box)
            stdscr.addstr(poison[0], poison[1], '*')

            # decrease speed of game
            level = 1 + int(score / 15)
            level_text = "Level: {}".format(level)
            stdscr.addstr(2, sw // 2 - len(level_text) // 2, level_text)
            curses.curs_set(0)
            stdscr.nodelay(1)
            # stdscr.timeout(100 - level * 25)
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()
            stack.pop()
            linked_list.delete_at_end()
            stdscr.refresh()

        else:
            # shift snake's tail
            stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()
            linked_list.delete_at_end()

        # conditions for game over

        if poison == food:
            create_poison(linked_list, box)

        if (snake[0][0] in [box[0][0], box[1][0]] or
                snake[0][1] in [box[0][1], box[1][1]] or
                linked_list.count() <= 2 or
                snake[0] in snake[1:]):
            msg = "Game Over!" + str(linked_list.count())

            stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            rs = ReportSnake
            rs.graphstack(stack)
            rs.graphdoubly(linked_list)
            while 1:
                key = stdscr.getch()
                if key == curses.KEY_ENTER or key in [10, 13]:
                    break

            stdscr.nodelay(0)
            stdscr.getch()
            break


class Snake:
    pass
