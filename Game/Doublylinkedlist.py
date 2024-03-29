class Node:
    def __init__(self, data):
        self.item = data
        self.prev = None
        self.pref = None

    def get_data(self):
        return self.item


class DoublyLinkedList:
    def __init__(self):
        self.start_prev = None
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.prev = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.prev is not None:
            n = n.prev
        new_node = Node(data)
        n.prev = new_node
        new_node.pref = n

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.prev is None:
            self.start_node = None
            return
        self.start_node = self.start_node.prev

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.prev is None:
            self.start_node = None
            return
        n = self.start_node
        while n.prev is not None:
            n = n.prev
        n.pref.prev = None

    def count(self):
        x = 0
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                x += 1
                n = n.prev
        return x
