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
    opendoubly = s
    s.view()



def graphdoubly(linked_list):
    s = Digraph('structs', filename='snake.gv', node_attr={'shape': 'record'})
    s.attr(rankdir='LR')
    n = linked_list.start_node
    while n is not None:
        s.node(str(n), '{ |' + str(n.item) + '|}')
        n = n.prev

    n = linked_list.start_node
    while n is not None:
        s.edge(str(n), str(n.prev))
        n = n.prev

    n = linked_list.start_node
    while n is not None:
        s.edge(str(n.prev), str(n))
        n = n.prev
    opendoubly = s
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


