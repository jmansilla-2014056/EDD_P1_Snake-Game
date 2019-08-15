from Game.Doublylinkedlist import Node
from Game.Stack import Stack
from graphviz import Digraph
import datetime


def graphstack(stack):
    s = Digraph('structs', filename='stack.gv', node_attr={'shape': 'record'})
    u = stack.get_size()
    g = ''
    for x in range(0, u):
        g = g + '|' + str(stack.pop())

    g = str(stack.pop()) + g

    s.node('stack', "{" + g + "}")
    s.view()


def graphdoubly(linked_list):
    s = Digraph('structs', filename='snake.gv', node_attr={'shape': 'record'})

    s.attr(rankdir='LR')
    n = linked_list.start_node
    s.edge(str(n), 'Head', constraint='false')
    s.edge('Head', str(n), style='invisible',  dir='none')
    while n is not None:
        s.node(str(n), '{ |' + str(n.item) + '|}')
        n = n.prev

    s.node('None', 'Tail')

    n = linked_list.start_node
    while n is not None:
        if n.prev is not None and n is not None:
            s.edge(str(n.prev), str(n))
        else:
            s.edge(str(n), 'None', constraint='true')
        n = n.prev

    n = linked_list.start_node

    while n is not None:
        if n.prev is not None and n is not None:
            s.edge(str(n), str(n.prev), constraint='true')
        n = n.prev

    s.view()


def graphcircular(cdl):
    s = Digraph('structs', filename='circular.gv', node_attr={'shape': 'record'})
    s.attr(rankdir='LR')
    index = cdl.first
    n = cdl.first
    while True:
        n = n.next
        s.node(str(n), '{|' + n.item[0] + '|}')
        if n == index:
            break

    n = cdl.first
    while True:
        n = n.next
        s.edge(str(n), str(n.next))
        s.edge(str(n), str(n.prev))
        if n == index:
            break
    s.view()


def graphsimple(likedlist):
    s = Digraph('structs', filename='simple.gv', node_attr={'shape': 'record'})
    s.attr(rankdir='LR')
    n = likedlist.head
    while n is not None:
        s.node(str(n), '{' + str(n.data) + '|}')
        n = n.next
    n = likedlist.head
    while n is not None:
        s.edge(str(n), str(n.next))
        n = n.next
    s.view()
