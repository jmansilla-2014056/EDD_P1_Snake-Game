import csv
from tkinter import messagebox

from Game.CircularDoublyLinkedList import CircularDoublyLinkedList
from Game.Doublylinkedlist import Node


def users(direct):
    with open(direct, 'r') as f:
        reader = csv.reader(f)
        listN = list(reader)
        cdl = CircularDoublyLinkedList()

    for x in listN[:]:
        new_node = Node(x)
        cdl.insert_at_beg(new_node)

    index = cdl.first
    n = cdl.first
    while True:
        n = n.next
        if n == index:
            break

    return cdl
