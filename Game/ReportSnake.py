from Game.Doublylinkedlist import Node
from Game.Stack import Stack
from graphviz import Digraph
import datetime


def graphstack(stack):
    s = Digraph('structs', filename='stack.gv', node_attr={'shape': 'record'})
    u = stack.get_size()
    g = ''
    for x in range(0, u):
        g = g + str(stack.pop()) + '|'

    g = g + str(stack.pop())

    s.node('stack', "{" + g + "}")
    s.view()


def graphdoubly(linked_list):
    s = Digraph('structs', filename='snake.gv', node_attr={'shape': 'record'})
    n = linked_list.start_node
    while n is not None:
        s.node(str(n), ' |' + str(n.item) + '|')
        n = n.nref

    n = linked_list.start_node
    while n is not None:
        s.edge(str(n), str(n.nref))
        n = n.nref

    n = linked_list.start_node
    while n is not None:
        s.edge(str(n.nref), str(n))
        n = n.nref

    s.view()

